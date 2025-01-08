# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..template import Template
from ..created_field import CreatedField

__all__ = ["BulkCreatedField", "CreateField"]


class CreateField(BaseModel):
    description: str

    name: str

    type: str

    rel_template: Optional[Template] = None


class BulkCreatedField(BaseModel):
    id: int

    created_fields: List[CreatedField]

    error: str

    status: str
