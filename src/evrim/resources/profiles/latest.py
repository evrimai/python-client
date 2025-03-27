# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.profiles import latest_retrieve_params
from ...types.profiles.latest_retrieve_response import LatestRetrieveResponse

__all__ = ["LatestResource", "AsyncLatestResource"]


class LatestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LatestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return LatestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LatestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return LatestResourceWithStreamingResponse(self)

    def retrieve(
        self,
        profile_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LatestRetrieveResponse:
        """
        Get the latest snapshot for a profile based on the profile id and created date

        Args:
          limit: Number of results to return per page.

          offset: The initial index from which to return the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._get(
            f"/prod/v0/profiles/{profile_id}/latest/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    latest_retrieve_params.LatestRetrieveParams,
                ),
            ),
            cast_to=LatestRetrieveResponse,
        )

    def retrieve_relationships(
        self,
        profile_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get relationships for a snapshot as records for easy usage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/prod/v0/profiles/{profile_id}/latest/relationships/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLatestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLatestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncLatestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLatestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncLatestResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        profile_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LatestRetrieveResponse:
        """
        Get the latest snapshot for a profile based on the profile id and created date

        Args:
          limit: Number of results to return per page.

          offset: The initial index from which to return the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._get(
            f"/prod/v0/profiles/{profile_id}/latest/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    latest_retrieve_params.LatestRetrieveParams,
                ),
            ),
            cast_to=LatestRetrieveResponse,
        )

    async def retrieve_relationships(
        self,
        profile_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get relationships for a snapshot as records for easy usage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/prod/v0/profiles/{profile_id}/latest/relationships/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LatestResourceWithRawResponse:
    def __init__(self, latest: LatestResource) -> None:
        self._latest = latest

        self.retrieve = to_raw_response_wrapper(
            latest.retrieve,
        )
        self.retrieve_relationships = to_raw_response_wrapper(
            latest.retrieve_relationships,
        )


class AsyncLatestResourceWithRawResponse:
    def __init__(self, latest: AsyncLatestResource) -> None:
        self._latest = latest

        self.retrieve = async_to_raw_response_wrapper(
            latest.retrieve,
        )
        self.retrieve_relationships = async_to_raw_response_wrapper(
            latest.retrieve_relationships,
        )


class LatestResourceWithStreamingResponse:
    def __init__(self, latest: LatestResource) -> None:
        self._latest = latest

        self.retrieve = to_streamed_response_wrapper(
            latest.retrieve,
        )
        self.retrieve_relationships = to_streamed_response_wrapper(
            latest.retrieve_relationships,
        )


class AsyncLatestResourceWithStreamingResponse:
    def __init__(self, latest: AsyncLatestResource) -> None:
        self._latest = latest

        self.retrieve = async_to_streamed_response_wrapper(
            latest.retrieve,
        )
        self.retrieve_relationships = async_to_streamed_response_wrapper(
            latest.retrieve_relationships,
        )
