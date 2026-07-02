import json

from app.models.job_description import JobDescription
from app.prompts.jd_prompt import build_jd_parser_prompt
from app.utils.json_utils import extract_json
from app.exceptions.parser_exceptions import ParserException


class JDParserNode:

    def __init__(self, llm_service):
        self.llm_service = llm_service

    def parse(self, job_description: str) -> JobDescription:

        prompt = build_jd_parser_prompt(job_description)

        response = self.llm_service.generate(
            messages=prompt,
            temperature=0
        )

        try:
            response = response.replace("```json", "")
            response = response.replace("```", "")
            json_data=json.loads(response)
            return JobDescription.model_validate(json_data)

        except Exception as e:
            raise ParserException(
                f"Failed to parse Job Description: {e}"
            ) from e