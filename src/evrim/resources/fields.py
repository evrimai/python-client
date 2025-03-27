# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import field_list_params, field_create_params, field_update_params, field_template_params
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
from ..types.field import Field
from .._base_client import make_request_options
from ..types.field_to_template import FieldToTemplate
from ..types.field_list_response import FieldListResponse

__all__ = ["FieldsResource", "AsyncFieldsResource"]


class FieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return FieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return FieldsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        name: str,
        type: str,
        id: int | NotGiven = NOT_GIVEN,
        directed: bool | NotGiven = NOT_GIVEN,
        enum_many: bool | NotGiven = NOT_GIVEN,
        enum_values: List[str] | NotGiven = NOT_GIVEN,
        keyword_search: bool | NotGiven = NOT_GIVEN,
        raw_documents: bool | NotGiven = NOT_GIVEN,
        rel_template_id: Optional[int] | NotGiven = NOT_GIVEN,
        sources: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Field:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prod/v0/fields/",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "type": type,
                    "id": id,
                    "directed": directed,
                    "enum_many": enum_many,
                    "enum_values": enum_values,
                    "keyword_search": keyword_search,
                    "raw_documents": raw_documents,
                    "rel_template_id": rel_template_id,
                    "sources": sources,
                },
                field_create_params.FieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Field,
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
    ) -> Field:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/prod/v0/fields/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Field,
        )

    def update(
        self,
        path_id: int,
        *,
        description: str,
        name: str,
        type: str,
        body_id: int | NotGiven = NOT_GIVEN,
        directed: bool | NotGiven = NOT_GIVEN,
        enum_many: bool | NotGiven = NOT_GIVEN,
        enum_values: List[str] | NotGiven = NOT_GIVEN,
        keyword_search: bool | NotGiven = NOT_GIVEN,
        raw_documents: bool | NotGiven = NOT_GIVEN,
        rel_template_id: Optional[int] | NotGiven = NOT_GIVEN,
        sources: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Field:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/prod/v0/fields/{path_id}/",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "type": type,
                    "body_id": body_id,
                    "directed": directed,
                    "enum_many": enum_many,
                    "enum_values": enum_values,
                    "keyword_search": keyword_search,
                    "raw_documents": raw_documents,
                    "rel_template_id": rel_template_id,
                    "sources": sources,
                },
                field_update_params.FieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Field,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        type: Literal["bln", "enm", "flt", "int", "rel", "str"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldListResponse:
        """
        Args:
          limit: Number of results to return per page.

          offset: The initial index from which to return the results.

          type: - `str` - String
              - `int` - Integer
              - `flt` - Float
              - `bln` - Boolean
              - `rel` - Relationship
              - `enm` - Enum

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/prod/v0/fields/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "type": type,
                    },
                    field_list_params.FieldListParams,
                ),
            ),
            cast_to=FieldListResponse,
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
            f"/prod/v0/fields/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def template(
        self,
        field_id: str,
        *,
        template_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldToTemplate:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return self._post(
            f"/prod/v0/fields/{field_id}/template/",
            body=maybe_transform({"template_id": template_id}, field_template_params.FieldTemplateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldToTemplate,
        )


class AsyncFieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncFieldsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        name: str,
        type: str,
        id: int | NotGiven = NOT_GIVEN,
        directed: bool | NotGiven = NOT_GIVEN,
        enum_many: bool | NotGiven = NOT_GIVEN,
        enum_values: List[str] | NotGiven = NOT_GIVEN,
        keyword_search: bool | NotGiven = NOT_GIVEN,
        raw_documents: bool | NotGiven = NOT_GIVEN,
        rel_template_id: Optional[int] | NotGiven = NOT_GIVEN,
        sources: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Field:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prod/v0/fields/",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "type": type,
                    "id": id,
                    "directed": directed,
                    "enum_many": enum_many,
                    "enum_values": enum_values,
                    "keyword_search": keyword_search,
                    "raw_documents": raw_documents,
                    "rel_template_id": rel_template_id,
                    "sources": sources,
                },
                field_create_params.FieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Field,
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
    ) -> Field:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/prod/v0/fields/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Field,
        )

    async def update(
        self,
        path_id: int,
        *,
        description: str,
        name: str,
        type: str,
        body_id: int | NotGiven = NOT_GIVEN,
        directed: bool | NotGiven = NOT_GIVEN,
        enum_many: bool | NotGiven = NOT_GIVEN,
        enum_values: List[str] | NotGiven = NOT_GIVEN,
        keyword_search: bool | NotGiven = NOT_GIVEN,
        raw_documents: bool | NotGiven = NOT_GIVEN,
        rel_template_id: Optional[int] | NotGiven = NOT_GIVEN,
        sources: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Field:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/prod/v0/fields/{path_id}/",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "type": type,
                    "body_id": body_id,
                    "directed": directed,
                    "enum_many": enum_many,
                    "enum_values": enum_values,
                    "keyword_search": keyword_search,
                    "raw_documents": raw_documents,
                    "rel_template_id": rel_template_id,
                    "sources": sources,
                },
                field_update_params.FieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Field,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        type: Literal["bln", "enm", "flt", "int", "rel", "str"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldListResponse:
        """
        Args:
          limit: Number of results to return per page.

          offset: The initial index from which to return the results.

          type: - `str` - String
              - `int` - Integer
              - `flt` - Float
              - `bln` - Boolean
              - `rel` - Relationship
              - `enm` - Enum

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/prod/v0/fields/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "type": type,
                    },
                    field_list_params.FieldListParams,
                ),
            ),
            cast_to=FieldListResponse,
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
            f"/prod/v0/fields/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def template(
        self,
        field_id: str,
        *,
        template_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FieldToTemplate:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        return await self._post(
            f"/prod/v0/fields/{field_id}/template/",
            body=await async_maybe_transform({"template_id": template_id}, field_template_params.FieldTemplateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FieldToTemplate,
        )


class FieldsResourceWithRawResponse:
    def __init__(self, fields: FieldsResource) -> None:
        self._fields = fields

        self.create = to_raw_response_wrapper(
            fields.create,
        )
        self.retrieve = to_raw_response_wrapper(
            fields.retrieve,
        )
        self.update = to_raw_response_wrapper(
            fields.update,
        )
        self.list = to_raw_response_wrapper(
            fields.list,
        )
        self.delete = to_raw_response_wrapper(
            fields.delete,
        )
        self.template = to_raw_response_wrapper(
            fields.template,
        )


class AsyncFieldsResourceWithRawResponse:
    def __init__(self, fields: AsyncFieldsResource) -> None:
        self._fields = fields

        self.create = async_to_raw_response_wrapper(
            fields.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            fields.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            fields.update,
        )
        self.list = async_to_raw_response_wrapper(
            fields.list,
        )
        self.delete = async_to_raw_response_wrapper(
            fields.delete,
        )
        self.template = async_to_raw_response_wrapper(
            fields.template,
        )


class FieldsResourceWithStreamingResponse:
    def __init__(self, fields: FieldsResource) -> None:
        self._fields = fields

        self.create = to_streamed_response_wrapper(
            fields.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            fields.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            fields.update,
        )
        self.list = to_streamed_response_wrapper(
            fields.list,
        )
        self.delete = to_streamed_response_wrapper(
            fields.delete,
        )
        self.template = to_streamed_response_wrapper(
            fields.template,
        )


class AsyncFieldsResourceWithStreamingResponse:
    def __init__(self, fields: AsyncFieldsResource) -> None:
        self._fields = fields

        self.create = async_to_streamed_response_wrapper(
            fields.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            fields.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            fields.update,
        )
        self.list = async_to_streamed_response_wrapper(
            fields.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            fields.delete,
        )
        self.template = async_to_streamed_response_wrapper(
            fields.template,
        )
