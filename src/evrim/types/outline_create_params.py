# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["OutlineCreateParams"]


class OutlineCreateParams(TypedDict, total=False):
    perspective: Required[str]

    profile_id: Required[int]

    report_title: Required[str]

    section_titles: Required[List[str]]

    outline: object
