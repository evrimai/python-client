# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["CreatedFieldListResponse", "Result"]


class Result(BaseModel):
    id: int

    total: float


class CreatedFieldListResponse(BaseModel):
    count: int

    results: List[Result]

    next: Optional[str] = None

    previous: Optional[str] = None
