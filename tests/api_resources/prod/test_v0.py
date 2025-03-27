# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim
from tests.utils import assert_matches_type
from evrim.types.prod import V0ListQuestionsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV0:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_questions(self, client: Evrim) -> None:
        v0 = client.prod.v0.list_questions()
        assert_matches_type(V0ListQuestionsResponse, v0, path=["response"])

    @parametrize
    def test_method_list_questions_with_all_params(self, client: Evrim) -> None:
        v0 = client.prod.v0.list_questions(
            limit=0,
            offset=0,
        )
        assert_matches_type(V0ListQuestionsResponse, v0, path=["response"])

    @parametrize
    def test_raw_response_list_questions(self, client: Evrim) -> None:
        response = client.prod.v0.with_raw_response.list_questions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v0 = response.parse()
        assert_matches_type(V0ListQuestionsResponse, v0, path=["response"])

    @parametrize
    def test_streaming_response_list_questions(self, client: Evrim) -> None:
        with client.prod.v0.with_streaming_response.list_questions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v0 = response.parse()
            assert_matches_type(V0ListQuestionsResponse, v0, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV0:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list_questions(self, async_client: AsyncEvrim) -> None:
        v0 = await async_client.prod.v0.list_questions()
        assert_matches_type(V0ListQuestionsResponse, v0, path=["response"])

    @parametrize
    async def test_method_list_questions_with_all_params(self, async_client: AsyncEvrim) -> None:
        v0 = await async_client.prod.v0.list_questions(
            limit=0,
            offset=0,
        )
        assert_matches_type(V0ListQuestionsResponse, v0, path=["response"])

    @parametrize
    async def test_raw_response_list_questions(self, async_client: AsyncEvrim) -> None:
        response = await async_client.prod.v0.with_raw_response.list_questions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v0 = await response.parse()
        assert_matches_type(V0ListQuestionsResponse, v0, path=["response"])

    @parametrize
    async def test_streaming_response_list_questions(self, async_client: AsyncEvrim) -> None:
        async with async_client.prod.v0.with_streaming_response.list_questions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v0 = await response.parse()
            assert_matches_type(V0ListQuestionsResponse, v0, path=["response"])

        assert cast(Any, response.is_closed) is True
