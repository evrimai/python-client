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
from ..._base_client import make_request_options
from ...types.profiles import created_field_create_params
from ...types.shared.created_fields_to_profile import CreatedFieldsToProfile

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
        profile_id: str,
        *,
        field_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreatedFieldsToProfile:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._post(
            f"/prod/v0/profiles/{profile_id}/created-fields/",
            body=maybe_transform({"field_ids": field_ids}, created_field_create_params.CreatedFieldCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedFieldsToProfile,
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
        profile_id: str,
        *,
        field_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreatedFieldsToProfile:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._post(
            f"/prod/v0/profiles/{profile_id}/created-fields/",
            body=await async_maybe_transform(
                {"field_ids": field_ids}, created_field_create_params.CreatedFieldCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedFieldsToProfile,
        )


class CreatedFieldsResourceWithRawResponse:
    def __init__(self, created_fields: CreatedFieldsResource) -> None:
        self._created_fields = created_fields

        self.create = to_raw_response_wrapper(
            created_fields.create,
        )


class AsyncCreatedFieldsResourceWithRawResponse:
    def __init__(self, created_fields: AsyncCreatedFieldsResource) -> None:
        self._created_fields = created_fields

        self.create = async_to_raw_response_wrapper(
            created_fields.create,
        )


class CreatedFieldsResourceWithStreamingResponse:
    def __init__(self, created_fields: CreatedFieldsResource) -> None:
        self._created_fields = created_fields

        self.create = to_streamed_response_wrapper(
            created_fields.create,
        )


class AsyncCreatedFieldsResourceWithStreamingResponse:
    def __init__(self, created_fields: AsyncCreatedFieldsResource) -> None:
        self._created_fields = created_fields

        self.create = async_to_streamed_response_wrapper(
            created_fields.create,
        )
