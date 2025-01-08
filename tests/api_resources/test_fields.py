# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim
from evrim.types import (
    Field,
    FieldToTemplate,
    FieldListResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Evrim) -> None:
        field = client.fields.create(
            description="description",
            name="name",
            type="xxx",
        )
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Evrim) -> None:
        field = client.fields.create(
            description="description",
            name="name",
            type="xxx",
            id=0,
            enum_many=True,
            enum_values=["string"],
            rel_template=0,
            rel_template_id=0,
        )
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Evrim) -> None:
        response = client.fields.with_raw_response.create(
            description="description",
            name="name",
            type="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Evrim) -> None:
        with client.fields.with_streaming_response.create(
            description="description",
            name="name",
            type="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(Field, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Evrim) -> None:
        field = client.fields.retrieve(
            0,
        )
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Evrim) -> None:
        response = client.fields.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Evrim) -> None:
        with client.fields.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(Field, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Evrim) -> None:
        field = client.fields.update(
            path_id=0,
        )
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Evrim) -> None:
        field = client.fields.update(
            path_id=0,
            body_id=0,
            description="description",
            enum_many=True,
            enum_values=["string"],
            name="name",
            rel_template=0,
            rel_template_id=0,
            type="xxx",
        )
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Evrim) -> None:
        response = client.fields.with_raw_response.update(
            path_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Evrim) -> None:
        with client.fields.with_streaming_response.update(
            path_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(Field, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Evrim) -> None:
        field = client.fields.list()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Evrim) -> None:
        response = client.fields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Evrim) -> None:
        with client.fields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldListResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Evrim) -> None:
        field = client.fields.delete(
            0,
        )
        assert field is None

    @parametrize
    def test_raw_response_delete(self, client: Evrim) -> None:
        response = client.fields.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert field is None

    @parametrize
    def test_streaming_response_delete(self, client: Evrim) -> None:
        with client.fields.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert field is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_template(self, client: Evrim) -> None:
        field = client.fields.template(
            field_id="321669910225",
            template_id=0,
        )
        assert_matches_type(FieldToTemplate, field, path=["response"])

    @parametrize
    def test_raw_response_template(self, client: Evrim) -> None:
        response = client.fields.with_raw_response.template(
            field_id="321669910225",
            template_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldToTemplate, field, path=["response"])

    @parametrize
    def test_streaming_response_template(self, client: Evrim) -> None:
        with client.fields.with_streaming_response.template(
            field_id="321669910225",
            template_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldToTemplate, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_template(self, client: Evrim) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            client.fields.with_raw_response.template(
                field_id="",
                template_id=0,
            )


class TestAsyncFields:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEvrim) -> None:
        field = await async_client.fields.create(
            description="description",
            name="name",
            type="xxx",
        )
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEvrim) -> None:
        field = await async_client.fields.create(
            description="description",
            name="name",
            type="xxx",
            id=0,
            enum_many=True,
            enum_values=["string"],
            rel_template=0,
            rel_template_id=0,
        )
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEvrim) -> None:
        response = await async_client.fields.with_raw_response.create(
            description="description",
            name="name",
            type="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEvrim) -> None:
        async with async_client.fields.with_streaming_response.create(
            description="description",
            name="name",
            type="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(Field, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEvrim) -> None:
        field = await async_client.fields.retrieve(
            0,
        )
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEvrim) -> None:
        response = await async_client.fields.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEvrim) -> None:
        async with async_client.fields.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(Field, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncEvrim) -> None:
        field = await async_client.fields.update(
            path_id=0,
        )
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEvrim) -> None:
        field = await async_client.fields.update(
            path_id=0,
            body_id=0,
            description="description",
            enum_many=True,
            enum_values=["string"],
            name="name",
            rel_template=0,
            rel_template_id=0,
            type="xxx",
        )
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEvrim) -> None:
        response = await async_client.fields.with_raw_response.update(
            path_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(Field, field, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEvrim) -> None:
        async with async_client.fields.with_streaming_response.update(
            path_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(Field, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncEvrim) -> None:
        field = await async_client.fields.list()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEvrim) -> None:
        response = await async_client.fields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEvrim) -> None:
        async with async_client.fields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldListResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncEvrim) -> None:
        field = await async_client.fields.delete(
            0,
        )
        assert field is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEvrim) -> None:
        response = await async_client.fields.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert field is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEvrim) -> None:
        async with async_client.fields.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert field is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_template(self, async_client: AsyncEvrim) -> None:
        field = await async_client.fields.template(
            field_id="321669910225",
            template_id=0,
        )
        assert_matches_type(FieldToTemplate, field, path=["response"])

    @parametrize
    async def test_raw_response_template(self, async_client: AsyncEvrim) -> None:
        response = await async_client.fields.with_raw_response.template(
            field_id="321669910225",
            template_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldToTemplate, field, path=["response"])

    @parametrize
    async def test_streaming_response_template(self, async_client: AsyncEvrim) -> None:
        async with async_client.fields.with_streaming_response.template(
            field_id="321669910225",
            template_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldToTemplate, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_template(self, async_client: AsyncEvrim) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_id` but received ''"):
            await async_client.fields.with_raw_response.template(
                field_id="",
                template_id=0,
            )
