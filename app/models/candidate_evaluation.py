from pydantic import BaseModel

from app.models.candidate_assessment import CandidateAssessment


class CandidateEvaluation(BaseModel):

    assessment: CandidateAssessment

    overall_score: int

    recommendation: str