# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RelationshipCreateParams"]


class RelationshipCreateParams(TypedDict, total=False):
    relationship: Required[str]

    source: Required[str]

    specification: Required[str]

    target: Required[str]

    url: Required[str]
