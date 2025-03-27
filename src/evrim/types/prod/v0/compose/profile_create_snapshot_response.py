# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel
from ....shared.profile import Profile

__all__ = ["ProfileCreateSnapshotResponse"]


class ProfileCreateSnapshotResponse(BaseModel):
    profile: Profile
