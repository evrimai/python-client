# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..template_param import TemplateParam

__all__ = ["CreatedFieldCreateParams", "CreateField"]


class CreatedFieldCreateParams(TypedDict, total=False):
    create_fields: Required[Iterable[CreateField]]

    specification: Required[str]


class CreateField(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    type: Required[str]

    rel_template: TemplateParam
