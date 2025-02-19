# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .created_field import CreatedField

__all__ = ["CreatedFieldListResponse"]


class CreatedFieldListResponse(BaseModel):
    count: int

    results: List[CreatedField]

    next: Optional[str] = None

    previous: Optional[str] = None
