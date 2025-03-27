# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["RelationshipCreateResponse"]


class RelationshipCreateResponse(BaseModel):
    id: int

    extraction: object

    relationship: str

    source: str

    specification: str

    status: str

    target: str

    url: str
