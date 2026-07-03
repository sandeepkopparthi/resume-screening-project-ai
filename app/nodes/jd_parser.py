# with lang graph implementation
from app.models.job_description import JobDescription
from app.models.screening_state import ScreeningState
from app.parsers.pdf_parser import extract_text_from_pdf
from app.prompts.jd_prompt import build_jd_messages
from app.utils.json_utils import extract_json
from app.exceptions.parser_exceptions import ParserException


class JDParserNode:

    def __init__(self, llm_service):
        self.llm_service = llm_service

    def invoke(self, state: ScreeningState) -> JobDescription:

        job_description_text = extract_text_from_pdf(state.jd_file_path)

        messages = build_jd_messages(job_description_text)

        try:
            response = self.llm_service.generate(
                messages=messages,
                temperature=0
            )

            data = extract_json(response)

            job_desc = JobDescription.model_validate(data)

            return state.model_copy(
                update={
                    "job_description_text": job_description_text,
                    "job_description": job_desc
                }
            )
        
        except Exception as e:
                raise ParserException(
                    f"Failed to parse Job Description: {e}"
                ) from e



# without lang graph implementation

# import json

# from app.models.job_description import JobDescription
# from app.prompts.jd_prompt import build_jd_parser_prompt
# from app.utils.json_utils import extract_json
# from app.exceptions.parser_exceptions import ParserException


# class JDParserNode:

    # def __init__(self, llm_service):
    #     self.llm_service = llm_service

    # def parse(self, job_description: str) -> JobDescription:

    #     prompt = build_jd_parser_prompt(job_description)

    #     response = self.llm_service.generate(
    #         messages=prompt,
    #         temperature=0
    #     )

    #     try:
    #         response = response.replace("```json", "")
    #         response = response.replace("```", "")
    #         json_data=json.loads(response)
    #         return JobDescription.model_validate(json_data)

    #     except Exception as e:
    #         raise ParserException(
    #             f"Failed to parse Job Description: {e}"
    #         ) from e