from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, ForwardRef, cast, get_args, get_origin

import perplexity.generated.api as generated_api
from perplexity._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
)
from perplexity._constants import RAW_RESPONSE_HEADER, OVERRIDE_CAST_TO_HEADER
from perplexity._streaming import Stream, AsyncStream
from perplexity.generated.runtime import (
    BinaryAPIResponse as GeneratedBinaryAPIResponse,
    AsyncBinaryAPIResponse as GeneratedAsyncBinaryAPIResponse,
)

if TYPE_CHECKING:
    from collections.abc import Callable

    from perplexity._client import Perplexity, AsyncPerplexity


class SyncTransportAdapter:
    def __init__(self, client: Perplexity, mode: str | None = None) -> None:
        self._client = client
        self._mode = mode

    def with_response_mode(self, mode: str) -> SyncTransportAdapter:
        return SyncTransportAdapter(self._client, mode)

    def _cast_type(self, model: Any) -> Any:
        if isinstance(model, ForwardRef):
            return self._cast_type(getattr(generated_api, model.__forward_arg__))
        if get_origin(model) is Union:
            return cast(Any, Union)[tuple(self._cast_type(item) for item in get_args(model))]
        if model is GeneratedBinaryAPIResponse:
            return BinaryAPIResponse
        return model

    def _options(self, options: dict[str, Any]) -> dict[str, Any]:
        result = dict(options)
        result["cast_to"] = self._cast_type(result["cast_to"])
        stream_class = result.get("stream_cls")
        if stream_class is not None and result.get("stream") is True:
            result["stream_cls"] = cast(Any, Stream)[self._cast_type(get_args(stream_class)[0])]
        else:
            result.pop("stream_cls", None)
        return result

    def _request(
        self,
        method: Callable[..., Any],
        path: str,
        options: dict[str, Any],
    ) -> Any:
        request_options = self._options(options)

        def request(*, extra_headers: dict[str, Any] | None = None) -> Any:
            transport_options = dict(request_options)
            nested_options = dict(transport_options.pop("options", {}))
            nested_options["headers"] = {
                **dict(nested_options.get("headers", {})),
                **(extra_headers or {}),
            }
            return method(path, **transport_options, options=nested_options)

        if self._mode == "raw":
            return to_raw_response_wrapper(request)()
        if self._mode != "streaming":
            return request()
        if request_options["cast_to"] is BinaryAPIResponse:
            return to_custom_streamed_response_wrapper(request, StreamedBinaryAPIResponse)()
        return to_streamed_response_wrapper(request)()

    def get(self, path: str, **options: Any) -> Any:
        return self._request(self._client.get, path, options)

    def post(self, path: str, **options: Any) -> Any:
        return self._request(self._client.post, path, options)

    def patch(self, path: str, **options: Any) -> Any:
        return self._request(self._client.patch, path, options)

    def put(self, path: str, **options: Any) -> Any:
        return self._request(self._client.put, path, options)

    def delete(self, path: str, **options: Any) -> Any:
        return self._request(self._client.delete, path, options)


class AsyncTransportAdapter:
    def __init__(self, client: AsyncPerplexity, mode: str | None = None) -> None:
        self._client = client
        self._mode = mode

    def with_response_mode(self, mode: str) -> AsyncTransportAdapter:
        return AsyncTransportAdapter(self._client, mode)

    def _cast_type(self, model: Any) -> Any:
        if isinstance(model, ForwardRef):
            return self._cast_type(getattr(generated_api, model.__forward_arg__))
        if get_origin(model) is Union:
            return cast(Any, Union)[tuple(self._cast_type(item) for item in get_args(model))]
        if model is GeneratedAsyncBinaryAPIResponse:
            return AsyncBinaryAPIResponse
        return model

    def _options(self, options: dict[str, Any]) -> dict[str, Any]:
        result = dict(options)
        result["cast_to"] = self._cast_type(result["cast_to"])
        stream_class = result.get("stream_cls")
        if stream_class is not None and result.get("stream") is True:
            result["stream_cls"] = cast(Any, AsyncStream)[self._cast_type(get_args(stream_class)[0])]
        else:
            result.pop("stream_cls", None)
        return result

    async def _request(
        self,
        method: Callable[..., Any],
        path: str,
        options: dict[str, Any],
    ) -> Any:
        request_options = self._options(options)

        async def request(*, extra_headers: dict[str, Any] | None = None) -> Any:
            transport_options = dict(request_options)
            nested_options = dict(transport_options.pop("options", {}))
            nested_options["headers"] = {
                **dict(nested_options.get("headers", {})),
                **(extra_headers or {}),
            }
            return await method(path, **transport_options, options=nested_options)

        if self._mode == "raw":
            return await async_to_raw_response_wrapper(request)()
        if self._mode != "streaming":
            return await request()
        extra_headers: dict[str, Any] = {RAW_RESPONSE_HEADER: "stream"}
        if request_options["cast_to"] is AsyncBinaryAPIResponse:
            extra_headers[OVERRIDE_CAST_TO_HEADER] = AsyncStreamedBinaryAPIResponse
        return await request(extra_headers=extra_headers)

    async def get(self, path: str, **options: Any) -> Any:
        return await self._request(self._client.get, path, options)

    async def post(self, path: str, **options: Any) -> Any:
        return await self._request(self._client.post, path, options)

    async def patch(self, path: str, **options: Any) -> Any:
        return await self._request(self._client.patch, path, options)

    async def put(self, path: str, **options: Any) -> Any:
        return await self._request(self._client.put, path, options)

    async def delete(self, path: str, **options: Any) -> Any:
        return await self._request(self._client.delete, path, options)
