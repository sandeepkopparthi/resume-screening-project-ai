from pydantic import BaseModel
from typing import Optional


class Education(BaseModel):
    degree: str | None = None
    institution: str | None = None
    graduation_year: str | None = None