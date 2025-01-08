# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..shared.snapshot import Snapshot

__all__ = ["LatestRetrieveResponse"]

LatestRetrieveResponse: TypeAlias = List[Snapshot]
