# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReportsV3CreateParams"]


class ReportsV3CreateParams(TypedDict, total=False):
    outline_id: Required[int]

    profile_id: Required[int]
