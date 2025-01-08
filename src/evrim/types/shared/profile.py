# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..tag import Tag
from .snapshot import Snapshot
from ..._models import BaseModel
from ..template import Template

__all__ = ["Profile"]


class Profile(BaseModel):
    id: int

    snapshots: List[Snapshot]

    specification: str

    template: Template

    tags: Optional[List[Tag]] = None
