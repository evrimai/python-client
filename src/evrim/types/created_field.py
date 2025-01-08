# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .field import Field
from .._models import BaseModel

__all__ = ["CreatedField"]


class CreatedField(BaseModel):
    id: int

    field: Field

    value: object
