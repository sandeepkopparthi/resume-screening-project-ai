import json

from app.models.candidate_assessment import CandidateAssessment
from app.models.resume import Resume
from app.models.job_description import JobDescription
from app.models.candidate_evaluation import CandidateEvaluation

from app.prompts.candidate_evaluation_prompt import (
    build_candidate_evaluation_prompt,
)

from app.exceptions.parser_exceptions import EvaluationException, ParserException

from app.services.evaluation_calculator import EvaluationCalculator
from app.utils.json_utils import extract_json

class CandidateEvaluatorNode:

    def __init__(self, llm_service):
        self.llm_service = llm_service

    def evaluate(
        self,
        resume: Resume,
        job: JobDescription,
    ) -> CandidateEvaluation:

        prompt = build_candidate_evaluation_prompt(
            self,
            resume=resume,
            job=job,
        )

        response = self.llm_service.generate(
            messages=prompt,
            temperature=0
        )

        try:

            json_data = extract_json(response)

            assessment = CandidateAssessment.model_validate(json_data)

            evaluation = EvaluationCalculator.calculate(
                assessment
            )

            return evaluation

        except Exception as e:

            raise EvaluationException(
                f"Failed to evaluate candidate: {e}"
            ) from e
        