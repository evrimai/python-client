# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim
from tests.utils import assert_matches_type
from evrim.types.prod.v0.compose import ProfileCreateSnapshotResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_snapshot(self, client: Evrim) -> None:
        profile = client.prod.v0.compose.profile.create_snapshot(
            answer_ids=[0],
            created_field_ids=[0],
            specification="specification",
            template_id=0,
        )
        assert_matches_type(ProfileCreateSnapshotResponse, profile, path=["response"])

    @parametrize
    def test_raw_response_create_snapshot(self, client: Evrim) -> None:
        response = client.prod.v0.compose.profile.with_raw_response.create_snapshot(
            answer_ids=[0],
            created_field_ids=[0],
            specification="specification",
            template_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileCreateSnapshotResponse, profile, path=["response"])

    @parametrize
    def test_streaming_response_create_snapshot(self, client: Evrim) -> None:
        with client.prod.v0.compose.profile.with_streaming_response.create_snapshot(
            answer_ids=[0],
            created_field_ids=[0],
            specification="specification",
            template_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileCreateSnapshotResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfile:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_snapshot(self, async_client: AsyncEvrim) -> None:
        profile = await async_client.prod.v0.compose.profile.create_snapshot(
            answer_ids=[0],
            created_field_ids=[0],
            specification="specification",
            template_id=0,
        )
        assert_matches_type(ProfileCreateSnapshotResponse, profile, path=["response"])

    @parametrize
    async def test_raw_response_create_snapshot(self, async_client: AsyncEvrim) -> None:
        response = await async_client.prod.v0.compose.profile.with_raw_response.create_snapshot(
            answer_ids=[0],
            created_field_ids=[0],
            specification="specification",
            template_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileCreateSnapshotResponse, profile, path=["response"])

    @parametrize
    async def test_streaming_response_create_snapshot(self, async_client: AsyncEvrim) -> None:
        async with async_client.prod.v0.compose.profile.with_streaming_response.create_snapshot(
            answer_ids=[0],
            created_field_ids=[0],
            specification="specification",
            template_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileCreateSnapshotResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
