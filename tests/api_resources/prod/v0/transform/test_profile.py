# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_latest(self, client: Evrim) -> None:
        profile = client.prod.v0.transform.profile.get_latest(
            0,
        )
        assert profile is None

    @parametrize
    def test_raw_response_get_latest(self, client: Evrim) -> None:
        response = client.prod.v0.transform.profile.with_raw_response.get_latest(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert profile is None

    @parametrize
    def test_streaming_response_get_latest(self, client: Evrim) -> None:
        with client.prod.v0.transform.profile.with_streaming_response.get_latest(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True


class TestAsyncProfile:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_latest(self, async_client: AsyncEvrim) -> None:
        profile = await async_client.prod.v0.transform.profile.get_latest(
            0,
        )
        assert profile is None

    @parametrize
    async def test_raw_response_get_latest(self, async_client: AsyncEvrim) -> None:
        response = await async_client.prod.v0.transform.profile.with_raw_response.get_latest(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert profile is None

    @parametrize
    async def test_streaming_response_get_latest(self, async_client: AsyncEvrim) -> None:
        async with async_client.prod.v0.transform.profile.with_streaming_response.get_latest(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True
