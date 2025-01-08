# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim
from tests.utils import assert_matches_type
from evrim.types.profiles import SnapshotListResponse, CreateProfileSnapshot

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Evrim) -> None:
        snapshot = client.profiles.snapshots.create(
            "321669910225",
        )
        assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Evrim) -> None:
        response = client.profiles.snapshots.with_raw_response.create(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Evrim) -> None:
        with client.profiles.snapshots.with_streaming_response.create(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Evrim) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.snapshots.with_raw_response.create(
                "",
            )

    @parametrize
    def test_method_retrieve(self, client: Evrim) -> None:
        snapshot = client.profiles.snapshots.retrieve(
            snapshot_id="snapshot_id",
            profile_id="321669910225",
        )
        assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Evrim) -> None:
        response = client.profiles.snapshots.with_raw_response.retrieve(
            snapshot_id="snapshot_id",
            profile_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Evrim) -> None:
        with client.profiles.snapshots.with_streaming_response.retrieve(
            snapshot_id="snapshot_id",
            profile_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Evrim) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.snapshots.with_raw_response.retrieve(
                snapshot_id="snapshot_id",
                profile_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            client.profiles.snapshots.with_raw_response.retrieve(
                snapshot_id="",
                profile_id="321669910225",
            )

    @parametrize
    def test_method_list(self, client: Evrim) -> None:
        snapshot = client.profiles.snapshots.list(
            "321669910225",
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Evrim) -> None:
        response = client.profiles.snapshots.with_raw_response.list(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Evrim) -> None:
        with client.profiles.snapshots.with_streaming_response.list(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Evrim) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.snapshots.with_raw_response.list(
                "",
            )


class TestAsyncSnapshots:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEvrim) -> None:
        snapshot = await async_client.profiles.snapshots.create(
            "321669910225",
        )
        assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEvrim) -> None:
        response = await async_client.profiles.snapshots.with_raw_response.create(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEvrim) -> None:
        async with async_client.profiles.snapshots.with_streaming_response.create(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncEvrim) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.snapshots.with_raw_response.create(
                "",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEvrim) -> None:
        snapshot = await async_client.profiles.snapshots.retrieve(
            snapshot_id="snapshot_id",
            profile_id="321669910225",
        )
        assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEvrim) -> None:
        response = await async_client.profiles.snapshots.with_raw_response.retrieve(
            snapshot_id="snapshot_id",
            profile_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEvrim) -> None:
        async with async_client.profiles.snapshots.with_streaming_response.retrieve(
            snapshot_id="snapshot_id",
            profile_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(CreateProfileSnapshot, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEvrim) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.snapshots.with_raw_response.retrieve(
                snapshot_id="snapshot_id",
                profile_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snapshot_id` but received ''"):
            await async_client.profiles.snapshots.with_raw_response.retrieve(
                snapshot_id="",
                profile_id="321669910225",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEvrim) -> None:
        snapshot = await async_client.profiles.snapshots.list(
            "321669910225",
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEvrim) -> None:
        response = await async_client.profiles.snapshots.with_raw_response.list(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEvrim) -> None:
        async with async_client.profiles.snapshots.with_streaming_response.list(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncEvrim) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.snapshots.with_raw_response.list(
                "",
            )
