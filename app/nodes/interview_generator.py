# with lang graph implementation

from app.exceptions.parser_exceptions import ParserException
from app.models.candidate_assessment import CandidateAssessment
from app.models.interview_plan import InterviewPlan
from app.models.job_description import JobDescription
from app.models.resume import Resume
from app.models.screening_state import ScreeningState
from app.prompts.interview_prompt import InterviewPromptBuilder
from app.services.llm_service import LLMService
from app.utils.json_utils import extract_json

class InterviewGeneratorNode:

    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def invoke(
            self,
            state: ScreeningState,
    ) -> InterviewPlan:
            
        try:
            
            prompt = InterviewPromptBuilder.build(
                resume=state.resume,
                job=state.job_description,
                assessment=state.candidate_evaluation,
            )

            messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ]

            response = self.llm_service.generate(
                messages=messages,
                temperature=0
            )

            json_data = extract_json(response)
            interview_questions_json = InterviewPlan.model_validate(json_data)
            return state.model_copy(
                update={
                    "interview_plan": interview_questions_json
                }
            )
                
        except Exception as e:
            raise ParserException(
                f"Interview generation failed: {e}"
            ) from e

# without lang graph implementation

# from app.exceptions.parser_exceptions import ParserException
# from app.models.candidate_assessment import CandidateAssessment
# from app.models.interview_plan import InterviewPlan
# from app.models.job_description import JobDescription
# from app.models.resume import Resume
# from app.prompts.interview_prompt import InterviewPromptBuilder
# from app.services.llm_service import LLMService
# from app.utils.json_utils import extract_json

# class InterviewGeneratorNode:

#     def __init__(self, llm_service: LLMService):
#         self.llm_service = llm_service

#     def generate(
#             self,
#             resume: Resume,
#             job: JobDescription,
#             assessment: CandidateAssessment,
#     ) -> InterviewPlan:
            
#         try:
            
#             prompt = InterviewPromptBuilder.build(
#                 resume=resume,
#                 job=job,
#                 assessment=assessment,
#             )
#             print("Prompt for interview generation:", prompt)

#             messages = [
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }
#             ]

#             response = self.llm_service.generate(
#                 messages=messages,
#                 temperature=0
#             )

#             json_data = extract_json(response)
#             print("Extracted JSON data for interview plan:", json_data)
#             return InterviewPlan.model_validate(json_data)
                
#         except Exception as e:
#             raise ParserException(
#                 f"Interview generation failed: {e}"
#             ) from e