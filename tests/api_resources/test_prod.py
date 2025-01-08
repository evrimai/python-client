# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim
from evrim.types import ProdSchemaResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProd:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_schema(self, client: Evrim) -> None:
        prod = client.prod.schema()
        assert_matches_type(ProdSchemaResponse, prod, path=["response"])

    @parametrize
    def test_method_schema_with_all_params(self, client: Evrim) -> None:
        prod = client.prod.schema(
            format="json",
            lang="af",
        )
        assert_matches_type(ProdSchemaResponse, prod, path=["response"])

    @parametrize
    def test_raw_response_schema(self, client: Evrim) -> None:
        response = client.prod.with_raw_response.schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prod = response.parse()
        assert_matches_type(ProdSchemaResponse, prod, path=["response"])

    @parametrize
    def test_streaming_response_schema(self, client: Evrim) -> None:
        with client.prod.with_streaming_response.schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prod = response.parse()
            assert_matches_type(ProdSchemaResponse, prod, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProd:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_schema(self, async_client: AsyncEvrim) -> None:
        prod = await async_client.prod.schema()
        assert_matches_type(ProdSchemaResponse, prod, path=["response"])

    @parametrize
    async def test_method_schema_with_all_params(self, async_client: AsyncEvrim) -> None:
        prod = await async_client.prod.schema(
            format="json",
            lang="af",
        )
        assert_matches_type(ProdSchemaResponse, prod, path=["response"])

    @parametrize
    async def test_raw_response_schema(self, async_client: AsyncEvrim) -> None:
        response = await async_client.prod.with_raw_response.schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prod = await response.parse()
        assert_matches_type(ProdSchemaResponse, prod, path=["response"])

    @parametrize
    async def test_streaming_response_schema(self, async_client: AsyncEvrim) -> None:
        async with async_client.prod.with_streaming_response.schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prod = await response.parse()
            assert_matches_type(ProdSchemaResponse, prod, path=["response"])

        assert cast(Any, response.is_closed) is True
