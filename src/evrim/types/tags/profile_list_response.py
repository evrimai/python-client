# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.profile import Profile

__all__ = ["ProfileListResponse"]


class ProfileListResponse(BaseModel):
    count: int

    results: List[Profile]

    next: Optional[str] = None

    previous: Optional[str] = None
