# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PromptTemplateCreateParams"]


class PromptTemplateCreateParams(TypedDict, total=False):
    prompt: Required[str]

    status: Literal["W", "P", "C", "F"]
    """
    - `W` - WAITING
    - `P` - PROCESSING
    - `C` - COMPLETED
    - `F` - FAILED
    """
