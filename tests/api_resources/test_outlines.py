# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim
from evrim.types import Outline, OutlineListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOutlines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Evrim) -> None:
        outline = client.outlines.create(
            perspective="perspective",
            profile_id=0,
            report_title="report_title",
            section_titles=["string"],
        )
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Evrim) -> None:
        outline = client.outlines.create(
            perspective="perspective",
            profile_id=0,
            report_title="report_title",
            section_titles=["string"],
            outline={},
        )
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Evrim) -> None:
        response = client.outlines.with_raw_response.create(
            perspective="perspective",
            profile_id=0,
            report_title="report_title",
            section_titles=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outline = response.parse()
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Evrim) -> None:
        with client.outlines.with_streaming_response.create(
            perspective="perspective",
            profile_id=0,
            report_title="report_title",
            section_titles=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outline = response.parse()
            assert_matches_type(Outline, outline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Evrim) -> None:
        outline = client.outlines.retrieve(
            0,
        )
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Evrim) -> None:
        response = client.outlines.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outline = response.parse()
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Evrim) -> None:
        with client.outlines.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outline = response.parse()
            assert_matches_type(Outline, outline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Evrim) -> None:
        outline = client.outlines.update(
            id=0,
        )
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Evrim) -> None:
        outline = client.outlines.update(
            id=0,
            outline={},
            perspective="perspective",
            profile_id=0,
            report_title="report_title",
            section_titles=["string"],
        )
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Evrim) -> None:
        response = client.outlines.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outline = response.parse()
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Evrim) -> None:
        with client.outlines.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outline = response.parse()
            assert_matches_type(Outline, outline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Evrim) -> None:
        outline = client.outlines.list()
        assert_matches_type(OutlineListResponse, outline, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Evrim) -> None:
        response = client.outlines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outline = response.parse()
        assert_matches_type(OutlineListResponse, outline, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Evrim) -> None:
        with client.outlines.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outline = response.parse()
            assert_matches_type(OutlineListResponse, outline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Evrim) -> None:
        outline = client.outlines.delete(
            0,
        )
        assert outline is None

    @parametrize
    def test_raw_response_delete(self, client: Evrim) -> None:
        response = client.outlines.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outline = response.parse()
        assert outline is None

    @parametrize
    def test_streaming_response_delete(self, client: Evrim) -> None:
        with client.outlines.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outline = response.parse()
            assert outline is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOutlines:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEvrim) -> None:
        outline = await async_client.outlines.create(
            perspective="perspective",
            profile_id=0,
            report_title="report_title",
            section_titles=["string"],
        )
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEvrim) -> None:
        outline = await async_client.outlines.create(
            perspective="perspective",
            profile_id=0,
            report_title="report_title",
            section_titles=["string"],
            outline={},
        )
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEvrim) -> None:
        response = await async_client.outlines.with_raw_response.create(
            perspective="perspective",
            profile_id=0,
            report_title="report_title",
            section_titles=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outline = await response.parse()
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEvrim) -> None:
        async with async_client.outlines.with_streaming_response.create(
            perspective="perspective",
            profile_id=0,
            report_title="report_title",
            section_titles=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outline = await response.parse()
            assert_matches_type(Outline, outline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEvrim) -> None:
        outline = await async_client.outlines.retrieve(
            0,
        )
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEvrim) -> None:
        response = await async_client.outlines.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outline = await response.parse()
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEvrim) -> None:
        async with async_client.outlines.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outline = await response.parse()
            assert_matches_type(Outline, outline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncEvrim) -> None:
        outline = await async_client.outlines.update(
            id=0,
        )
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEvrim) -> None:
        outline = await async_client.outlines.update(
            id=0,
            outline={},
            perspective="perspective",
            profile_id=0,
            report_title="report_title",
            section_titles=["string"],
        )
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEvrim) -> None:
        response = await async_client.outlines.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outline = await response.parse()
        assert_matches_type(Outline, outline, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEvrim) -> None:
        async with async_client.outlines.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outline = await response.parse()
            assert_matches_type(Outline, outline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncEvrim) -> None:
        outline = await async_client.outlines.list()
        assert_matches_type(OutlineListResponse, outline, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEvrim) -> None:
        response = await async_client.outlines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outline = await response.parse()
        assert_matches_type(OutlineListResponse, outline, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEvrim) -> None:
        async with async_client.outlines.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outline = await response.parse()
            assert_matches_type(OutlineListResponse, outline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncEvrim) -> None:
        outline = await async_client.outlines.delete(
            0,
        )
        assert outline is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEvrim) -> None:
        response = await async_client.outlines.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outline = await response.parse()
        assert outline is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEvrim) -> None:
        async with async_client.outlines.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outline = await response.parse()
            assert outline is None

        assert cast(Any, response.is_closed) is True
