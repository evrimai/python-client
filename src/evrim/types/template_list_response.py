# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .template import Template

__all__ = ["TemplateListResponse"]


class TemplateListResponse(BaseModel):
    count: int

    results: List[Template]

    next: Optional[str] = None

    previous: Optional[str] = None
