from app.exceptions.parser_exceptions import ParserException
from app.models.candidate_assessment import CandidateAssessment
from app.models.interview_plan import InterviewPlan
from app.models.job_description import JobDescription
from app.models.resume import Resume
from app.prompts.interview_prompt import InterviewPromptBuilder
from app.services.llm_service import LLMService
from app.utils.json_utils import extract_json

class InterviewGeneratorNode:

    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def generate(
            self,
            resume: Resume,
            job: JobDescription,
            assessment: CandidateAssessment,
    ) -> InterviewPlan:
            
        try:
            
            prompt = InterviewPromptBuilder.build(
                resume=resume,
                job=job,
                assessment=assessment,
            )
            print("Prompt for interview generation:", prompt)
            response = self.llm_service.generate(
                messages=prompt,
                temperature=0
            )

            json_data = extract_json(response)
            return InterviewPlan.model_validate(json_data)
                
        except Exception as e:
            raise ParserException(
                f"Interview generation failed: {e}"
            ) from e