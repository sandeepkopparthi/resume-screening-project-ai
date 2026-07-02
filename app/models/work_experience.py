from pydantic import BaseModel, Field


class WorkExperience(BaseModel):
    """
    Represents one work experience entry extracted from a resume.
    """

    company: str | None = None

    role: str | None = None

    duration: str | None = None

    responsibilities: list[str] = Field(default_factory=list)