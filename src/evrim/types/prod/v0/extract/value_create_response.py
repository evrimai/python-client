# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["ValueCreateResponse"]


class ValueCreateResponse(BaseModel):
    id: int

    description: str

    extraction: object

    name: str

    source: str

    specification: str

    status: str

    type: str

    keyword_search: Optional[bool] = None

    raw_documents: Optional[bool] = None

    rerank: Optional[bool] = None

    urls: Optional[List[str]] = None
