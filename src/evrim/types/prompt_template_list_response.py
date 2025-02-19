# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .prompt_template import PromptTemplate

__all__ = ["PromptTemplateListResponse"]


class PromptTemplateListResponse(BaseModel):
    count: int

    results: List[PromptTemplate]

    next: Optional[str] = None

    previous: Optional[str] = None
