# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["RawListResponse", "Result"]


class Result(BaseModel):
    id: int

    error: str

    extraction: object

    query: str

    source: str

    status: str


class RawListResponse(BaseModel):
    count: int

    results: List[Result]

    next: Optional[str] = None

    previous: Optional[str] = None
