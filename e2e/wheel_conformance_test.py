from __future__ import annotations

import os
import sys
import zipfile
import tempfile
import importlib
from pathlib import Path

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


def wheel_path() -> Path:
    for variable in ("RUNFILES_DIR", "TEST_SRCDIR"):
        value = os.environ.get(variable)
        if value:
            wheels = list(Path(value).rglob("perplexityai-*.whl"))
            if len(wheels) == 1:
                return wheels[0]

    manifest = os.environ.get("RUNFILES_MANIFEST_FILE")
    if manifest:
        for line in Path(manifest).read_text(encoding="utf-8").splitlines():
            logical, separator, physical = line.partition(" ")
            if logical.endswith(".whl") and "perplexityai-" in logical:
                return Path(physical if separator else logical)

    raise AssertionError("packaged perplexityai wheel not found in runfiles")


def test_wheel_conformance() -> None:
    with tempfile.TemporaryDirectory() as directory:
        extracted = Path(directory)
        with zipfile.ZipFile(wheel_path()) as wheel:
            wheel.extractall(extracted)

        sys.path.insert(0, str(extracted))
        perplexity = importlib.import_module("perplexity")
        generated = importlib.import_module("perplexity.generated.api")

        assert Path(perplexity.__file__).resolve().is_relative_to(extracted.resolve())
        assert perplexity.Perplexity
        assert perplexity.AsyncPerplexity
        assert perplexity.APIError

        for module_name, public_base, generated_base in RESOURCE_MODULES:
            module = importlib.import_module(module_name)
            assert getattr(module, f"{public_base}Resource") is getattr(
                generated,
                f"{generated_base}Resource",
            )
            assert getattr(module, f"Async{public_base}Resource") is getattr(
                generated,
                f"AsyncClient{generated_base}Resource",
            )

        with perplexity.Perplexity(api_key="test", base_url="https://example.test") as client:
            assert isinstance(client.chat, generated.ChatResource)
            assert isinstance(client.chat.completions, generated.ChatCompletionsResource)
            assert isinstance(client.responses.files, generated.ResponsesFilesResource)
