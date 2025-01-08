# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import reports_v3_create_params, reports_v3_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.report import Report
from ..types.reports_v3_list_response import ReportsV3ListResponse

__all__ = ["ReportsV3Resource", "AsyncReportsV3Resource"]


class ReportsV3Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportsV3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return ReportsV3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsV3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return ReportsV3ResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        outline_id: int,
        profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Report:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prod/v0/reports-v3/",
            body=maybe_transform(
                {
                    "outline_id": outline_id,
                    "profile_id": profile_id,
                },
                reports_v3_create_params.ReportsV3CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Report:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/prod/v0/reports-v3/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    def update(
        self,
        id: int,
        *,
        outline_id: int | NotGiven = NOT_GIVEN,
        profile_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Report:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/prod/v0/reports-v3/{id}/",
            body=maybe_transform(
                {
                    "outline_id": outline_id,
                    "profile_id": profile_id,
                },
                reports_v3_update_params.ReportsV3UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReportsV3ListResponse:
        return self._get(
            "/prod/v0/reports-v3/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportsV3ListResponse,
        )

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/prod/v0/reports-v3/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncReportsV3Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportsV3ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsV3ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsV3ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncReportsV3ResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        outline_id: int,
        profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Report:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prod/v0/reports-v3/",
            body=await async_maybe_transform(
                {
                    "outline_id": outline_id,
                    "profile_id": profile_id,
                },
                reports_v3_create_params.ReportsV3CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Report:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/prod/v0/reports-v3/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    async def update(
        self,
        id: int,
        *,
        outline_id: int | NotGiven = NOT_GIVEN,
        profile_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Report:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/prod/v0/reports-v3/{id}/",
            body=await async_maybe_transform(
                {
                    "outline_id": outline_id,
                    "profile_id": profile_id,
                },
                reports_v3_update_params.ReportsV3UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Report,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReportsV3ListResponse:
        return await self._get(
            "/prod/v0/reports-v3/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReportsV3ListResponse,
        )

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/prod/v0/reports-v3/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ReportsV3ResourceWithRawResponse:
    def __init__(self, reports_v3: ReportsV3Resource) -> None:
        self._reports_v3 = reports_v3

        self.create = to_raw_response_wrapper(
            reports_v3.create,
        )
        self.retrieve = to_raw_response_wrapper(
            reports_v3.retrieve,
        )
        self.update = to_raw_response_wrapper(
            reports_v3.update,
        )
        self.list = to_raw_response_wrapper(
            reports_v3.list,
        )
        self.delete = to_raw_response_wrapper(
            reports_v3.delete,
        )


class AsyncReportsV3ResourceWithRawResponse:
    def __init__(self, reports_v3: AsyncReportsV3Resource) -> None:
        self._reports_v3 = reports_v3

        self.create = async_to_raw_response_wrapper(
            reports_v3.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            reports_v3.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            reports_v3.update,
        )
        self.list = async_to_raw_response_wrapper(
            reports_v3.list,
        )
        self.delete = async_to_raw_response_wrapper(
            reports_v3.delete,
        )


class ReportsV3ResourceWithStreamingResponse:
    def __init__(self, reports_v3: ReportsV3Resource) -> None:
        self._reports_v3 = reports_v3

        self.create = to_streamed_response_wrapper(
            reports_v3.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            reports_v3.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            reports_v3.update,
        )
        self.list = to_streamed_response_wrapper(
            reports_v3.list,
        )
        self.delete = to_streamed_response_wrapper(
            reports_v3.delete,
        )


class AsyncReportsV3ResourceWithStreamingResponse:
    def __init__(self, reports_v3: AsyncReportsV3Resource) -> None:
        self._reports_v3 = reports_v3

        self.create = async_to_streamed_response_wrapper(
            reports_v3.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            reports_v3.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            reports_v3.update,
        )
        self.list = async_to_streamed_response_wrapper(
            reports_v3.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            reports_v3.delete,
        )
