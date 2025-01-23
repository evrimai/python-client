# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from .template_param import TemplateParam

__all__ = ["CreatedFieldUpdateParams"]


class CreatedFieldUpdateParams(TypedDict, total=False):
    description: str

    enum_many: bool

    enum_values: List[str]

    name: str

    rel_template: TemplateParam

    source_entity_type: Optional[str]

    specification: str

    type: str
