from functools import cached_property

from perplexity.generated.runtime import AsyncTransport, SyncTransport
from .async_ import (
    AsyncResource,
    AsyncAsyncResource,
    AsyncResourceWithRawResponse,
    AsyncAsyncResourceWithRawResponse,
    AsyncResourceWithStreamingResponse,
    AsyncAsyncResourceWithStreamingResponse,
)
from .browser import (
    BrowserResource,
    AsyncBrowserResource,
    BrowserResourceWithRawResponse,
    AsyncBrowserResourceWithRawResponse,
    BrowserResourceWithStreamingResponse,
    AsyncBrowserResourceWithStreamingResponse,
)
from .chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from .contextualized_embeddings import (
    ContextualizedEmbeddingsResource,
    AsyncContextualizedEmbeddingsResource,
    ContextualizedEmbeddingsResourceWithRawResponse,
    AsyncContextualizedEmbeddingsResourceWithRawResponse,
    ContextualizedEmbeddingsResourceWithStreamingResponse,
    AsyncContextualizedEmbeddingsResourceWithStreamingResponse,
)
from .embeddings import (
    EmbeddingsResource,
    AsyncEmbeddingsResource,
    EmbeddingsResourceWithRawResponse,
    AsyncEmbeddingsResourceWithRawResponse,
    EmbeddingsResourceWithStreamingResponse,
    AsyncEmbeddingsResourceWithStreamingResponse,
)
from .responses import (
    ResponsesResource,
    AsyncResponsesResource,
    ResponsesResourceWithRawResponse,
    AsyncResponsesResourceWithRawResponse,
    ResponsesResourceWithStreamingResponse,
    AsyncResponsesResourceWithStreamingResponse,
)
from .search import (
    SearchResource,
    AsyncSearchResource,
    SearchResourceWithRawResponse,
    AsyncSearchResourceWithRawResponse,
    SearchResourceWithStreamingResponse,
    AsyncSearchResourceWithStreamingResponse,
)


class SyncClientResources:
    _sdk_transport: SyncTransport

    @cached_property
    def async_(self) -> AsyncResource:
        return AsyncResource(self._sdk_transport)

    @cached_property
    def browser(self) -> BrowserResource:
        return BrowserResource(self._sdk_transport)

    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._sdk_transport)

    @cached_property
    def contextualized_embeddings(self) -> ContextualizedEmbeddingsResource:
        return ContextualizedEmbeddingsResource(self._sdk_transport)

    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        return EmbeddingsResource(self._sdk_transport)

    @cached_property
    def responses(self) -> ResponsesResource:
        return ResponsesResource(self._sdk_transport)

    @cached_property
    def search(self) -> SearchResource:
        return SearchResource(self._sdk_transport)


class AsyncClientResources:
    _sdk_transport: AsyncTransport

    @cached_property
    def async_(self) -> AsyncAsyncResource:
        return AsyncAsyncResource(self._sdk_transport)

    @cached_property
    def browser(self) -> AsyncBrowserResource:
        return AsyncBrowserResource(self._sdk_transport)

    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._sdk_transport)

    @cached_property
    def contextualized_embeddings(self) -> AsyncContextualizedEmbeddingsResource:
        return AsyncContextualizedEmbeddingsResource(self._sdk_transport)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        return AsyncEmbeddingsResource(self._sdk_transport)

    @cached_property
    def responses(self) -> AsyncResponsesResource:
        return AsyncResponsesResource(self._sdk_transport)

    @cached_property
    def search(self) -> AsyncSearchResource:
        return AsyncSearchResource(self._sdk_transport)


class SyncClientWithRawResponse:
    def __init__(self, client: SyncClientResources) -> None:
        self._client = client

    @cached_property
    def async_(self) -> AsyncResourceWithRawResponse:
        return AsyncResourceWithRawResponse(self._client.async_)

    @cached_property
    def browser(self) -> BrowserResourceWithRawResponse:
        return BrowserResourceWithRawResponse(self._client.browser)

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def contextualized_embeddings(
        self,
    ) -> ContextualizedEmbeddingsResourceWithRawResponse:
        return ContextualizedEmbeddingsResourceWithRawResponse(
            self._client.contextualized_embeddings
        )

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithRawResponse:
        return EmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def responses(self) -> ResponsesResourceWithRawResponse:
        return ResponsesResourceWithRawResponse(self._client.responses)

    @cached_property
    def search(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self._client.search)


class AsyncClientWithRawResponse:
    def __init__(self, client: AsyncClientResources) -> None:
        self._client = client

    @cached_property
    def async_(self) -> AsyncAsyncResourceWithRawResponse:
        return AsyncAsyncResourceWithRawResponse(self._client.async_)

    @cached_property
    def browser(self) -> AsyncBrowserResourceWithRawResponse:
        return AsyncBrowserResourceWithRawResponse(self._client.browser)

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def contextualized_embeddings(
        self,
    ) -> AsyncContextualizedEmbeddingsResourceWithRawResponse:
        return AsyncContextualizedEmbeddingsResourceWithRawResponse(
            self._client.contextualized_embeddings
        )

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithRawResponse:
        return AsyncEmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithRawResponse:
        return AsyncResponsesResourceWithRawResponse(self._client.responses)

    @cached_property
    def search(self) -> AsyncSearchResourceWithRawResponse:
        return AsyncSearchResourceWithRawResponse(self._client.search)


class SyncClientWithStreamingResponse:
    def __init__(self, client: SyncClientResources) -> None:
        self._client = client

    @cached_property
    def async_(self) -> AsyncResourceWithStreamingResponse:
        return AsyncResourceWithStreamingResponse(self._client.async_)

    @cached_property
    def browser(self) -> BrowserResourceWithStreamingResponse:
        return BrowserResourceWithStreamingResponse(self._client.browser)

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def contextualized_embeddings(
        self,
    ) -> ContextualizedEmbeddingsResourceWithStreamingResponse:
        return ContextualizedEmbeddingsResourceWithStreamingResponse(
            self._client.contextualized_embeddings
        )

    @cached_property
    def embeddings(self) -> EmbeddingsResourceWithStreamingResponse:
        return EmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def responses(self) -> ResponsesResourceWithStreamingResponse:
        return ResponsesResourceWithStreamingResponse(self._client.responses)

    @cached_property
    def search(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self._client.search)


class AsyncClientWithStreamingResponse:
    def __init__(self, client: AsyncClientResources) -> None:
        self._client = client

    @cached_property
    def async_(self) -> AsyncAsyncResourceWithStreamingResponse:
        return AsyncAsyncResourceWithStreamingResponse(self._client.async_)

    @cached_property
    def browser(self) -> AsyncBrowserResourceWithStreamingResponse:
        return AsyncBrowserResourceWithStreamingResponse(self._client.browser)

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def contextualized_embeddings(
        self,
    ) -> AsyncContextualizedEmbeddingsResourceWithStreamingResponse:
        return AsyncContextualizedEmbeddingsResourceWithStreamingResponse(
            self._client.contextualized_embeddings
        )

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResourceWithStreamingResponse:
        return AsyncEmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def responses(self) -> AsyncResponsesResourceWithStreamingResponse:
        return AsyncResponsesResourceWithStreamingResponse(self._client.responses)

    @cached_property
    def search(self) -> AsyncSearchResourceWithStreamingResponse:
        return AsyncSearchResourceWithStreamingResponse(self._client.search)

