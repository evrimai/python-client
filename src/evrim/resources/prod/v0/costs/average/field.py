# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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

__all__ = ["FieldResource", "AsyncFieldResource"]


class FieldResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FieldResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return FieldResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FieldResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return FieldResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get avg field cost for all fields"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/prod/v0/costs/average/field/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_by_type(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get avg field cost for all fields by field type"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/prod/v0/costs/average/field/type/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFieldResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFieldResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncFieldResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFieldResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncFieldResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get avg field cost for all fields"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/prod/v0/costs/average/field/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_by_type(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get avg field cost for all fields by field type"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/prod/v0/costs/average/field/type/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FieldResourceWithRawResponse:
    def __init__(self, field: FieldResource) -> None:
        self._field = field

        self.list = to_raw_response_wrapper(
            field.list,
        )
        self.get_by_type = to_raw_response_wrapper(
            field.get_by_type,
        )


class AsyncFieldResourceWithRawResponse:
    def __init__(self, field: AsyncFieldResource) -> None:
        self._field = field

        self.list = async_to_raw_response_wrapper(
            field.list,
        )
        self.get_by_type = async_to_raw_response_wrapper(
            field.get_by_type,
        )


class FieldResourceWithStreamingResponse:
    def __init__(self, field: FieldResource) -> None:
        self._field = field

        self.list = to_streamed_response_wrapper(
            field.list,
        )
        self.get_by_type = to_streamed_response_wrapper(
            field.get_by_type,
        )


class AsyncFieldResourceWithStreamingResponse:
    def __init__(self, field: AsyncFieldResource) -> None:
        self._field = field

        self.list = async_to_streamed_response_wrapper(
            field.list,
        )
        self.get_by_type = async_to_streamed_response_wrapper(
            field.get_by_type,
        )
