# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .field import Field
from .._models import BaseModel

__all__ = ["FieldListResponse"]


class FieldListResponse(BaseModel):
    count: int

    results: List[Field]

    next: Optional[str] = None

    previous: Optional[str] = None
