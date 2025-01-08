# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ProfileCreateParams"]


class ProfileCreateParams(TypedDict, total=False):
    collection_id: Required[int]

    profile_ids: Required[Iterable[int]]
