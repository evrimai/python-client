# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AnswerCreateParams"]


class AnswerCreateParams(TypedDict, total=False):
    specification: Required[str]

    question: Optional[str]
