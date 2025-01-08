# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .bulk_job import BulkJob

__all__ = ["ProfileListResponse"]

ProfileListResponse: TypeAlias = List[BulkJob]
