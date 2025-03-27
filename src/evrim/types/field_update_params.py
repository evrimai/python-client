# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FieldUpdateParams"]


class FieldUpdateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    type: Required[str]

    body_id: Annotated[int, PropertyInfo(alias="id")]

    directed: bool

    enum_many: bool

    enum_values: List[str]

    keyword_search: bool

    raw_documents: bool

    rel_template_id: Optional[int]

    sources: Optional[List[str]]
