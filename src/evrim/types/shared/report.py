# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..outline import Outline
from ..._models import BaseModel

__all__ = ["Report"]


class Report(BaseModel):
    id: int

    outline: Outline

    report: object
