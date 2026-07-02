from pydantic import BaseModel, Field

from app.models.skill_evidence import SkillEvidence


class CandidateAssessment(BaseModel):

    technical_match_score: int

    experience_match_score: int

    education_match_score: int

    responsibility_match_score: int

    soft_skill_match_score: int

    confidence_score: int

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