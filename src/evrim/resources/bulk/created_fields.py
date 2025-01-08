# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.bulk import created_field_create_params
from ..._base_client import make_request_options
from ...types.bulk.bulk_created_field import BulkCreatedField
from ...types.bulk.created_field_list_response import CreatedFieldListResponse

__all__ = ["CreatedFieldsResource", "AsyncCreatedFieldsResource"]


class CreatedFieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreatedFieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return CreatedFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreatedFieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return CreatedFieldsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        create_fields: Iterable[created_field_create_params.CreateField],
        specification: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkCreatedField:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prod/v0/bulk/created-fields/",
            body=maybe_transform(
                {
                    "create_fields": create_fields,
                    "specification": specification,
                },
                created_field_create_params.CreatedFieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCreatedField,
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
    ) -> BulkCreatedField:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/prod/v0/bulk/created-fields/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCreatedField,
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
    ) -> CreatedFieldListResponse:
        return self._get(
            "/prod/v0/bulk/created-fields/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedFieldListResponse,
        )


class AsyncCreatedFieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreatedFieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncCreatedFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreatedFieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncCreatedFieldsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        create_fields: Iterable[created_field_create_params.CreateField],
        specification: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkCreatedField:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prod/v0/bulk/created-fields/",
            body=await async_maybe_transform(
                {
                    "create_fields": create_fields,
                    "specification": specification,
                },
                created_field_create_params.CreatedFieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCreatedField,
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
    ) -> BulkCreatedField:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/prod/v0/bulk/created-fields/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCreatedField,
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
    ) -> CreatedFieldListResponse:
        return await self._get(
            "/prod/v0/bulk/created-fields/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedFieldListResponse,
        )


class CreatedFieldsResourceWithRawResponse:
    def __init__(self, created_fields: CreatedFieldsResource) -> None:
        self._created_fields = created_fields

        self.create = to_raw_response_wrapper(
            created_fields.create,
        )
        self.retrieve = to_raw_response_wrapper(
            created_fields.retrieve,
        )
        self.list = to_raw_response_wrapper(
            created_fields.list,
        )


class AsyncCreatedFieldsResourceWithRawResponse:
    def __init__(self, created_fields: AsyncCreatedFieldsResource) -> None:
        self._created_fields = created_fields

        self.create = async_to_raw_response_wrapper(
            created_fields.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            created_fields.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            created_fields.list,
        )


class CreatedFieldsResourceWithStreamingResponse:
    def __init__(self, created_fields: CreatedFieldsResource) -> None:
        self._created_fields = created_fields

        self.create = to_streamed_response_wrapper(
            created_fields.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            created_fields.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            created_fields.list,
        )


class AsyncCreatedFieldsResourceWithStreamingResponse:
    def __init__(self, created_fields: AsyncCreatedFieldsResource) -> None:
        self._created_fields = created_fields

        self.create = async_to_streamed_response_wrapper(
            created_fields.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            created_fields.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            created_fields.list,
        )
