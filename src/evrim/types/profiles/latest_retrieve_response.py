# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..created_field import CreatedField

__all__ = ["LatestRetrieveResponse", "Result", "ResultAnswer"]


class ResultAnswer(BaseModel):
    id: int

    answer: object

    question: str

    source: Optional[str] = None


class Result(BaseModel):
    answers: List[ResultAnswer]

    fields: List[CreatedField]

    specification: str


class LatestRetrieveResponse(BaseModel):
    count: int

    results: List[Result]

    next: Optional[str] = None

    previous: Optional[str] = None
