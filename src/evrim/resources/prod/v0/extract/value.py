# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.prod.v0.extract import value_list_params, value_create_params
from .....types.prod.v0.extract.value_list_response import ValueListResponse
from .....types.prod.v0.extract.value_create_response import ValueCreateResponse
from .....types.prod.v0.extract.value_retrieve_response import ValueRetrieveResponse

__all__ = ["ValueResource", "AsyncValueResource"]


class ValueResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return ValueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return ValueResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        name: str,
        source: str,
        specification: str,
        type: str,
        keyword_search: bool | NotGiven = NOT_GIVEN,
        raw_documents: bool | NotGiven = NOT_GIVEN,
        rerank: bool | NotGiven = NOT_GIVEN,
        urls: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prod/v0/extract/value/",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "source": source,
                    "specification": specification,
                    "type": type,
                    "keyword_search": keyword_search,
                    "raw_documents": raw_documents,
                    "rerank": rerank,
                    "urls": urls,
                },
                value_create_params.ValueCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValueCreateResponse,
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
    ) -> ValueRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/prod/v0/extract/value/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValueRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueListResponse:
        """
        Args:
          limit: Number of results to return per page.

          offset: The initial index from which to return the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/prod/v0/extract/value/",
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
                    value_list_params.ValueListParams,
                ),
            ),
            cast_to=ValueListResponse,
        )


class AsyncValueResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncValueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncValueResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        name: str,
        source: str,
        specification: str,
        type: str,
        keyword_search: bool | NotGiven = NOT_GIVEN,
        raw_documents: bool | NotGiven = NOT_GIVEN,
        rerank: bool | NotGiven = NOT_GIVEN,
        urls: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prod/v0/extract/value/",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "source": source,
                    "specification": specification,
                    "type": type,
                    "keyword_search": keyword_search,
                    "raw_documents": raw_documents,
                    "rerank": rerank,
                    "urls": urls,
                },
                value_create_params.ValueCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValueCreateResponse,
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
    ) -> ValueRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/prod/v0/extract/value/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValueRetrieveResponse,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueListResponse:
        """
        Args:
          limit: Number of results to return per page.

          offset: The initial index from which to return the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/prod/v0/extract/value/",
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
                    value_list_params.ValueListParams,
                ),
            ),
            cast_to=ValueListResponse,
        )


class ValueResourceWithRawResponse:
    def __init__(self, value: ValueResource) -> None:
        self._value = value

        self.create = to_raw_response_wrapper(
            value.create,
        )
        self.retrieve = to_raw_response_wrapper(
            value.retrieve,
        )
        self.list = to_raw_response_wrapper(
            value.list,
        )


class AsyncValueResourceWithRawResponse:
    def __init__(self, value: AsyncValueResource) -> None:
        self._value = value

        self.create = async_to_raw_response_wrapper(
            value.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            value.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            value.list,
        )


class ValueResourceWithStreamingResponse:
    def __init__(self, value: ValueResource) -> None:
        self._value = value

        self.create = to_streamed_response_wrapper(
            value.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            value.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            value.list,
        )


class AsyncValueResourceWithStreamingResponse:
    def __init__(self, value: AsyncValueResource) -> None:
        self._value = value

        self.create = async_to_streamed_response_wrapper(
            value.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            value.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            value.list,
        )
