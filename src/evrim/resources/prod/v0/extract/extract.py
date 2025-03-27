# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .raw import (
    RawResource,
    AsyncRawResource,
    RawResourceWithRawResponse,
    AsyncRawResourceWithRawResponse,
    RawResourceWithStreamingResponse,
    AsyncRawResourceWithStreamingResponse,
)
from .value import (
    ValueResource,
    AsyncValueResource,
    ValueResourceWithRawResponse,
    AsyncValueResourceWithRawResponse,
    ValueResourceWithStreamingResponse,
    AsyncValueResourceWithStreamingResponse,
)
from .command import (
    CommandResource,
    AsyncCommandResource,
    CommandResourceWithRawResponse,
    AsyncCommandResourceWithRawResponse,
    CommandResourceWithStreamingResponse,
    AsyncCommandResourceWithStreamingResponse,
)
from ....._compat import cached_property
from .relationship import (
    RelationshipResource,
    AsyncRelationshipResource,
    RelationshipResourceWithRawResponse,
    AsyncRelationshipResourceWithRawResponse,
    RelationshipResourceWithStreamingResponse,
    AsyncRelationshipResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def command(self) -> CommandResource:
        return CommandResource(self._client)

    @cached_property
    def raw(self) -> RawResource:
        return RawResource(self._client)

    @cached_property
    def relationship(self) -> RelationshipResource:
        return RelationshipResource(self._client)

    @cached_property
    def value(self) -> ValueResource:
        return ValueResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def command(self) -> AsyncCommandResource:
        return AsyncCommandResource(self._client)

    @cached_property
    def raw(self) -> AsyncRawResource:
        return AsyncRawResource(self._client)

    @cached_property
    def relationship(self) -> AsyncRelationshipResource:
        return AsyncRelationshipResource(self._client)

    @cached_property
    def value(self) -> AsyncValueResource:
        return AsyncValueResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evrimai/python-client#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evrimai/python-client#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

    @cached_property
    def command(self) -> CommandResourceWithRawResponse:
        return CommandResourceWithRawResponse(self._extract.command)

    @cached_property
    def raw(self) -> RawResourceWithRawResponse:
        return RawResourceWithRawResponse(self._extract.raw)

    @cached_property
    def relationship(self) -> RelationshipResourceWithRawResponse:
        return RelationshipResourceWithRawResponse(self._extract.relationship)

    @cached_property
    def value(self) -> ValueResourceWithRawResponse:
        return ValueResourceWithRawResponse(self._extract.value)


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

    @cached_property
    def command(self) -> AsyncCommandResourceWithRawResponse:
        return AsyncCommandResourceWithRawResponse(self._extract.command)

    @cached_property
    def raw(self) -> AsyncRawResourceWithRawResponse:
        return AsyncRawResourceWithRawResponse(self._extract.raw)

    @cached_property
    def relationship(self) -> AsyncRelationshipResourceWithRawResponse:
        return AsyncRelationshipResourceWithRawResponse(self._extract.relationship)

    @cached_property
    def value(self) -> AsyncValueResourceWithRawResponse:
        return AsyncValueResourceWithRawResponse(self._extract.value)


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

    @cached_property
    def command(self) -> CommandResourceWithStreamingResponse:
        return CommandResourceWithStreamingResponse(self._extract.command)

    @cached_property
    def raw(self) -> RawResourceWithStreamingResponse:
        return RawResourceWithStreamingResponse(self._extract.raw)

    @cached_property
    def relationship(self) -> RelationshipResourceWithStreamingResponse:
        return RelationshipResourceWithStreamingResponse(self._extract.relationship)

    @cached_property
    def value(self) -> ValueResourceWithStreamingResponse:
        return ValueResourceWithStreamingResponse(self._extract.value)


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

    @cached_property
    def command(self) -> AsyncCommandResourceWithStreamingResponse:
        return AsyncCommandResourceWithStreamingResponse(self._extract.command)

    @cached_property
    def raw(self) -> AsyncRawResourceWithStreamingResponse:
        return AsyncRawResourceWithStreamingResponse(self._extract.raw)

    @cached_property
    def relationship(self) -> AsyncRelationshipResourceWithStreamingResponse:
        return AsyncRelationshipResourceWithStreamingResponse(self._extract.relationship)

    @cached_property
    def value(self) -> AsyncValueResourceWithStreamingResponse:
        return AsyncValueResourceWithStreamingResponse(self._extract.value)
