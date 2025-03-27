# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.prod.v0 import answer_list_params, answer_create_params
from ....types.prod.v0.answer_list_response import AnswerListResponse
from ....types.prod.v0.answer_create_response import AnswerCreateResponse
from ....types.prod.v0.answer_retrieve_response import AnswerRetrieveResponse

__all__ = ["AnswersResource", "AsyncAnswersResource"]


class AnswersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnswersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AnswersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnswersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AnswersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        specification: str,
        question: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnswerCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prod/v0/answers/",
            body=maybe_transform(
                {
                    "specification": specification,
                    "question": question,
                },
                answer_create_params.AnswerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnswerCreateResponse,
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
    ) -> AnswerRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/prod/v0/answers/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnswerRetrieveResponse,
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
    ) -> AnswerListResponse:
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
            "/prod/v0/answers/",
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
                    answer_list_params.AnswerListParams,
                ),
            ),
            cast_to=AnswerListResponse,
        )


class AsyncAnswersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnswersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncAnswersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnswersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncAnswersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        specification: str,
        question: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnswerCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prod/v0/answers/",
            body=await async_maybe_transform(
                {
                    "specification": specification,
                    "question": question,
                },
                answer_create_params.AnswerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnswerCreateResponse,
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
    ) -> AnswerRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/prod/v0/answers/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnswerRetrieveResponse,
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
    ) -> AnswerListResponse:
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
            "/prod/v0/answers/",
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
                    answer_list_params.AnswerListParams,
                ),
            ),
            cast_to=AnswerListResponse,
        )


class AnswersResourceWithRawResponse:
    def __init__(self, answers: AnswersResource) -> None:
        self._answers = answers

        self.create = to_raw_response_wrapper(
            answers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            answers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            answers.list,
        )


class AsyncAnswersResourceWithRawResponse:
    def __init__(self, answers: AsyncAnswersResource) -> None:
        self._answers = answers

        self.create = async_to_raw_response_wrapper(
            answers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            answers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            answers.list,
        )


class AnswersResourceWithStreamingResponse:
    def __init__(self, answers: AnswersResource) -> None:
        self._answers = answers

        self.create = to_streamed_response_wrapper(
            answers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            answers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            answers.list,
        )


class AsyncAnswersResourceWithStreamingResponse:
    def __init__(self, answers: AsyncAnswersResource) -> None:
        self._answers = answers

        self.create = async_to_streamed_response_wrapper(
            answers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            answers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            answers.list,
        )
