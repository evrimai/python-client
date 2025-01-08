# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim
from evrim.types import ReportsV3ListResponse
from tests.utils import assert_matches_type
from evrim.types.shared import Report

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReportsV3:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Evrim) -> None:
        reports_v3 = client.reports_v3.create(
            outline_id=0,
            profile_id=0,
        )
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Evrim) -> None:
        response = client.reports_v3.with_raw_response.create(
            outline_id=0,
            profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reports_v3 = response.parse()
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Evrim) -> None:
        with client.reports_v3.with_streaming_response.create(
            outline_id=0,
            profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reports_v3 = response.parse()
            assert_matches_type(Report, reports_v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Evrim) -> None:
        reports_v3 = client.reports_v3.retrieve(
            0,
        )
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Evrim) -> None:
        response = client.reports_v3.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reports_v3 = response.parse()
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Evrim) -> None:
        with client.reports_v3.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reports_v3 = response.parse()
            assert_matches_type(Report, reports_v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Evrim) -> None:
        reports_v3 = client.reports_v3.update(
            id=0,
        )
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Evrim) -> None:
        reports_v3 = client.reports_v3.update(
            id=0,
            outline_id=0,
            profile_id=0,
        )
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Evrim) -> None:
        response = client.reports_v3.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reports_v3 = response.parse()
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Evrim) -> None:
        with client.reports_v3.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reports_v3 = response.parse()
            assert_matches_type(Report, reports_v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Evrim) -> None:
        reports_v3 = client.reports_v3.list()
        assert_matches_type(ReportsV3ListResponse, reports_v3, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Evrim) -> None:
        response = client.reports_v3.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reports_v3 = response.parse()
        assert_matches_type(ReportsV3ListResponse, reports_v3, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Evrim) -> None:
        with client.reports_v3.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reports_v3 = response.parse()
            assert_matches_type(ReportsV3ListResponse, reports_v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Evrim) -> None:
        reports_v3 = client.reports_v3.delete(
            0,
        )
        assert reports_v3 is None

    @parametrize
    def test_raw_response_delete(self, client: Evrim) -> None:
        response = client.reports_v3.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reports_v3 = response.parse()
        assert reports_v3 is None

    @parametrize
    def test_streaming_response_delete(self, client: Evrim) -> None:
        with client.reports_v3.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reports_v3 = response.parse()
            assert reports_v3 is None

        assert cast(Any, response.is_closed) is True


class TestAsyncReportsV3:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEvrim) -> None:
        reports_v3 = await async_client.reports_v3.create(
            outline_id=0,
            profile_id=0,
        )
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEvrim) -> None:
        response = await async_client.reports_v3.with_raw_response.create(
            outline_id=0,
            profile_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reports_v3 = await response.parse()
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEvrim) -> None:
        async with async_client.reports_v3.with_streaming_response.create(
            outline_id=0,
            profile_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reports_v3 = await response.parse()
            assert_matches_type(Report, reports_v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEvrim) -> None:
        reports_v3 = await async_client.reports_v3.retrieve(
            0,
        )
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEvrim) -> None:
        response = await async_client.reports_v3.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reports_v3 = await response.parse()
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEvrim) -> None:
        async with async_client.reports_v3.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reports_v3 = await response.parse()
            assert_matches_type(Report, reports_v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncEvrim) -> None:
        reports_v3 = await async_client.reports_v3.update(
            id=0,
        )
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEvrim) -> None:
        reports_v3 = await async_client.reports_v3.update(
            id=0,
            outline_id=0,
            profile_id=0,
        )
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEvrim) -> None:
        response = await async_client.reports_v3.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reports_v3 = await response.parse()
        assert_matches_type(Report, reports_v3, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEvrim) -> None:
        async with async_client.reports_v3.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reports_v3 = await response.parse()
            assert_matches_type(Report, reports_v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncEvrim) -> None:
        reports_v3 = await async_client.reports_v3.list()
        assert_matches_type(ReportsV3ListResponse, reports_v3, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEvrim) -> None:
        response = await async_client.reports_v3.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reports_v3 = await response.parse()
        assert_matches_type(ReportsV3ListResponse, reports_v3, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEvrim) -> None:
        async with async_client.reports_v3.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reports_v3 = await response.parse()
            assert_matches_type(ReportsV3ListResponse, reports_v3, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncEvrim) -> None:
        reports_v3 = await async_client.reports_v3.delete(
            0,
        )
        assert reports_v3 is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEvrim) -> None:
        response = await async_client.reports_v3.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reports_v3 = await response.parse()
        assert reports_v3 is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEvrim) -> None:
        async with async_client.reports_v3.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reports_v3 = await response.parse()
            assert reports_v3 is None

        assert cast(Any, response.is_closed) is True
