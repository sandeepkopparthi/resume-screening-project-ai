from pydantic import BaseModel, Field


class Project(BaseModel):
    """
    Represents one project extracted from a candidate's resume.
    """

    project_name: str | None = None

    description: str | None = None

    duration: str | None = None

    candidate_role: str | None = None

    technologies_used: list[str] = Field(default_factory=list)

    responsibilities: list[str] = Field(default_factory=list)