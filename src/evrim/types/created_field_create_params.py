# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .template_param import TemplateParam

__all__ = ["CreatedFieldCreateParams"]


class CreatedFieldCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    specification: Required[str]

    type: Required[str]

    enum_many: bool

    enum_values: List[str]

    rel_template: TemplateParam

    source_entity_type: Optional[str]

    sources: Optional[List[str]]
