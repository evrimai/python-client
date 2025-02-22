# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .bulk_job import BulkJob
from ...._models import BaseModel

__all__ = ["ProfileListResponse"]


class ProfileListResponse(BaseModel):
    count: int

    results: List[BulkJob]

    next: Optional[str] = None

    previous: Optional[str] = None
