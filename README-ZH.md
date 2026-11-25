# Perplexity Python API 库

**语言 / Languages:** [English](./README.md) · [中文](./README-ZH.md) · [Español](./README-ES.md) · [Français](./README-FR.md) · [Português](./README-PT.md) · [Русский](./README-RU.md) · [Deutsch](./README-DE.md)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/perplexityai.svg?label=pypi%20(stable))](https://pypi.org/project/perplexityai/)

Perplexity Python 库为任何 Python 3.9+ 应用程序提供了便捷访问 Perplexity REST API 的方式。该库包含所有请求参数和响应字段的类型定义，并提供由 [httpx](https://github.com/encode/httpx) 驱动的同步和异步客户端。

该库由 [Stainless](https://www.stainless.com/) 生成。

## 文档

REST API 文档可在 [docs.perplexity.ai](https://docs.perplexity.ai/) 查看。本库的完整 API 说明见 [api.md](api.md)。

## 安装

```sh
# install from PyPI
pip install perplexityai
```

## Search API

获取网页搜索结果：

```python
import os
from perplexity import Perplexity

client = Perplexity(
    api_key=os.environ.get("PERPLEXITY_API_KEY"),  # This is the default and can be omitted
)

search = client.search.create(
    query="latest AI developments 2024",
    max_results=5
)

for result in search.results:
    print(f"{result.title}: {result.url}")
```

## Chat Completions

本库的完整 API 说明见 [api.md](api.md)。

```python
import os
from perplexity import Perplexity

client = Perplexity(
    api_key=os.environ.get("PERPLEXITY_API_KEY"),  # This is the default and can be omitted
)

stream_chunk = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me about the latest developments in AI",
        }
    ],
    model="sonar",
)
print(stream_chunk.id)
```

虽然你可以通过 `api_key` 关键字参数传入 API 密钥，但我们建议使用 [python-dotenv](https://pypi.org/project/python-dotenv/) 将 `PERPLEXITY_API_KEY="My API Key"` 添加到 `.env` 文件中，这样 API 密钥就不会被提交到源代码管理中。

## 异步用法

只需导入 `AsyncPerplexity` 而不是 `Perplexity`，并在每次 API 调用时使用 `await`：

```python
import os
import asyncio
from perplexity import AsyncPerplexity

client = AsyncPerplexity(
    api_key=os.environ.get("PERPLEXITY_API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    stream_chunk = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Tell me about the latest developments in AI",
            }
        ],
        model="sonar",
    )
    print(stream_chunk.id)


asyncio.run(main())
```

同步客户端与异步客户端的功能在其他方面完全相同。

### 使用 aiohttp

默认情况下，异步客户端使用 `httpx` 发送 HTTP 请求。不过，为了获得更好的并发性能，你也可以使用 `aiohttp` 作为 HTTP 后端。

你可以通过安装 `aiohttp` 来启用此功能：

```sh
# install from PyPI
pip install perplexityai[aiohttp]
```

然后，在实例化客户端时传入 `http_client=DefaultAioHttpClient()` 即可启用：

```python
import os
import asyncio
from perplexity import DefaultAioHttpClient
from perplexity import AsyncPerplexity


async def main() -> None:
    async with AsyncPerplexity(
        api_key=os.environ.get("PERPLEXITY_API_KEY"),  # This is the default and can be omitted
        http_client=DefaultAioHttpClient(),
    ) as client:
        stream_chunk = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Tell me about the latest developments in AI",
                }
            ],
            model="sonar",
        )
        print(stream_chunk.id)


asyncio.run(main())
```

## 流式响应

我们支持使用服务端事件（Server Side Events，SSE）进行流式响应。

```python
from perplexity import Perplexity

client = Perplexity()

stream = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me about the latest developments in AI",
        }
    ],
    model="sonar",
    stream=True,
)
for stream_chunk in stream:
    print(stream_chunk.id)
```

异步客户端使用完全相同的接口。

```python
from perplexity import AsyncPerplexity

client = AsyncPerplexity()

stream = await client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me about the latest developments in AI",
        }
    ],
    model="sonar",
    stream=True,
)
async for stream_chunk in stream:
    print(stream_chunk.id)
```

## 使用类型

嵌套的请求参数是 [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict)。响应是 [Pydantic 模型](https://docs.pydantic.dev)，还提供以下辅助方法：

- 序列化回 JSON：`model.to_json()`
- 转换为字典：`model.to_dict()`

类型化的请求和响应可在编辑器中提供自动补全和文档。如果你希望在 VS Code 中看到类型错误以便更早发现 bug，请将 `python.analysis.typeCheckingMode` 设置为 `basic`。

## 嵌套参数

嵌套参数是字典，使用 `TypedDict` 进行类型标注，例如：

```python
from perplexity import Perplexity

client = Perplexity()

stream_chunk = client.chat.completions.create(
    messages=[
        {
            "content": "string",
            "role": "system",
        }
    ],
    model="model",
    web_search_options={},
)
print(stream_chunk.choices)
```

## 错误处理

当库无法连接到 API 时（例如由于网络连接问题或超时），会抛出 `perplexity.APIConnectionError` 的子类。

当 API 返回非成功状态码（即 4xx 或 5xx 响应）时，会抛出 `perplexity.APIStatusError` 的子类，其中包含 `status_code` 和 `response` 属性。

所有错误都继承自 `perplexity.APIError`。

```python
import perplexity
from perplexity import Perplexity

client = Perplexity()

try:
    client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "What is the capital of France?",
            }
        ],
        model="sonar",
    )
except perplexity.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except perplexity.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except perplexity.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

错误码对应关系如下：

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### 重试

默认情况下，某些错误会自动重试 2 次，并采用短暂的指数退避策略。连接错误（例如由于网络连接问题）、408 Request Timeout、409 Conflict、429 Rate Limit 以及 >=500 内部错误默认都会重试。

你可以使用 `max_retries` 选项来配置或禁用重试设置：

```python
from perplexity import Perplexity

# Configure the default for all requests:
client = Perplexity(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model="sonar",
)
```

### 超时

默认情况下，请求在 15 分钟后超时。你可以通过 `timeout` 选项进行配置，该选项接受浮点数或 [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) 对象：

```python
import httpx
from perplexity import Perplexity

# Configure the default for all requests:
client = Perplexity(
    # 20 seconds (default is 15 minutes)
    timeout=20.0,
)

# More granular control:
client = Perplexity(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model="sonar",
)
```

超时时会抛出 `APITimeoutError`。

请注意，超时的请求[默认会重试两次](#重试)。

## 高级用法

### 日志

我们使用标准库的 [`logging`](https://docs.python.org/3/library/logging.html) 模块。

你可以通过将环境变量 `PERPLEXITY_LOG` 设置为 `info` 来启用日志。

```shell
$ export PERPLEXITY_LOG=info
```

或者设置为 `debug` 以获取更详细的日志输出。

### 如何判断 `None` 表示 `null` 还是字段缺失

在 API 响应中，某个字段可能显式为 `null`，也可能完全缺失；在这两种情况下，该字段在本库中的值都是 `None`。你可以通过 `.model_fields_set` 来区分这两种情况：

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### 访问原始响应数据（例如 headers）

可以通过在任何 HTTP 方法调用前加上 `.with_raw_response.` 来访问"原始" Response 对象，例如：

```py
from perplexity import Perplexity

client = Perplexity()
response = client.chat.completions.with_raw_response.create(
    messages=[{
        "role": "user",
        "content": "What is the capital of France?",
    }],
    model="sonar",
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion.id)
```

这些方法返回 [`APIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py) 对象。

异步客户端返回具有相同结构的 [`AsyncAPIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py)，唯一的区别是读取响应内容的方法需要使用 `await`。

#### `.with_streaming_response`

上述接口在你发起请求时会立即读取完整的响应体，这可能并不总是你想要的。

若要流式读取响应体，请改用 `.with_streaming_response`，它需要配合上下文管理器使用，并且只有在你调用 `.read()`、`.text()`、`.json()`、`.iter_bytes()`、`.iter_text()`、`.iter_lines()` 或 `.parse()` 时才会读取响应体。在异步客户端中，这些是异步方法。

```python
with client.chat.completions.with_streaming_response.create(
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model="sonar",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

必须使用上下文管理器，以确保响应能够被可靠地关闭。

### 发起自定义/未文档化的请求

本库针对已文档化的 API 提供了便捷的类型支持。

如果你需要访问未文档化的端点、参数或响应属性，仍然可以使用本库。

#### 未文档化的端点

要向未文档化的端点发起请求，可以使用 `client.get`、`client.post` 以及其他 HTTP 动词。发起此类请求时，客户端上的配置选项（例如重试）仍然会被尊重。

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### 未文档化的请求参数

如果你想显式发送额外的参数，可以通过 `extra_query`、`extra_body` 和 `extra_headers` 请求选项来实现。

#### 未文档化的响应属性

要访问未文档化的响应属性，可以像 `response.unknown_prop` 这样访问额外字段。你也可以通过 [`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra) 将 Pydantic 模型上的所有额外字段作为字典获取。

### 配置 HTTP 客户端

你可以直接覆盖 [httpx 客户端](https://www.python-httpx.org/api/#client) 以满足你的使用场景，包括：

- 支持[代理](https://www.python-httpx.org/advanced/proxies/)
- 自定义[传输层](https://www.python-httpx.org/advanced/transports/)
- 其他[高级](https://www.python-httpx.org/advanced/clients/)功能

```python
import httpx
from perplexity import Perplexity, DefaultHttpxClient

client = Perplexity(
    # Or use the `PERPLEXITY_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

你也可以通过 `with_options()` 在每次请求的基础上自定义客户端：

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### 管理 HTTP 资源

默认情况下，当客户端被[垃圾回收](https://docs.python.org/3/reference/datamodel.html#object.__del__)时，库会关闭底层的 HTTP 连接。如果需要，你可以使用 `.close()` 方法手动关闭客户端，或者使用在退出时自动关闭的上下文管理器。

```py
from perplexity import Perplexity

with Perplexity() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## 版本控制

本包通常遵循 [SemVer](https://semver.org/spec/v2.0.0.html) 约定，但某些向后不兼容的变更可能会作为次要版本发布：

1. 仅影响静态类型、但不破坏运行时行为的变更。
2. 对库内部实现的变更，这些实现在技术上属于公开 API，但并非为外部使用而设计或文档化。_（如果你依赖此类内部实现，请提交 GitHub issue 告知我们。）_
3. 我们预计不会对绝大多数用户产生实际影响的变更。

我们非常重视向后兼容性，并努力确保你能获得顺畅的升级体验。

我们非常欢迎你的反馈；如有问题、bug 或建议，请提交 [issue](https://www.github.com/perplexityai/perplexity-py/issues)。

### 确定已安装的版本

如果你已升级到最新版本，但没有看到预期的新功能，那么你的 Python 环境可能仍在使用旧版本。

你可以通过以下方式确定运行时使用的版本：

```py
import perplexity
print(perplexity.__version__)
```

## 环境要求

Python 3.9 或更高版本。

## 贡献

请参阅[贡献文档](./CONTRIBUTING.md)。
