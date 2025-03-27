# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V0ListQuestionsParams"]


class V0ListQuestionsParams(TypedDict, total=False):
    limit: int
    """Number of results to return per page."""

    offset: int
    """The initial index from which to return the results."""
