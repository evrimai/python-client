# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["RawCreateResponse"]


class RawCreateResponse(BaseModel):
    id: int

    error: str

    extraction: object

    query: str

    source: str

    status: str
