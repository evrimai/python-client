# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .template import Template

__all__ = ["PromptTemplate"]


class PromptTemplate(BaseModel):
    id: int

    prompt: str

    template: Template

    status: Optional[Literal["W", "P", "C", "F"]] = None
    """
    - `W` - WAITING
    - `P` - PROCESSING
    - `C` - COMPLETED
    - `F` - FAILED
    """
