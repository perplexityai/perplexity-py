from __future__ import annotations

import importlib

import pytest

from perplexity import Perplexity
from perplexity.generated import api as generated

RESOURCE_MODULES = [
    ("perplexity.resources.async_.async_", "Async", "Async"),
    ("perplexity.resources.async_.chat.chat", "Chat", "AsyncChat"),
    ("perplexity.resources.async_.chat.completions", "Completions", "AsyncChatCompletions"),
    ("perplexity.resources.browser.browser", "Browser", "Browser"),
    ("perplexity.resources.browser.sessions", "Sessions", "BrowserSessions"),
    ("perplexity.resources.chat.chat", "Chat", "Chat"),
    ("perplexity.resources.chat.completions", "Completions", "ChatCompletions"),
    (
        "perplexity.resources.contextualized_embeddings",
        "ContextualizedEmbeddings",
        "ContextualizedEmbeddings",
    ),
    ("perplexity.resources.embeddings", "Embeddings", "Embeddings"),
    ("perplexity.resources.responses.responses", "Responses", "Responses"),
    ("perplexity.resources.responses.files", "Files", "ResponsesFiles"),
    ("perplexity.resources.search", "Search", "Search"),
]


@pytest.mark.parametrize(("module_name", "public_base", "generated_base"), RESOURCE_MODULES)
def test_legacy_resource_entrypoints_reexport_generated_resources(
    module_name: str,
    public_base: str,
    generated_base: str,
) -> None:
    module = importlib.import_module(module_name)
    aliases = {
        f"{public_base}Resource": f"{generated_base}Resource",
        f"Async{public_base}Resource": f"AsyncClient{generated_base}Resource",
        f"{public_base}ResourceWithRawResponse": f"{generated_base}ResourceWithRawResponse",
        f"Async{public_base}ResourceWithRawResponse": (f"AsyncClient{generated_base}ResourceWithRawResponse"),
        f"{public_base}ResourceWithStreamingResponse": f"{generated_base}ResourceWithStreamingResponse",
        f"Async{public_base}ResourceWithStreamingResponse": (
            f"AsyncClient{generated_base}ResourceWithStreamingResponse"
        ),
    }

    assert set(aliases) <= set(module.__all__)
    for public_name, generated_name in aliases.items():
        assert getattr(module, public_name) is getattr(generated, generated_name)


def test_client_resource_graph_uses_generated_resources() -> None:
    with Perplexity(api_key="test", base_url="https://example.test") as client:
        assert isinstance(client.chat, generated.ChatResource)
        assert isinstance(client.chat.completions, generated.ChatCompletionsResource)
        assert isinstance(client.chat.with_raw_response, generated.ChatResourceWithRawResponse)
        assert isinstance(
            client.chat.with_raw_response.completions,
            generated.ChatCompletionsResourceWithRawResponse,
        )
        assert isinstance(
            client.chat.with_streaming_response,
            generated.ChatResourceWithStreamingResponse,
        )
        assert isinstance(
            client.chat.with_streaming_response.completions,
            generated.ChatCompletionsResourceWithStreamingResponse,
        )

        assert isinstance(client.responses, generated.ResponsesResource)
        assert isinstance(client.responses.files, generated.ResponsesFilesResource)
        assert isinstance(client.browser.sessions, generated.BrowserSessionsResource)
        assert isinstance(client.async_.chat.completions, generated.AsyncChatCompletionsResource)
