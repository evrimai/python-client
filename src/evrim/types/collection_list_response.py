# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .collection import Collection

__all__ = ["CollectionListResponse"]


class CollectionListResponse(BaseModel):
    count: int

    results: List[Collection]

    next: Optional[str] = None

    previous: Optional[str] = None
