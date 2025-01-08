# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import prompt_template_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.prompt_template import PromptTemplate
from ..types.prompt_template_list_response import PromptTemplateListResponse

__all__ = ["PromptTemplatesResource", "AsyncPromptTemplatesResource"]


class PromptTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return PromptTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return PromptTemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt: str,
        status: Literal["W", "P", "C", "F"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptTemplate:
        """
        Args:
          status: - `W` - WAITING
              - `P` - PROCESSING
              - `C` - COMPLETED
              - `F` - FAILED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prod/v0/prompt-templates/",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "status": status,
                },
                prompt_template_create_params.PromptTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptTemplate,
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
    ) -> PromptTemplate:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/prod/v0/prompt-templates/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptTemplate,
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
    ) -> PromptTemplateListResponse:
        return self._get(
            "/prod/v0/prompt-templates/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptTemplateListResponse,
        )


class AsyncPromptTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncPromptTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt: str,
        status: Literal["W", "P", "C", "F"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PromptTemplate:
        """
        Args:
          status: - `W` - WAITING
              - `P` - PROCESSING
              - `C` - COMPLETED
              - `F` - FAILED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prod/v0/prompt-templates/",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "status": status,
                },
                prompt_template_create_params.PromptTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptTemplate,
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
    ) -> PromptTemplate:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/prod/v0/prompt-templates/{id}/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptTemplate,
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
    ) -> PromptTemplateListResponse:
        return await self._get(
            "/prod/v0/prompt-templates/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromptTemplateListResponse,
        )


class PromptTemplatesResourceWithRawResponse:
    def __init__(self, prompt_templates: PromptTemplatesResource) -> None:
        self._prompt_templates = prompt_templates

        self.create = to_raw_response_wrapper(
            prompt_templates.create,
        )
        self.retrieve = to_raw_response_wrapper(
            prompt_templates.retrieve,
        )
        self.list = to_raw_response_wrapper(
            prompt_templates.list,
        )


class AsyncPromptTemplatesResourceWithRawResponse:
    def __init__(self, prompt_templates: AsyncPromptTemplatesResource) -> None:
        self._prompt_templates = prompt_templates

        self.create = async_to_raw_response_wrapper(
            prompt_templates.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            prompt_templates.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            prompt_templates.list,
        )


class PromptTemplatesResourceWithStreamingResponse:
    def __init__(self, prompt_templates: PromptTemplatesResource) -> None:
        self._prompt_templates = prompt_templates

        self.create = to_streamed_response_wrapper(
            prompt_templates.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            prompt_templates.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            prompt_templates.list,
        )


class AsyncPromptTemplatesResourceWithStreamingResponse:
    def __init__(self, prompt_templates: AsyncPromptTemplatesResource) -> None:
        self._prompt_templates = prompt_templates

        self.create = async_to_streamed_response_wrapper(
            prompt_templates.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            prompt_templates.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            prompt_templates.list,
        )
