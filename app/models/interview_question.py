from enum import Enum

from pydantic import BaseModel, Field


class QuestionCategory(str, Enum):
    TECHNICAL_CORE = "technical_core"
    TECHNICAL_MISSING = "technical_missing"
    TECHNICAL_EXPERIENCE = "technical_experience"
    TECHNICAL_ARCHITECTURE = "technical_architecture"
    TECHNICAL_SCENARIO = "technical_scenario"
    BEHAVIORAL = "behavioral"


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class InterviewQuestion(BaseModel):
    category: QuestionCategory

    difficulty: Difficulty

    skill: str

    question: str

    purpose: str

    expected_signals: list[str] = Field(default_factory=list)
    
    follow_up_questions: list[str] = Field(default_factory=list)