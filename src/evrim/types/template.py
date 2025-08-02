# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .field import Field
from .._models import BaseModel

__all__ = ["Template"]


class Template(BaseModel):
    id: int

    created_at: datetime

    fields: List[Field]

    name: str

    updated_at: datetime

    description: Optional[str] = None

    questions: Optional[List[str]] = None

    tags: Optional[List[str]] = None
