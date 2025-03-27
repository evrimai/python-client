# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .....types.prod.v0.extract import relationship_list_params, relationship_create_params
from .....types.prod.v0.extract.relationship_list_response import RelationshipListResponse
from .....types.prod.v0.extract.relationship_create_response import RelationshipCreateResponse
from .....types.prod.v0.extract.relationship_retrieve_response import RelationshipRetrieveResponse

__all__ = ["RelationshipResource", "AsyncRelationshipResource"]


class RelationshipResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelationshipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return RelationshipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelationshipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return RelationshipResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        relationship: str,
        source: str,
        specification: str,
        target: str,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelationshipCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prod/v0/extract/relationship/",
            body=maybe_transform(
                {
                    "relationship": relationship,
                    "source": source,
                    "specification": specification,
                    "target": target,
                    "url": url,
                },
                relationship_create_params.RelationshipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RelationshipCreateResponse,
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
    ) -> RelationshipRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/prod/v0/extract/relationship/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RelationshipRetrieveResponse,
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
    ) -> RelationshipListResponse:
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
            "/prod/v0/extract/relationship/",
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
                    relationship_list_params.RelationshipListParams,
                ),
            ),
            cast_to=RelationshipListResponse,
        )


class AsyncRelationshipResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelationshipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncRelationshipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelationshipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncRelationshipResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        relationship: str,
        source: str,
        specification: str,
        target: str,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RelationshipCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prod/v0/extract/relationship/",
            body=await async_maybe_transform(
                {
                    "relationship": relationship,
                    "source": source,
                    "specification": specification,
                    "target": target,
                    "url": url,
                },
                relationship_create_params.RelationshipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RelationshipCreateResponse,
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
    ) -> RelationshipRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/prod/v0/extract/relationship/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RelationshipRetrieveResponse,
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
    ) -> RelationshipListResponse:
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
            "/prod/v0/extract/relationship/",
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
                    relationship_list_params.RelationshipListParams,
                ),
            ),
            cast_to=RelationshipListResponse,
        )


class RelationshipResourceWithRawResponse:
    def __init__(self, relationship: RelationshipResource) -> None:
        self._relationship = relationship

        self.create = to_raw_response_wrapper(
            relationship.create,
        )
        self.retrieve = to_raw_response_wrapper(
            relationship.retrieve,
        )
        self.list = to_raw_response_wrapper(
            relationship.list,
        )


class AsyncRelationshipResourceWithRawResponse:
    def __init__(self, relationship: AsyncRelationshipResource) -> None:
        self._relationship = relationship

        self.create = async_to_raw_response_wrapper(
            relationship.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            relationship.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            relationship.list,
        )


class RelationshipResourceWithStreamingResponse:
    def __init__(self, relationship: RelationshipResource) -> None:
        self._relationship = relationship

        self.create = to_streamed_response_wrapper(
            relationship.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            relationship.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            relationship.list,
        )


class AsyncRelationshipResourceWithStreamingResponse:
    def __init__(self, relationship: AsyncRelationshipResource) -> None:
        self._relationship = relationship

        self.create = async_to_streamed_response_wrapper(
            relationship.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            relationship.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            relationship.list,
        )
