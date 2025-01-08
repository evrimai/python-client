# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .tag_param import TagParam

__all__ = ["ProfileCreateParams"]


class ProfileCreateParams(TypedDict, total=False):
    specification: Required[str]

    template_id: Required[int]

    tags: Iterable[TagParam]
