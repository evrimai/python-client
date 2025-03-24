# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .report import Report
from ..._models import BaseModel
from ..created_field import CreatedField

__all__ = ["Snapshot", "Answer"]


class Answer(BaseModel):
    id: int

    answer: object

    question: str

    source: Optional[str] = None


class Snapshot(BaseModel):
    id: int

    answers: List[Answer]

    fields: List[CreatedField]

    reports: List[Report]

    status: str
