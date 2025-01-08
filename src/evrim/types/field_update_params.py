# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FieldUpdateParams"]


class FieldUpdateParams(TypedDict, total=False):
    path_id: Required[Annotated[int, PropertyInfo(alias="id")]]

    body_id: Annotated[int, PropertyInfo(alias="id")]

    description: str

    enum_many: bool

    enum_values: List[str]

    name: str

    rel_template: Optional[int]

    rel_template_id: Optional[int]

    type: str
