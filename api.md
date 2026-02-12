# Shared Types

```python
from perplexity.types import (
    APIPublicSearchResult,
    BrowserSessionResponse,
    ChatMessageInput,
    ChatMessageOutput,
    Choice,
    ContextualizedEmbeddingObject,
    EmbeddingObject,
    EmbeddingsUsage,
    ExecuteCodeResponse,
    FileEntry,
    JsonSchemaFormat,
    ListFilesResponse,
    ListProcessesResponse,
    ModifiedFilesResponse,
    PauseSandboxResponse,
    ProcessInfo,
    ReadFileResponse,
    ResponseFormat,
    SandboxSessionResponse,
    SearchResult,
    UsageInfo,
    UserLocation,
    WebSearchOptions,
    WriteFileResponse,
)
```

# Chat

Types:

```python
from perplexity.types import StreamChunk
```

## Completions

Methods:

- <code title="post /chat/completions">client.chat.completions.<a href="./src/perplexity/resources/chat/completions.py">create</a>(\*\*<a href="src/perplexity/types/chat/completion_create_params.py">params</a>) -> <a href="./src/perplexity/types/stream_chunk.py">StreamChunk</a></code>

# Search

Types:

```python
from perplexity.types import SearchCreateResponse
```

Methods:

- <code title="post /search">client.search.<a href="./src/perplexity/resources/search.py">create</a>(\*\*<a href="src/perplexity/types/search_create_params.py">params</a>) -> <a href="./src/perplexity/types/search_create_response.py">SearchCreateResponse</a></code>

# Responses

Types:

```python
from perplexity.types import (
    Annotation,
    ContentPart,
    ErrorInfo,
    FunctionCallOutputItem,
    FunctionTool,
    InputItem,
    OutputItem,
    ResponseStreamChunk,
    ResponsesCreateParams,
    ResponsesUsage,
    ResponseCreateResponse,
)
```

Methods:

- <code title="post /v1/responses">client.responses.<a href="./src/perplexity/resources/responses.py">create</a>(\*\*<a href="src/perplexity/types/response_create_params.py">params</a>) -> <a href="./src/perplexity/types/response_create_response.py">ResponseCreateResponse</a></code>

# Embeddings

Types:

