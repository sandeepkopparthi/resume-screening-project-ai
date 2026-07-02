from pydantic import BaseModel, Field

from app.models.interview_question import InterviewQuestion


class InterviewPlan(BaseModel):
    overall_strategy: str

    interviewer_notes: str

    questions: list[InterviewQuestion] = Field(default_factory=list)