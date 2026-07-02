from pydantic import BaseModel, Field


class JobDescription(BaseModel):
    job_title: str | None = None

    company_name: str | None = None

    location: str | None = None

    employment_type: str | None = None

    experience_required: str | None = None

    education_required: str | None = None

    required_technical_skills: list[str] = Field(default_factory=list)

    preferred_skills: list[str] = Field(default_factory=list)

    responsibilities: list[str] = Field(default_factory=list)

    required_certifications: list[str] = Field(default_factory=list)

    tools_and_frameworks: list[str] = Field(default_factory=list)

    soft_skills: list[str] = Field(default_factory=list)

    domain: str | None = None

    summary: str | None = None