```python
from perplexity.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /v1/embeddings">client.embeddings.<a href="./src/perplexity/resources/embeddings.py">create</a>(\*\*<a href="src/perplexity/types/embedding_create_params.py">params</a>) -> <a href="./src/perplexity/types/embedding_create_response.py">EmbeddingCreateResponse</a></code>

# ContextualizedEmbeddings

Types:

```python
from perplexity.types import ContextualizedEmbeddingCreateResponse
```

Methods:

- <code title="post /v1/contextualizedembeddings">client.contextualized_embeddings.<a href="./src/perplexity/resources/contextualized_embeddings.py">create</a>(\*\*<a href="src/perplexity/types/contextualized_embedding_create_params.py">params</a>) -> <a href="./src/perplexity/types/contextualized_embedding_create_response.py">ContextualizedEmbeddingCreateResponse</a></code>

# Browser

## Sessions

Methods:

- <code title="post /v1/browser/sessions">client.browser.sessions.<a href="./src/perplexity/resources/browser/sessions.py">create</a>() -> <a href="./src/perplexity/types/shared/browser_session_response.py">BrowserSessionResponse</a></code>
- <code title="delete /v1/browser/sessions/{session_id}">client.browser.sessions.<a href="./src/perplexity/resources/browser/sessions.py">delete</a>(session_id) -> None</code>

# Sandbox

## Sessions

Methods:

- <code title="post /v1/sandbox/sessions">client.sandbox.sessions.<a href="./src/perplexity/resources/sandbox/sessions/sessions.py">create</a>(\*\*<a href="src/perplexity/types/sandbox/session_create_params.py">params</a>) -> <a href="./src/perplexity/types/shared/sandbox_session_response.py">SandboxSessionResponse</a></code>
- <code title="delete /v1/sandbox/sessions/{session_id}">client.sandbox.sessions.<a href="./src/perplexity/resources/sandbox/sessions/sessions.py">delete</a>(session_id) -> None</code>
- <code title="get /v1/sandbox/sessions/{session_id}">client.sandbox.sessions.<a href="./src/perplexity/resources/sandbox/sessions/sessions.py">get</a>(session_id) -> <a href="./src/perplexity/types/shared/sandbox_session_response.py">SandboxSessionResponse</a></code>

### Execute

Methods:

- <code title="post /v1/sandbox/sessions/{session_id}/execute">client.sandbox.sessions.execute.<a href="./src/perplexity/resources/sandbox/sessions/execute.py">create</a>(session_id, \*\*<a href="src/perplexity/types/sandbox/sessions/execute_create_params.py">params</a>) -> <a href="./src/perplexity/types/shared/execute_code_response.py">ExecuteCodeResponse</a></code>

### Pause

Methods:

- <code title="post /v1/sandbox/sessions/{session_id}/pause">client.sandbox.sessions.pause.<a href="./src/perplexity/resources/sandbox/sessions/pause.py">create</a>(session_id) -> <a href="./src/perplexity/types/shared/pause_sandbox_response.py">PauseSandboxResponse</a></code>

### Resume

Methods:

- <code title="post /v1/sandbox/sessions/{session_id}/resume">client.sandbox.sessions.resume.<a href="./src/perplexity/resources/sandbox/sessions/resume.py">create</a>(session_id, \*\*<a href="src/perplexity/types/sandbox/sessions/resume_create_params.py">params</a>) -> <a href="./src/perplexity/types/shared/sandbox_session_response.py">SandboxSessionResponse</a></code>

### Files

Methods:

- <code title="get /v1/sandbox/sessions/{session_id}/files/list">client.sandbox.sessions.files.<a href="./src/perplexity/resources/sandbox/sessions/files.py">list</a>(session_id, \*\*<a href="src/perplexity/types/sandbox/sessions/file_list_params.py">params</a>) -> <a href="./src/perplexity/types/shared/list_files_response.py">ListFilesResponse</a></code>
- <code title="get /v1/sandbox/sessions/{session_id}/files/modified">client.sandbox.sessions.files.<a href="./src/perplexity/resources/sandbox/sessions/files.py">modified</a>(session_id) -> <a href="./src/perplexity/types/shared/modified_files_response.py">ModifiedFilesResponse</a></code>
- <code title="get /v1/sandbox/sessions/{session_id}/files">client.sandbox.sessions.files.<a href="./src/perplexity/resources/sandbox/sessions/files.py">read</a>(session_id, \*\*<a href="src/perplexity/types/sandbox/sessions/file_read_params.py">params</a>) -> <a href="./src/perplexity/types/shared/read_file_response.py">ReadFileResponse</a></code>
- <code title="post /v1/sandbox/sessions/{session_id}/files">client.sandbox.sessions.files.<a href="./src/perplexity/resources/sandbox/sessions/files.py">write</a>(session_id, \*\*<a href="src/perplexity/types/sandbox/sessions/file_write_params.py">params</a>) -> <a href="./src/perplexity/types/shared/write_file_response.py">WriteFileResponse</a></code>

### Processes

Methods:

- <code title="get /v1/sandbox/sessions/{session_id}/processes">client.sandbox.sessions.processes.<a href="./src/perplexity/resources/sandbox/sessions/processes.py">list</a>(session_id) -> <a href="./src/perplexity/types/shared/list_processes_response.py">ListProcessesResponse</a></code>
- <code title="delete /v1/sandbox/sessions/{session_id}/processes/{pid}">client.sandbox.sessions.processes.<a href="./src/perplexity/resources/sandbox/sessions/processes.py">delete</a>(pid, \*, session_id) -> None</code>
- <code title="get /v1/sandbox/sessions/{session_id}/processes/{pid}">client.sandbox.sessions.processes.<a href="./src/perplexity/resources/sandbox/sessions/processes.py">get</a>(pid, \*, session_id) -> <a href="./src/perplexity/types/shared/process_info.py">ProcessInfo</a></code>

# Async

## Chat

### Completions

Types:

```python
from perplexity.types.async_.chat import (
    CompletionCreateResponse,
    CompletionListResponse,
    CompletionGetResponse,
)
```

Methods:

- <code title="post /async/chat/completions">client.async*.chat.completions.<a href="./src/perplexity/resources/async*/chat/completions.py">create</a>(\*\*<a href="src/perplexity/types/async_/chat/completion_create_params.py">params</a>) -> <a href="./src/perplexity/types/async_/chat/completion_create_response.py">CompletionCreateResponse</a></code>
- <code title="get /async/chat/completions">client.async*.chat.completions.<a href="./src/perplexity/resources/async*/chat/completions.py">list</a>() -> <a href="./src/perplexity/types/async_/chat/completion_list_response.py">CompletionListResponse</a></code>
- <code title="get /async/chat/completions/{api_request}">client.async*.chat.completions.<a href="./src/perplexity/resources/async*/chat/completions.py">get</a>(api*request, \*\*<a href="src/perplexity/types/async*/chat/completion*get_params.py">params</a>) -> <a href="./src/perplexity/types/async*/chat/completion_get_response.py">CompletionGetResponse</a></code>
