# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ProfileCreateParams"]


class ProfileCreateParams(TypedDict, total=False):
    specifications: Required[List[str]]

    template_id: Required[int]
