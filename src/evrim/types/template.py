# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .field import Field
from .._models import BaseModel

__all__ = ["Template"]


class Template(BaseModel):
    id: int

    fields: List[Field]

    name: str

    description: Optional[str] = None

    questions: Optional[List[str]] = None
