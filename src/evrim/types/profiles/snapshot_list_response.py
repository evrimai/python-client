# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .create_profile_snapshot import CreateProfileSnapshot

__all__ = ["SnapshotListResponse"]

SnapshotListResponse: TypeAlias = List[CreateProfileSnapshot]
