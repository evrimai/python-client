# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options

__all__ = ["HealthResource", "AsyncHealthResource"]


class HealthResource(SyncAPIResource):
    @cached_property
    def profile(self) -> ProfileResource:
        return ProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> HealthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return HealthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return HealthResourceWithStreamingResponse(self)

    def retrieve_snapshot(
        self,
        snapshot_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get the health of a profile snapshot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/prod/v0/health/snapshot/{snapshot_id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncHealthResource(AsyncAPIResource):
    @cached_property
    def profile(self) -> AsyncProfileResource:
        return AsyncProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHealthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncHealthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncHealthResourceWithStreamingResponse(self)

    async def retrieve_snapshot(
        self,
        snapshot_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get the health of a profile snapshot

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/prod/v0/health/snapshot/{snapshot_id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class HealthResourceWithRawResponse:
    def __init__(self, health: HealthResource) -> None:
        self._health = health

        self.retrieve_snapshot = to_raw_response_wrapper(
            health.retrieve_snapshot,
        )

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        return ProfileResourceWithRawResponse(self._health.profile)


class AsyncHealthResourceWithRawResponse:
    def __init__(self, health: AsyncHealthResource) -> None:
        self._health = health

        self.retrieve_snapshot = async_to_raw_response_wrapper(
            health.retrieve_snapshot,
        )

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        return AsyncProfileResourceWithRawResponse(self._health.profile)


class HealthResourceWithStreamingResponse:
    def __init__(self, health: HealthResource) -> None:
        self._health = health

        self.retrieve_snapshot = to_streamed_response_wrapper(
            health.retrieve_snapshot,
        )

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        return ProfileResourceWithStreamingResponse(self._health.profile)


class AsyncHealthResourceWithStreamingResponse:
    def __init__(self, health: AsyncHealthResource) -> None:
        self._health = health

        self.retrieve_snapshot = async_to_streamed_response_wrapper(
            health.retrieve_snapshot,
        )

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        return AsyncProfileResourceWithStreamingResponse(self._health.profile)
