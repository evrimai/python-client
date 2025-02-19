# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.snapshot import Snapshot

__all__ = ["SnapshotListResponse"]


class SnapshotListResponse(BaseModel):
    count: int

    results: List[Snapshot]

    next: Optional[str] = None

    previous: Optional[str] = None
