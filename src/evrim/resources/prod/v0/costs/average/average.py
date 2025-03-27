# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .field import (
    FieldResource,
    AsyncFieldResource,
    FieldResourceWithRawResponse,
    AsyncFieldResourceWithRawResponse,
    FieldResourceWithStreamingResponse,
    AsyncFieldResourceWithStreamingResponse,
)
from ......_types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options

__all__ = ["AverageResource", "AsyncAverageResource"]


class AverageResource(SyncAPIResource):
    @cached_property
    def field(self) -> FieldResource:
        return FieldResource(self._client)

    @cached_property
    def with_raw_response(self) -> AverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AverageResourceWithStreamingResponse(self)

    def get_answer(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get avg answer cost for all answers"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/prod/v0/costs/average/answer/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAverageResource(AsyncAPIResource):
    @cached_property
    def field(self) -> AsyncFieldResource:
        return AsyncFieldResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncAverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncAverageResourceWithStreamingResponse(self)

    async def get_answer(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get avg answer cost for all answers"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/prod/v0/costs/average/answer/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AverageResourceWithRawResponse:
    def __init__(self, average: AverageResource) -> None:
        self._average = average

        self.get_answer = to_raw_response_wrapper(
            average.get_answer,
        )

    @cached_property
    def field(self) -> FieldResourceWithRawResponse:
        return FieldResourceWithRawResponse(self._average.field)


class AsyncAverageResourceWithRawResponse:
    def __init__(self, average: AsyncAverageResource) -> None:
        self._average = average

        self.get_answer = async_to_raw_response_wrapper(
            average.get_answer,
        )

    @cached_property
    def field(self) -> AsyncFieldResourceWithRawResponse:
        return AsyncFieldResourceWithRawResponse(self._average.field)


class AverageResourceWithStreamingResponse:
    def __init__(self, average: AverageResource) -> None:
        self._average = average

        self.get_answer = to_streamed_response_wrapper(
            average.get_answer,
        )

    @cached_property
    def field(self) -> FieldResourceWithStreamingResponse:
        return FieldResourceWithStreamingResponse(self._average.field)


class AsyncAverageResourceWithStreamingResponse:
    def __init__(self, average: AsyncAverageResource) -> None:
        self._average = average

        self.get_answer = async_to_streamed_response_wrapper(
            average.get_answer,
        )

    @cached_property
    def field(self) -> AsyncFieldResourceWithStreamingResponse:
        return AsyncFieldResourceWithStreamingResponse(self._average.field)
