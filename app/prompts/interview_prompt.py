from app.models.resume import Resume
from app.models.job_description import JobDescription
from app.models.candidate_assessment import CandidateAssessment


class InterviewPromptBuilder:

    @staticmethod
    def build(
        resume: Resume,
        job: JobDescription,
        assessment: CandidateAssessment,
    ) -> str:
        ""