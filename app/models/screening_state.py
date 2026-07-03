from pydantic import BaseModel

from app.models.resume import Resume
from app.models.job_description import JobDescription
from app.models.candidate_assessment import CandidateAssessment
from app.models.candidate_evaluation import CandidateEvaluation
from app.models.interview_plan import InterviewPlan


class ScreeningState(BaseModel):
    # file paths
    resume_file_path: str | None = None
    jd_file_path: str | None = None
    
    # Raw Inputs
    resume_text: str | None = None
    jd_text: str | None = None

    # Parsed Objects
    resume: Resume | None = None
    job_description: JobDescription | None = None

    # AI Outputs
    candidate_assessment: CandidateAssessment | None = None
    candidate_evaluation: CandidateEvaluation | None = None
    interview_plan: InterviewPlan | None = None