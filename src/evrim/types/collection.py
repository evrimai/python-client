# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.profile import Profile

__all__ = ["Collection"]


class Collection(BaseModel):
    id: int

    collection: List[Profile]

    description: str

    name: str
