# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FieldListParams"]


class FieldListParams(TypedDict, total=False):
    limit: int
    """Number of results to return per page."""

    name: str

    offset: int
    """The initial index from which to return the results."""

    type: Literal["bln", "enm", "flt", "int", "rel", "str"]
    """
    - `str` - String
    - `int` - Integer
    - `flt` - Float
    - `bln` - Boolean
    - `rel` - Relationship
    - `enm` - Enum
    """
