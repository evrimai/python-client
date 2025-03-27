# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["AnswerRetrieveResponse"]


class AnswerRetrieveResponse(BaseModel):
    id: int

    answer: object

    status: str

    question: Optional[str] = None
