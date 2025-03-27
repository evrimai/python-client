# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["CostRetrieveSnapshotResponse"]


class CostRetrieveSnapshotResponse(BaseModel):
    answer_costs: float

    field_costs: float

    total_cost: float
