# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    created_field_create_params,
    created_field_update_params,
    created_field_profile_params,
)
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
from ..types.created_field import CreatedField
from ..types.created_field_list_response import CreatedFieldListResponse

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
        description: str,
        name: str,
        specification: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreatedField:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prod/v0/created-fields/",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "specification": specification,
                    "type": type,
                },
                created_field_create_params.CreatedFieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedField,
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
    ) -> CreatedField:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/prod/v0/created-fields/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedField,
        )

    def update(
        self,
        id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        specification: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreatedField:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/prod/v0/created-fields/{id}/",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "specification": specification,
                    "type": type,
                },
                created_field_update_params.CreatedFieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedField,
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
            "/prod/v0/created-fields/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedFieldListResponse,
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
            f"/prod/v0/created-fields/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def profile(
        self,
        field_id: str,
        *,
        profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Attach a created field to a profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/prod/v0/created-fields/{field_id}/profile/",
            body=maybe_transform({"profile_id": profile_id}, created_field_profile_params.CreatedFieldProfileParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        description: str,
        name: str,
        specification: str,
        type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreatedField:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prod/v0/created-fields/",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "specification": specification,
                    "type": type,
                },
                created_field_create_params.CreatedFieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedField,
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
    ) -> CreatedField:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/prod/v0/created-fields/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedField,
        )

    async def update(
        self,
        id: int,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        specification: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreatedField:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/prod/v0/created-fields/{id}/",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "specification": specification,
                    "type": type,
                },
                created_field_update_params.CreatedFieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedField,
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
            "/prod/v0/created-fields/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedFieldListResponse,
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
            f"/prod/v0/created-fields/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def profile(
        self,
        field_id: str,
        *,
        profile_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Attach a created field to a profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not field_id:
            raise ValueError(f"Expected a non-empty value for `field_id` but received {field_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/prod/v0/created-fields/{field_id}/profile/",
            body=await async_maybe_transform(
                {"profile_id": profile_id}, created_field_profile_params.CreatedFieldProfileParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        self.update = to_raw_response_wrapper(
            created_fields.update,
        )
        self.list = to_raw_response_wrapper(
            created_fields.list,
        )
        self.delete = to_raw_response_wrapper(
            created_fields.delete,
        )
        self.profile = to_raw_response_wrapper(
            created_fields.profile,
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
        self.update = async_to_raw_response_wrapper(
            created_fields.update,
        )
        self.list = async_to_raw_response_wrapper(
            created_fields.list,
        )
        self.delete = async_to_raw_response_wrapper(
            created_fields.delete,
        )
        self.profile = async_to_raw_response_wrapper(
            created_fields.profile,
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
        self.update = to_streamed_response_wrapper(
            created_fields.update,
        )
        self.list = to_streamed_response_wrapper(
            created_fields.list,
        )
        self.delete = to_streamed_response_wrapper(
            created_fields.delete,
        )
        self.profile = to_streamed_response_wrapper(
            created_fields.profile,
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
        self.update = async_to_streamed_response_wrapper(
            created_fields.update,
        )
        self.list = async_to_streamed_response_wrapper(
            created_fields.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            created_fields.delete,
        )
        self.profile = async_to_streamed_response_wrapper(
            created_fields.profile,
        )
