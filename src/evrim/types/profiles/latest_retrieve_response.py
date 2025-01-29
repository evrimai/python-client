# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..created_field import CreatedField

__all__ = ["LatestRetrieveResponse", "LatestRetrieveResponseItem", "LatestRetrieveResponseItemAnswer"]


class LatestRetrieveResponseItemAnswer(BaseModel):
    id: int

    answer: object


class LatestRetrieveResponseItem(BaseModel):
    answers: List[LatestRetrieveResponseItemAnswer]

    fields: List[CreatedField]

    specification: str


LatestRetrieveResponse: TypeAlias = List[LatestRetrieveResponseItem]
