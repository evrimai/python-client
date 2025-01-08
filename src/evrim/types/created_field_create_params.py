# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CreatedFieldCreateParams"]


class CreatedFieldCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    specification: Required[str]

    type: Required[str]
