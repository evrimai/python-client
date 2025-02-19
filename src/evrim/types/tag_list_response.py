# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .tag import Tag
from .._models import BaseModel

__all__ = ["TagListResponse"]


class TagListResponse(BaseModel):
    count: int

    results: List[Tag]

    next: Optional[str] = None

    previous: Optional[str] = None
