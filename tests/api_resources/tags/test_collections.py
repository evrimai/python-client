# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim
from tests.utils import assert_matches_type
from evrim.types.tags import TagToCollection

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_tag(self, client: Evrim) -> None:
        collection = client.tags.collections.tag(
            tag_id="321669910225",
            collection_id=0,
        )
        assert_matches_type(TagToCollection, collection, path=["response"])

    @parametrize
    def test_raw_response_tag(self, client: Evrim) -> None:
        response = client.tags.collections.with_raw_response.tag(
            tag_id="321669910225",
            collection_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(TagToCollection, collection, path=["response"])

    @parametrize
    def test_streaming_response_tag(self, client: Evrim) -> None:
        with client.tags.collections.with_streaming_response.tag(
            tag_id="321669910225",
            collection_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(TagToCollection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_tag(self, client: Evrim) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            client.tags.collections.with_raw_response.tag(
                tag_id="",
                collection_id=0,
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_tag(self, async_client: AsyncEvrim) -> None:
        collection = await async_client.tags.collections.tag(
            tag_id="321669910225",
            collection_id=0,
        )
        assert_matches_type(TagToCollection, collection, path=["response"])

    @parametrize
    async def test_raw_response_tag(self, async_client: AsyncEvrim) -> None:
        response = await async_client.tags.collections.with_raw_response.tag(
            tag_id="321669910225",
            collection_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(TagToCollection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_tag(self, async_client: AsyncEvrim) -> None:
        async with async_client.tags.collections.with_streaming_response.tag(
            tag_id="321669910225",
            collection_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(TagToCollection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_tag(self, async_client: AsyncEvrim) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tag_id` but received ''"):
            await async_client.tags.collections.with_raw_response.tag(
                tag_id="",
                collection_id=0,
            )
