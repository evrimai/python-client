# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..created_field import CreatedField
from ..shared.report import Report

__all__ = ["CreateProfileSnapshot", "Answer"]


class Answer(BaseModel):
    id: int

    answer: object


class CreateProfileSnapshot(BaseModel):
    id: int

    answers: List[Answer]

    fields: List[CreatedField]

    reports: List[Report]
