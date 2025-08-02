# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    limit: int
    """Number of results to return per page."""

    name: str

    offset: int
    """The initial index from which to return the results."""

    ordering: str
    """Which field to use when ordering the results."""

    search: str
    """A search term."""
