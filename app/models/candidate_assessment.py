from pydantic import BaseModel, Field

from app.models.skill_evidence import SkillEvidence


class CandidateAssessment(BaseModel):

    technical_match_score: float

    experience_match_score: float

    education_match_score: float

    responsibility_match_score: float

    soft_skill_match_score: float

    confidence_score: float

    required_matching_skills: list[str] = Field(default_factory=list)

    required_missing_skills: list[str] = Field(default_factory=list)

    preferred_matching_skills: list[str] = Field(default_factory=list)

    preferred_missing_skills: list[str] = Field(default_factory=list)

    additional_skills: list[str] = Field(default_factory=list)

    matched_skill_evidence: list[SkillEvidence] = Field(default_factory=list)

    strengths: list[str] = Field(default_factory=list)

    weaknesses: list[str] = Field(default_factory=list)

    hiring_risks: list[str] = Field(default_factory=list)

    interview_focus_areas: list[str] = Field(default_factory=list)

    reasoning: str