from pydantic import BaseModel, Field

from app.models.education import Education
from app.models.projects import Project
from app.models.work_experience import WorkExperience


class Resume(BaseModel):
    """
    Represents a structured resume extracted from an unstructured document.
    """

    candidate_name: str | None = None

    summary: str | None = None

    current_job_role: str | None = None

    total_years_experience: int | None = None

    technical_skills: list[str] = Field(default_factory=list)

    soft_skills: list[str] = Field(default_factory=list)

    education: list[Education] = Field(default_factory=list)

    certifications: list[str] = Field(default_factory=list)

    projects: list[Project] = Field(default_factory=list)

    work_experience: list[WorkExperience] = Field(default_factory=list)

    achievements: list[str] = Field(default_factory=list)