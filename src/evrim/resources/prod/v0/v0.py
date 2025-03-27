# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .answers import (
    AnswersResource,
    AsyncAnswersResource,
    AnswersResourceWithRawResponse,
    AsyncAnswersResourceWithRawResponse,
    AnswersResourceWithStreamingResponse,
    AsyncAnswersResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .costs.costs import (
    CostsResource,
    AsyncCostsResource,
    CostsResourceWithRawResponse,
    AsyncCostsResourceWithRawResponse,
    CostsResourceWithStreamingResponse,
    AsyncCostsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.prod import v0_list_questions_params
from .health.health import (
    HealthResource,
    AsyncHealthResource,
    HealthResourceWithRawResponse,
    AsyncHealthResourceWithRawResponse,
    HealthResourceWithStreamingResponse,
    AsyncHealthResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .compose.compose import (
    ComposeResource,
    AsyncComposeResource,
    ComposeResourceWithRawResponse,
    AsyncComposeResourceWithRawResponse,
    ComposeResourceWithStreamingResponse,
    AsyncComposeResourceWithStreamingResponse,
)
from .extract.extract import (
    ExtractResource,
    AsyncExtractResource,
    ExtractResourceWithRawResponse,
    AsyncExtractResourceWithRawResponse,
    ExtractResourceWithStreamingResponse,
    AsyncExtractResourceWithStreamingResponse,
)
from .transform.transform import (
    TransformResource,
    AsyncTransformResource,
    TransformResourceWithRawResponse,
    AsyncTransformResourceWithRawResponse,
    TransformResourceWithStreamingResponse,
    AsyncTransformResourceWithStreamingResponse,
)
from ....types.prod.v0_list_questions_response import V0ListQuestionsResponse

__all__ = ["V0Resource", "AsyncV0Resource"]


class V0Resource(SyncAPIResource):
    @cached_property
    def answers(self) -> AnswersResource:
        return AnswersResource(self._client)

    @cached_property
    def compose(self) -> ComposeResource:
        return ComposeResource(self._client)

    @cached_property
    def costs(self) -> CostsResource:
        return CostsResource(self._client)

    @cached_property
    def extract(self) -> ExtractResource:
        return ExtractResource(self._client)

    @cached_property
    def health(self) -> HealthResource:
        return HealthResource(self._client)

    @cached_property
    def transform(self) -> TransformResource:
        return TransformResource(self._client)

    @cached_property
    def with_raw_response(self) -> V0ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return V0ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V0ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return V0ResourceWithStreamingResponse(self)

    def list_questions(
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
    ) -> V0ListQuestionsResponse:
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
            "/prod/v0/questions/",
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
                    v0_list_questions_params.V0ListQuestionsParams,
                ),
            ),
            cast_to=V0ListQuestionsResponse,
        )


class AsyncV0Resource(AsyncAPIResource):
    @cached_property
    def answers(self) -> AsyncAnswersResource:
        return AsyncAnswersResource(self._client)

    @cached_property
    def compose(self) -> AsyncComposeResource:
        return AsyncComposeResource(self._client)

    @cached_property
    def costs(self) -> AsyncCostsResource:
        return AsyncCostsResource(self._client)

    @cached_property
    def extract(self) -> AsyncExtractResource:
        return AsyncExtractResource(self._client)

    @cached_property
    def health(self) -> AsyncHealthResource:
        return AsyncHealthResource(self._client)

    @cached_property
    def transform(self) -> AsyncTransformResource:
        return AsyncTransformResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV0ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncV0ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV0ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncV0ResourceWithStreamingResponse(self)

    async def list_questions(
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
    ) -> V0ListQuestionsResponse:
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
            "/prod/v0/questions/",
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
                    v0_list_questions_params.V0ListQuestionsParams,
                ),
            ),
            cast_to=V0ListQuestionsResponse,
        )


