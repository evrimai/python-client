# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TransformResource", "AsyncTransformResource"]


class TransformResource(SyncAPIResource):
    @cached_property
    def profile(self) -> ProfileResource:
        return ProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> TransformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return TransformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return TransformResourceWithStreamingResponse(self)


class AsyncTransformResource(AsyncAPIResource):
    @cached_property
    def profile(self) -> AsyncProfileResource:
        return AsyncProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncTransformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncTransformResourceWithStreamingResponse(self)


class TransformResourceWithRawResponse:
    def __init__(self, transform: TransformResource) -> None:
        self._transform = transform

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        return ProfileResourceWithRawResponse(self._transform.profile)


class AsyncTransformResourceWithRawResponse:
    def __init__(self, transform: AsyncTransformResource) -> None:
        self._transform = transform

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        return AsyncProfileResourceWithRawResponse(self._transform.profile)


class TransformResourceWithStreamingResponse:
    def __init__(self, transform: TransformResource) -> None:
        self._transform = transform

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        return ProfileResourceWithStreamingResponse(self._transform.profile)


class AsyncTransformResourceWithStreamingResponse:
    def __init__(self, transform: AsyncTransformResource) -> None:
        self._transform = transform

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        return AsyncProfileResourceWithStreamingResponse(self._transform.profile)
