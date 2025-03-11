# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from .template_param import TemplateParam

__all__ = ["CreatedFieldUpdateParams"]


class CreatedFieldUpdateParams(TypedDict, total=False):
    description: str

    directed_source: Optional[str]

    enum_many: bool

    enum_values: List[str]

    keyword_search: Optional[bool]

    name: str

    raw_documents: Optional[bool]

    rel_template: TemplateParam

    source_entity_type: Optional[str]

    sources: Optional[List[str]]

    specification: str

    type: str
