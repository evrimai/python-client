# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..created_field import CreatedField
from ..shared.report import Report

__all__ = ["CreateProfileSnapshot", "Answer"]


class Answer(BaseModel):
    id: int

    answer: object

    question: str

    source: Optional[str] = None


class CreateProfileSnapshot(BaseModel):
    id: int

    answers: List[Answer]

    fields: List[CreatedField]

    reports: List[Report]
