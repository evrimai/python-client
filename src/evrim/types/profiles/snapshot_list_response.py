# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .create_profile_snapshot import CreateProfileSnapshot

__all__ = ["SnapshotListResponse"]


class SnapshotListResponse(BaseModel):
    count: int

    results: List[CreateProfileSnapshot]

    next: Optional[str] = None

    previous: Optional[str] = None
