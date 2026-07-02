import json

from app.models.resume import Resume
from app.prompts.resume_parser_prompt import build_resume_parser_messages


class ResumeParser:

    def __init__(self, llm_service):
        self.llm = llm_service
    def parse(self,resume_text:str) -> Resume:
        response = self.llm.generate(
            messages=build_resume_parser_messages(resume_text),
            temperature=0
        )
        response = response.replace("```json", "")
        response = response.replace("```", "")
        print("Response from LLM:", response)
        
        response_dict = json.loads(response)
        resume = Resume.model_validate(response_dict)
        return resume

