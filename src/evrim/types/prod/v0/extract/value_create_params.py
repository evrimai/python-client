# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ValueCreateParams"]


class ValueCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    source: Required[str]

    specification: Required[str]

    type: Required[str]

    keyword_search: bool

    raw_documents: bool

    rerank: bool

    urls: Optional[List[str]]
