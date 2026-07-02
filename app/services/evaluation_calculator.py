from app.config.scoring import (
    TECHNICAL_WEIGHT,
    EXPERIENCE_WEIGHT,
    RESPONSIBILITY_WEIGHT,
    EDUCATION_WEIGHT,
    SOFT_SKILL_WEIGHT,
    HIGHLY_RECOMMENDED,
    RECOMMENDED,
    CONSIDER,
)

from app.models.candidate_assessment import CandidateAssessment
from app.models.candidate_evaluation import CandidateEvaluation


class EvaluationCalculator:

    @staticmethod
    def calculate(
        assessment: CandidateAssessment,
    ) -> CandidateEvaluation:

        overall_score = round(

            assessment.technical_match_score * TECHNICAL_WEIGHT +

            assessment.experience_match_score * EXPERIENCE_WEIGHT +

            assessment.responsibility_match_score * RESPONSIBILITY_WEIGHT +

            assessment.education_match_score * EDUCATION_WEIGHT +

            assessment.soft_skill_match_score * SOFT_SKILL_WEIGHT

        )

        return CandidateEvaluation(

            assessment=assessment,

            overall_score=overall_score,

            recommendation=EvaluationCalculator.get_recommendation(
                overall_score
            )
        )

    @staticmethod
    def get_recommendation(score: int) -> str:

        if score >= HIGHLY_RECOMMENDED:
            return "Highly Recommended"

        if score >= RECOMMENDED:
            return "Recommended"

        if score >= CONSIDER:
            return "Consider"

        return "Not Recommended"