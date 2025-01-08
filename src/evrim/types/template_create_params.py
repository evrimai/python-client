# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .field_param import FieldParam

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    fields: Required[Iterable[FieldParam]]

    name: Required[str]

    description: Optional[str]

    questions: List[str]
