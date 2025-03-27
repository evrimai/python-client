# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim
from tests.utils import assert_matches_type
from evrim.types.prod.v0.costs import AnswerListResponse, AnswerRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnswer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Evrim) -> None:
        answer = client.prod.v0.costs.answer.retrieve(
            0,
        )
        assert_matches_type(AnswerRetrieveResponse, answer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Evrim) -> None:
        response = client.prod.v0.costs.answer.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        answer = response.parse()
        assert_matches_type(AnswerRetrieveResponse, answer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Evrim) -> None:
        with client.prod.v0.costs.answer.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            answer = response.parse()
            assert_matches_type(AnswerRetrieveResponse, answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Evrim) -> None:
        answer = client.prod.v0.costs.answer.list()
        assert_matches_type(AnswerListResponse, answer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Evrim) -> None:
        answer = client.prod.v0.costs.answer.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AnswerListResponse, answer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Evrim) -> None:
        response = client.prod.v0.costs.answer.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        answer = response.parse()
        assert_matches_type(AnswerListResponse, answer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Evrim) -> None:
        with client.prod.v0.costs.answer.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            answer = response.parse()
            assert_matches_type(AnswerListResponse, answer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnswer:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEvrim) -> None:
        answer = await async_client.prod.v0.costs.answer.retrieve(
            0,
        )
        assert_matches_type(AnswerRetrieveResponse, answer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEvrim) -> None:
        response = await async_client.prod.v0.costs.answer.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        answer = await response.parse()
        assert_matches_type(AnswerRetrieveResponse, answer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEvrim) -> None:
        async with async_client.prod.v0.costs.answer.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            answer = await response.parse()
            assert_matches_type(AnswerRetrieveResponse, answer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncEvrim) -> None:
        answer = await async_client.prod.v0.costs.answer.list()
        assert_matches_type(AnswerListResponse, answer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEvrim) -> None:
        answer = await async_client.prod.v0.costs.answer.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AnswerListResponse, answer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEvrim) -> None:
        response = await async_client.prod.v0.costs.answer.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        answer = await response.parse()
        assert_matches_type(AnswerListResponse, answer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEvrim) -> None:
        async with async_client.prod.v0.costs.answer.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            answer = await response.parse()
            assert_matches_type(AnswerListResponse, answer, path=["response"])

        assert cast(Any, response.is_closed) is True
