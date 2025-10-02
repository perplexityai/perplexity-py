# Shared Types

```python
from perplexity.types import (
    APIPublicSearchResult,
    ChatMessageInput,
    ChatMessageOutput,
    Choice,
    UsageInfo,
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

# Search

Types:

```python
from perplexity.types import SearchCreateResponse
```

Methods:

- <code title="post /search">client.search.<a href="./src/perplexity/resources/search.py">create</a>(\*\*<a href="src/perplexity/types/search_create_params.py">params</a>) -> <a href="./src/perplexity/types/search_create_response.py">SearchCreateResponse</a></code>
