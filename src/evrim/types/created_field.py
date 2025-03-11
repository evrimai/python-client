# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .field import Field
from .._models import BaseModel

__all__ = ["CreatedField"]


class CreatedField(BaseModel):
    id: int

    field: Field

    status: str

    value: object

    keyword_search: Optional[bool] = None

    raw_documents: Optional[bool] = None
