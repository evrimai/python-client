# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Field"]


class Field(BaseModel):
    description: str

    name: str

    rel_template: Optional[int] = None

    type: str

    id: Optional[int] = None

    directed: Optional[bool] = None

    enum_many: Optional[bool] = None

    enum_values: Optional[List[str]] = None

    keyword_search: Optional[bool] = None

    raw_documents: Optional[bool] = None

    sources: Optional[List[str]] = None
