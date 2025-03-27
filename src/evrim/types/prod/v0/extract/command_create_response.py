# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["CommandCreateResponse"]


class CommandCreateResponse(BaseModel):
    id: int

    error: str

    extraction: object

    query: str

    status: str
