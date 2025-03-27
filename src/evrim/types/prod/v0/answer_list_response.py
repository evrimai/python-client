# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AnswerListResponse", "Result"]


class Result(BaseModel):
    id: int

    answer: object

    status: str

    question: Optional[str] = None


class AnswerListResponse(BaseModel):
    count: int

    results: List[Result]

    next: Optional[str] = None

    previous: Optional[str] = None
