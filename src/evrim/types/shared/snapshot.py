# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .report import Report
from ..._models import BaseModel
from ..created_field import CreatedField

__all__ = ["Snapshot", "Answer"]


class Answer(BaseModel):
    id: int

    answer: object


class Snapshot(BaseModel):
    id: int

    answers: List[Answer]

    fields: List[CreatedField]

    reports: List[Report]

    status: str
