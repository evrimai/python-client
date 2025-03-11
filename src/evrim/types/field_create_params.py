# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["FieldCreateParams"]


class FieldCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    type: Required[str]

    id: int

    directed: bool

    enum_many: bool

    enum_values: List[str]

    keyword_search: bool

    raw_documents: bool

    rel_template_id: Optional[int]

    sources: Optional[List[str]]
