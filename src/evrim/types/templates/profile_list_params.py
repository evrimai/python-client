# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProfileListParams"]


class ProfileListParams(TypedDict, total=False):
    include_answers: bool
    """Include answers in the response"""

    include_fields: bool
    """Include fields in the response"""

    include_snapshots: bool
    """Include snapshots in the response"""

    to_records: bool
    """Transform the snapshot fields into a list of records"""
