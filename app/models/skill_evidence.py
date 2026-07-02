from pydantic import BaseModel


class SkillEvidence(BaseModel):
    skill: str
    evidence: str