class V0ResourceWithRawResponse:
    def __init__(self, v0: V0Resource) -> None:
        self._v0 = v0

        self.list_questions = to_raw_response_wrapper(
            v0.list_questions,
        )

    @cached_property
    def answers(self) -> AnswersResourceWithRawResponse:
        return AnswersResourceWithRawResponse(self._v0.answers)

    @cached_property
    def compose(self) -> ComposeResourceWithRawResponse:
        return ComposeResourceWithRawResponse(self._v0.compose)

    @cached_property
    def costs(self) -> CostsResourceWithRawResponse:
        return CostsResourceWithRawResponse(self._v0.costs)

    @cached_property
    def extract(self) -> ExtractResourceWithRawResponse:
        return ExtractResourceWithRawResponse(self._v0.extract)

    @cached_property
    def health(self) -> HealthResourceWithRawResponse:
        return HealthResourceWithRawResponse(self._v0.health)

    @cached_property
    def transform(self) -> TransformResourceWithRawResponse:
        return TransformResourceWithRawResponse(self._v0.transform)


class AsyncV0ResourceWithRawResponse:
    def __init__(self, v0: AsyncV0Resource) -> None:
        self._v0 = v0

        self.list_questions = async_to_raw_response_wrapper(
            v0.list_questions,
        )

    @cached_property
    def answers(self) -> AsyncAnswersResourceWithRawResponse:
        return AsyncAnswersResourceWithRawResponse(self._v0.answers)

    @cached_property
    def compose(self) -> AsyncComposeResourceWithRawResponse:
        return AsyncComposeResourceWithRawResponse(self._v0.compose)

    @cached_property
    def costs(self) -> AsyncCostsResourceWithRawResponse:
        return AsyncCostsResourceWithRawResponse(self._v0.costs)

    @cached_property
    def extract(self) -> AsyncExtractResourceWithRawResponse:
        return AsyncExtractResourceWithRawResponse(self._v0.extract)

    @cached_property
    def health(self) -> AsyncHealthResourceWithRawResponse:
        return AsyncHealthResourceWithRawResponse(self._v0.health)

    @cached_property
    def transform(self) -> AsyncTransformResourceWithRawResponse:
        return AsyncTransformResourceWithRawResponse(self._v0.transform)


class V0ResourceWithStreamingResponse:
    def __init__(self, v0: V0Resource) -> None:
        self._v0 = v0

        self.list_questions = to_streamed_response_wrapper(
            v0.list_questions,
        )

    @cached_property
    def answers(self) -> AnswersResourceWithStreamingResponse:
        return AnswersResourceWithStreamingResponse(self._v0.answers)

    @cached_property
    def compose(self) -> ComposeResourceWithStreamingResponse:
        return ComposeResourceWithStreamingResponse(self._v0.compose)

    @cached_property
    def costs(self) -> CostsResourceWithStreamingResponse:
        return CostsResourceWithStreamingResponse(self._v0.costs)

    @cached_property
    def extract(self) -> ExtractResourceWithStreamingResponse:
        return ExtractResourceWithStreamingResponse(self._v0.extract)

    @cached_property
    def health(self) -> HealthResourceWithStreamingResponse:
        return HealthResourceWithStreamingResponse(self._v0.health)

    @cached_property
    def transform(self) -> TransformResourceWithStreamingResponse:
        return TransformResourceWithStreamingResponse(self._v0.transform)


class AsyncV0ResourceWithStreamingResponse:
    def __init__(self, v0: AsyncV0Resource) -> None:
        self._v0 = v0

        self.list_questions = async_to_streamed_response_wrapper(
            v0.list_questions,
        )

    @cached_property
    def answers(self) -> AsyncAnswersResourceWithStreamingResponse:
        return AsyncAnswersResourceWithStreamingResponse(self._v0.answers)

    @cached_property
    def compose(self) -> AsyncComposeResourceWithStreamingResponse:
        return AsyncComposeResourceWithStreamingResponse(self._v0.compose)

    @cached_property
    def costs(self) -> AsyncCostsResourceWithStreamingResponse:
        return AsyncCostsResourceWithStreamingResponse(self._v0.costs)

    @cached_property
    def extract(self) -> AsyncExtractResourceWithStreamingResponse:
        return AsyncExtractResourceWithStreamingResponse(self._v0.extract)

    @cached_property
    def health(self) -> AsyncHealthResourceWithStreamingResponse:
        return AsyncHealthResourceWithStreamingResponse(self._v0.health)

    @cached_property
    def transform(self) -> AsyncTransformResourceWithStreamingResponse:
        return AsyncTransformResourceWithStreamingResponse(self._v0.transform)
