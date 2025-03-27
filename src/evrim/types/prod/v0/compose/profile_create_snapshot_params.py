# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ProfileCreateSnapshotParams"]


class ProfileCreateSnapshotParams(TypedDict, total=False):
    answer_ids: Required[Iterable[int]]

    created_field_ids: Required[Iterable[int]]

    specification: Required[str]

    template_id: Required[int]
