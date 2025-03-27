# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["V0ListQuestionsResponse", "Result"]


class Result(BaseModel):
    question: str


class V0ListQuestionsResponse(BaseModel):
    count: int

    results: List[Result]

    next: Optional[str] = None

    previous: Optional[str] = None
