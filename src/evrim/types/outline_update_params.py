# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["OutlineUpdateParams"]


class OutlineUpdateParams(TypedDict, total=False):
    outline: object

    perspective: str

    profile_id: int

    report_title: str

    section_titles: List[str]
