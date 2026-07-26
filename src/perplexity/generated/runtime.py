from __future__ import annotations

# Runtime adapters intentionally preserve third-party transport call signatures.
# ruff: noqa: ANN401
from collections.abc import AsyncIterator, Callable, Iterator, Mapping
from functools import wraps
from typing import Any, Generic, Literal, Protocol, TypeAlias, TypeVar

import httpx
from pydantic import BaseModel as PydanticBaseModel, ConfigDict

_T_co = TypeVar("_T_co", covariant=True)


class Omit:
    pass


class NotGiven:
    pass


omit = Omit()
not_given = NotGiven()
NoneType = type(None)
Body: TypeAlias = Mapping[str, object]
Headers: TypeAlias = Mapping[str, str | None]
Query: TypeAlias = Mapping[str, object]
Timeout: TypeAlias = httpx.Timeout


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(extra="allow", defer_build=True, populate_by_name=True)

    def to_dict(
        self,
        *,
        mode: Literal["json", "python"] = "python",
        use_api_names: bool = True,
        exclude_unset: bool = True,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        warnings: bool = True,
    ) -> dict[str, object]:
        return self.model_dump(
            mode=mode,
            by_alias=use_api_names,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            warnings=warnings,
        )

    def to_json(
        self,
        *,
        indent: int | None = 2,
        use_api_names: bool = True,
        exclude_unset: bool = True,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        warnings: bool = True,
    ) -> str:
        return self.model_dump_json(
            indent=indent,
            by_alias=use_api_names,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            warnings=warnings,
        )


class Stream(Protocol, Generic[_T_co]):
    def __iter__(self) -> Iterator[_T_co]: ...


class AsyncStream(Protocol, Generic[_T_co]):
    def __aiter__(self) -> AsyncIterator[_T_co]: ...


class BinaryAPIResponse(Protocol):
    def read(self) -> bytes: ...


class AsyncBinaryAPIResponse(Protocol):
    async def read(self) -> bytes: ...


class SyncTransport(Protocol):
    def get(self, path: str, **options: Any) -> Any: ...

    def post(self, path: str, **options: Any) -> Any: ...

    def patch(self, path: str, **options: Any) -> Any: ...

    def put(self, path: str, **options: Any) -> Any: ...

    def delete(self, path: str, **options: Any) -> Any: ...

    def with_response_mode(
        self, mode: Literal["raw", "streaming"]
    ) -> SyncTransport: ...


class AsyncTransport(Protocol):
    async def get(self, path: str, **options: Any) -> Any: ...

    async def post(self, path: str, **options: Any) -> Any: ...

    async def patch(self, path: str, **options: Any) -> Any: ...

    async def put(self, path: str, **options: Any) -> Any: ...

    async def delete(self, path: str, **options: Any) -> Any: ...

    def with_response_mode(
        self, mode: Literal["raw", "streaming"]
    ) -> AsyncTransport: ...


class SyncAPIResource:
    def __init__(self, client: SyncTransport) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete


class AsyncAPIResource:
    def __init__(self, client: AsyncTransport) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete


def make_request_options(
    *,
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | Timeout | None | NotGiven = not_given,
) -> dict[str, object]:
    options: dict[str, object] = {}
    if extra_headers is not None:
        options["headers"] = extra_headers
    if extra_query is not None:
        options["params"] = extra_query
    if extra_body is not None:
        options["extra_json"] = extra_body
    if timeout is not not_given:
        options["timeout"] = timeout
    return options


def _sync_response_wrapper(
    resource: SyncAPIResource,
    method_name: str,
    mode: Literal["raw", "streaming"],
) -> Callable[..., Any]:
    method = getattr(resource, method_name)
    mode_resource = type(resource)(resource._client.with_response_mode(mode))
    mode_method = getattr(mode_resource, method_name)

    @wraps(method)
    def wrapped(*args: Any, **kwargs: Any) -> Any:
        return mode_method(*args, **kwargs)

    return wrapped


def _async_response_wrapper(
    resource: AsyncAPIResource,
    method_name: str,
    mode: Literal["raw", "streaming"],
) -> Callable[..., Any]:
    method = getattr(resource, method_name)
    mode_resource = type(resource)(resource._client.with_response_mode(mode))
    mode_method = getattr(mode_resource, method_name)

    @wraps(method)
    async def wrapped(*args: Any, **kwargs: Any) -> Any:
        return await mode_method(*args, **kwargs)

    return wrapped


def to_raw_response_wrapper(
    resource: SyncAPIResource, method_name: str
) -> Callable[..., Any]:
    return _sync_response_wrapper(resource, method_name, "raw")


def to_streamed_response_wrapper(
    resource: SyncAPIResource, method_name: str
) -> Callable[..., Any]:
    return _sync_response_wrapper(resource, method_name, "streaming")


def async_to_raw_response_wrapper(
    resource: AsyncAPIResource, method_name: str
) -> Callable[..., Any]:
    return _async_response_wrapper(resource, method_name, "raw")


def async_to_streamed_response_wrapper(
    resource: AsyncAPIResource, method_name: str
) -> Callable[..., Any]:
    return _async_response_wrapper(resource, method_name, "streaming")
