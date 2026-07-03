# with lang graph implementation

from turtle import update

from app.models.resume import Resume
from app.models.screening_state import ScreeningState
from app.parsers.pdf_parser import extract_text_from_pdf
from app.prompts.resume_parser_prompt import  build_resume_messages
from app.utils.json_utils import extract_json

class ResumeParserNode:

    def __init__(self, llm_service):
        self.llm = llm_service

    def invoke(self, state: ScreeningState) -> ScreeningState:

        resume_text = extract_text_from_pdf(state.resume_file_path)

        messages = build_resume_messages(
            resume_text
        )

        response = self.llm.generate(messages=messages, temperature=0)

        data = extract_json(response)

        resume = Resume.model_validate(data)

        return state.model_copy(
            update={
                "resume_text": resume_text,
                "resume": resume
            }
        )

        # return state


# without lang grap implementation

# import json
# from app.models.resume import Resume
# from app.prompts.resume_parser_prompt import build_resume_parser_messages


# class ResumeParser:

#     def __init__(self, llm_service):
#         self.llm = llm_service
#     def parse(self,resume_text:str) -> Resume:
#         response = self.llm.generate(
#             messages=build_resume_parser_messages(resume_text),
#             temperature=0
#         )
#         response = response.replace("```json", "")
#         response = response.replace("```", "")
        
#         response_dict = json.loads(response)
#         resume = Resume.model_validate(response_dict)
#         return resume

