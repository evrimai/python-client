# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .answer import (
    AnswerResource,
    AsyncAnswerResource,
    AnswerResourceWithRawResponse,
    AsyncAnswerResourceWithRawResponse,
    AnswerResourceWithStreamingResponse,
    AsyncAnswerResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .created_field import (
    CreatedFieldResource,
    AsyncCreatedFieldResource,
    CreatedFieldResourceWithRawResponse,
    AsyncCreatedFieldResourceWithRawResponse,
    CreatedFieldResourceWithStreamingResponse,
    AsyncCreatedFieldResourceWithStreamingResponse,
)
from .average.average import (
    AverageResource,
    AsyncAverageResource,
    AverageResourceWithRawResponse,
    AsyncAverageResourceWithRawResponse,
    AverageResourceWithStreamingResponse,
    AsyncAverageResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.prod.v0.cost_retrieve_snapshot_response import CostRetrieveSnapshotResponse

__all__ = ["CostsResource", "AsyncCostsResource"]


class CostsResource(SyncAPIResource):
    @cached_property
    def answer(self) -> AnswerResource:
        return AnswerResource(self._client)

    @cached_property
    def average(self) -> AverageResource:
        return AverageResource(self._client)

    @cached_property
    def created_field(self) -> CreatedFieldResource:
        return CreatedFieldResource(self._client)

    @cached_property
    def with_raw_response(self) -> CostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return CostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return CostsResourceWithStreamingResponse(self)

    def retrieve_snapshot(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CostRetrieveSnapshotResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/prod/v0/costs/snapshot/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CostRetrieveSnapshotResponse,
        )


class AsyncCostsResource(AsyncAPIResource):
    @cached_property
    def answer(self) -> AsyncAnswerResource:
        return AsyncAnswerResource(self._client)

    @cached_property
    def average(self) -> AsyncAverageResource:
        return AsyncAverageResource(self._client)

    @cached_property
    def created_field(self) -> AsyncCreatedFieldResource:
        return AsyncCreatedFieldResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncCostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncCostsResourceWithStreamingResponse(self)

    async def retrieve_snapshot(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CostRetrieveSnapshotResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/prod/v0/costs/snapshot/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CostRetrieveSnapshotResponse,
        )


class CostsResourceWithRawResponse:
    def __init__(self, costs: CostsResource) -> None:
        self._costs = costs

        self.retrieve_snapshot = to_raw_response_wrapper(
            costs.retrieve_snapshot,
        )

    @cached_property
    def answer(self) -> AnswerResourceWithRawResponse:
        return AnswerResourceWithRawResponse(self._costs.answer)

    @cached_property
    def average(self) -> AverageResourceWithRawResponse:
        return AverageResourceWithRawResponse(self._costs.average)

    @cached_property
    def created_field(self) -> CreatedFieldResourceWithRawResponse:
        return CreatedFieldResourceWithRawResponse(self._costs.created_field)


class AsyncCostsResourceWithRawResponse:
    def __init__(self, costs: AsyncCostsResource) -> None:
        self._costs = costs

        self.retrieve_snapshot = async_to_raw_response_wrapper(
            costs.retrieve_snapshot,
        )

    @cached_property
    def answer(self) -> AsyncAnswerResourceWithRawResponse:
        return AsyncAnswerResourceWithRawResponse(self._costs.answer)

    @cached_property
    def average(self) -> AsyncAverageResourceWithRawResponse:
        return AsyncAverageResourceWithRawResponse(self._costs.average)

    @cached_property
    def created_field(self) -> AsyncCreatedFieldResourceWithRawResponse:
        return AsyncCreatedFieldResourceWithRawResponse(self._costs.created_field)


class CostsResourceWithStreamingResponse:
    def __init__(self, costs: CostsResource) -> None:
        self._costs = costs

        self.retrieve_snapshot = to_streamed_response_wrapper(
            costs.retrieve_snapshot,
        )

    @cached_property
    def answer(self) -> AnswerResourceWithStreamingResponse:
        return AnswerResourceWithStreamingResponse(self._costs.answer)

    @cached_property
    def average(self) -> AverageResourceWithStreamingResponse:
        return AverageResourceWithStreamingResponse(self._costs.average)

    @cached_property
    def created_field(self) -> CreatedFieldResourceWithStreamingResponse:
        return CreatedFieldResourceWithStreamingResponse(self._costs.created_field)


class AsyncCostsResourceWithStreamingResponse:
    def __init__(self, costs: AsyncCostsResource) -> None:
        self._costs = costs

        self.retrieve_snapshot = async_to_streamed_response_wrapper(
            costs.retrieve_snapshot,
        )

    @cached_property
    def answer(self) -> AsyncAnswerResourceWithStreamingResponse:
        return AsyncAnswerResourceWithStreamingResponse(self._costs.answer)

    @cached_property
    def average(self) -> AsyncAverageResourceWithStreamingResponse:
        return AsyncAverageResourceWithStreamingResponse(self._costs.average)

    @cached_property
    def created_field(self) -> AsyncCreatedFieldResourceWithStreamingResponse:
        return AsyncCreatedFieldResourceWithStreamingResponse(self._costs.created_field)
