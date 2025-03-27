# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestField:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Evrim) -> None:
        field = client.prod.v0.costs.average.field.list()
        assert field is None

    @parametrize
    def test_raw_response_list(self, client: Evrim) -> None:
        response = client.prod.v0.costs.average.field.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert field is None

    @parametrize
    def test_streaming_response_list(self, client: Evrim) -> None:
        with client.prod.v0.costs.average.field.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert field is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_by_type(self, client: Evrim) -> None:
        field = client.prod.v0.costs.average.field.get_by_type()
        assert field is None

    @parametrize
    def test_raw_response_get_by_type(self, client: Evrim) -> None:
        response = client.prod.v0.costs.average.field.with_raw_response.get_by_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert field is None

    @parametrize
    def test_streaming_response_get_by_type(self, client: Evrim) -> None:
        with client.prod.v0.costs.average.field.with_streaming_response.get_by_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert field is None

        assert cast(Any, response.is_closed) is True


class TestAsyncField:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncEvrim) -> None:
        field = await async_client.prod.v0.costs.average.field.list()
        assert field is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEvrim) -> None:
        response = await async_client.prod.v0.costs.average.field.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert field is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEvrim) -> None:
        async with async_client.prod.v0.costs.average.field.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert field is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_by_type(self, async_client: AsyncEvrim) -> None:
        field = await async_client.prod.v0.costs.average.field.get_by_type()
        assert field is None

    @parametrize
    async def test_raw_response_get_by_type(self, async_client: AsyncEvrim) -> None:
        response = await async_client.prod.v0.costs.average.field.with_raw_response.get_by_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert field is None

    @parametrize
    async def test_streaming_response_get_by_type(self, async_client: AsyncEvrim) -> None:
        async with async_client.prod.v0.costs.average.field.with_streaming_response.get_by_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert field is None

        assert cast(Any, response.is_closed) is True
