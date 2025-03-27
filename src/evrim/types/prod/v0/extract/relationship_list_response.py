# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["RelationshipListResponse", "Result"]


class Result(BaseModel):
    id: int

    extraction: object

    relationship: str

    source: str

    specification: str

    status: str

    target: str

    url: str


class RelationshipListResponse(BaseModel):
    count: int

    results: List[Result]

    next: Optional[str] = None

    previous: Optional[str] = None
