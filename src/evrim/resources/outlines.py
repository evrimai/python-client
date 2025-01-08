# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import outline_create_params, outline_update_params
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
from ..types.outline import Outline
from ..types.outline_list_response import OutlineListResponse

__all__ = ["OutlinesResource", "AsyncOutlinesResource"]


class OutlinesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OutlinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return OutlinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutlinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return OutlinesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        perspective: str,
        profile_id: int,
        report_title: str,
        section_titles: List[str],
        outline: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Outline:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prod/v0/outlines/",
            body=maybe_transform(
                {
                    "perspective": perspective,
                    "profile_id": profile_id,
                    "report_title": report_title,
                    "section_titles": section_titles,
                    "outline": outline,
                },
                outline_create_params.OutlineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Outline,
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
    ) -> Outline:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/prod/v0/outlines/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Outline,
        )

    def update(
        self,
        id: int,
        *,
        outline: object | NotGiven = NOT_GIVEN,
        perspective: str | NotGiven = NOT_GIVEN,
        profile_id: int | NotGiven = NOT_GIVEN,
        report_title: str | NotGiven = NOT_GIVEN,
        section_titles: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Outline:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/prod/v0/outlines/{id}/",
            body=maybe_transform(
                {
                    "outline": outline,
                    "perspective": perspective,
                    "profile_id": profile_id,
                    "report_title": report_title,
                    "section_titles": section_titles,
                },
                outline_update_params.OutlineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Outline,
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
    ) -> OutlineListResponse:
        return self._get(
            "/prod/v0/outlines/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutlineListResponse,
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
            f"/prod/v0/outlines/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOutlinesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOutlinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncOutlinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutlinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncOutlinesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        perspective: str,
        profile_id: int,
        report_title: str,
        section_titles: List[str],
        outline: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Outline:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prod/v0/outlines/",
            body=await async_maybe_transform(
                {
                    "perspective": perspective,
                    "profile_id": profile_id,
                    "report_title": report_title,
                    "section_titles": section_titles,
                    "outline": outline,
                },
                outline_create_params.OutlineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Outline,
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
    ) -> Outline:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/prod/v0/outlines/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Outline,
        )

    async def update(
        self,
        id: int,
        *,
        outline: object | NotGiven = NOT_GIVEN,
        perspective: str | NotGiven = NOT_GIVEN,
        profile_id: int | NotGiven = NOT_GIVEN,
        report_title: str | NotGiven = NOT_GIVEN,
        section_titles: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Outline:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/prod/v0/outlines/{id}/",
            body=await async_maybe_transform(
                {
                    "outline": outline,
                    "perspective": perspective,
                    "profile_id": profile_id,
                    "report_title": report_title,
                    "section_titles": section_titles,
                },
                outline_update_params.OutlineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Outline,
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
    ) -> OutlineListResponse:
        return await self._get(
            "/prod/v0/outlines/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutlineListResponse,
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
            f"/prod/v0/outlines/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OutlinesResourceWithRawResponse:
    def __init__(self, outlines: OutlinesResource) -> None:
        self._outlines = outlines

        self.create = to_raw_response_wrapper(
            outlines.create,
        )
        self.retrieve = to_raw_response_wrapper(
            outlines.retrieve,
        )
        self.update = to_raw_response_wrapper(
            outlines.update,
        )
        self.list = to_raw_response_wrapper(
            outlines.list,
        )
        self.delete = to_raw_response_wrapper(
            outlines.delete,
        )


class AsyncOutlinesResourceWithRawResponse:
    def __init__(self, outlines: AsyncOutlinesResource) -> None:
        self._outlines = outlines

        self.create = async_to_raw_response_wrapper(
            outlines.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            outlines.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            outlines.update,
        )
        self.list = async_to_raw_response_wrapper(
            outlines.list,
        )
        self.delete = async_to_raw_response_wrapper(
            outlines.delete,
        )


class OutlinesResourceWithStreamingResponse:
    def __init__(self, outlines: OutlinesResource) -> None:
        self._outlines = outlines

        self.create = to_streamed_response_wrapper(
            outlines.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            outlines.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            outlines.update,
        )
        self.list = to_streamed_response_wrapper(
            outlines.list,
        )
        self.delete = to_streamed_response_wrapper(
            outlines.delete,
        )


class AsyncOutlinesResourceWithStreamingResponse:
    def __init__(self, outlines: AsyncOutlinesResource) -> None:
        self._outlines = outlines

        self.create = async_to_streamed_response_wrapper(
            outlines.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            outlines.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            outlines.update,
        )
        self.list = async_to_streamed_response_wrapper(
            outlines.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            outlines.delete,
        )
