# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ...template import Template
from ...shared.profile import Profile

__all__ = ["BulkJob"]


class BulkJob(BaseModel):
    id: int

    error: str

    profiles: List[Profile]

    status: str

    template: Template
