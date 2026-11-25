# Python-библиотека API Perplexity

**Языки / Languages:** [English](./README.md) · [中文](./README-ZH.md) · [Español](./README-ES.md) · [Français](./README-FR.md) · [Português](./README-PT.md) · [Русский](./README-RU.md) · [Deutsch](./README-DE.md)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/perplexityai.svg?label=pypi%20(stable))](https://pypi.org/project/perplexityai/)

Python-библиотека Perplexity обеспечивает удобный доступ к REST API Perplexity из любого приложения на Python 3.9+. Библиотека включает определения типов для всех параметров запросов и полей ответов, а также предоставляет синхронные и асинхронные клиенты на базе [httpx](https://github.com/encode/httpx).

Она сгенерирована с помощью [Stainless](https://www.stainless.com/).

## Документация

Документация REST API доступна на [docs.perplexity.ai](https://docs.perplexity.ai/). Полный API этой библиотеки можно найти в [api.md](api.md).

## Установка

```sh
# install from PyPI
pip install perplexityai
```

## Search API

Получите результаты веб-поиска:

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

Полный API этой библиотеки можно найти в [api.md](api.md).

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

Хотя вы можете передать ключевой аргумент `api_key`,
мы рекомендуем использовать [python-dotenv](https://pypi.org/project/python-dotenv/)
и добавить `PERPLEXITY_API_KEY="My API Key"` в ваш файл `.env`,
чтобы API-ключ не хранился в системе контроля версий.

## Асинхронное использование

Просто импортируйте `AsyncPerplexity` вместо `Perplexity` и используйте `await` с каждым вызовом API:

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

Функциональность синхронного и асинхронного клиентов в остальном идентична.

### С aiohttp

По умолчанию асинхронный клиент использует `httpx` для HTTP-запросов. Однако для повышения производительности при конкурентном доступе вы также можете использовать `aiohttp` в качестве HTTP-бэкенда.

Вы можете включить это, установив `aiohttp`:

```sh
# install from PyPI
pip install perplexityai[aiohttp]
```

Затем вы можете включить это, создав экземпляр клиента с `http_client=DefaultAioHttpClient()`:

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

## Потоковые ответы

Мы поддерживаем потоковые ответы с использованием Server Side Events (SSE).

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

Асинхронный клиент использует точно такой же интерфейс.

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

## Использование типов

Вложенные параметры запросов — это [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Ответы — это [модели Pydantic](https://docs.pydantic.dev), которые также предоставляют вспомогательные методы для таких операций, как:

- Сериализация обратно в JSON, `model.to_json()`
- Преобразование в словарь, `model.to_dict()`

Типизированные запросы и ответы обеспечивают автодополнение и документацию в вашем редакторе. Если вы хотите видеть ошибки типов в VS Code, чтобы раньше обнаруживать ошибки, установите `python.analysis.typeCheckingMode` в `basic`.

## Вложенные параметры

Вложенные параметры — это словари, типизированные с помощью `TypedDict`, например:

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

## Обработка ошибок

Когда библиотека не может подключиться к API (например, из-за проблем с сетевым подключением или таймаута), выбрасывается подкласс `perplexity.APIConnectionError`.

Когда API возвращает код статуса неуспешного ответа (то есть 4xx или 5xx), выбрасывается подкласс `perplexity.APIStatusError`, содержащий свойства `status_code` и `response`.

Все ошибки наследуются от `perplexity.APIError`.

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

Коды ошибок следующие:

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

### Повторные попытки

Некоторые ошибки автоматически повторяются 2 раза по умолчанию с короткой экспоненциальной задержкой.
Ошибки подключения (например, из-за проблем с сетевым подключением), 408 Request Timeout, 409 Conflict,
429 Rate Limit и внутренние ошибки >=500 по умолчанию повторяются.

Вы можете использовать опцию `max_retries` для настройки или отключения параметров повторных попыток:

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

### Таймауты

По умолчанию запросы завершаются по таймауту через 15 минут. Вы можете настроить это с помощью опции `timeout`,
которая принимает float или объект [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration):

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

При таймауте выбрасывается `APITimeoutError`.

Обратите внимание, что запросы, завершившиеся по таймауту, [повторяются дважды по умолчанию](#повторные-попытки).

## Расширенные возможности

### Логирование

Мы используем модуль [`logging`](https://docs.python.org/3/library/logging.html) стандартной библиотеки.

Вы можете включить логирование, установив переменную окружения `PERPLEXITY_LOG` в `info`.

```shell
$ export PERPLEXITY_LOG=info
```

Или в `debug` для более подробного логирования.

### Как определить, означает ли `None` значение `null` или отсутствие поля

В ответе API поле может быть явно `null` или полностью отсутствовать; в обоих случаях его значение в этой библиотеке — `None`. Вы можете различить эти два случая с помощью `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Доступ к необработанным данным ответа (например, заголовкам)

К «необработанному» объекту Response можно получить доступ, добавив префикс `.with_raw_response.` к любому вызову HTTP-метода, например:

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

Эти методы возвращают объект [`APIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py).

Асинхронный клиент возвращает [`AsyncAPIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py) с той же структурой; единственное отличие — методы с `await` для чтения содержимого ответа.

#### `.with_streaming_response`

Интерфейс выше жадно читает полное тело ответа при выполнении запроса, что не всегда желательно.

Для потоковой передачи тела ответа используйте `.with_streaming_response`, что требует менеджера контекста и читает тело ответа только после вызова `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` или `.parse()`. В асинхронном клиенте это асинхронные методы.

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

Менеджер контекста необходим, чтобы ответ был надёжно закрыт.

### Выполнение пользовательских/недокументированных запросов

Эта библиотека типизирована для удобного доступа к документированному API.

Если вам нужен доступ к недокументированным endpoint'ам, параметрам или свойствам ответа, библиотеку всё равно можно использовать.

#### Недокументированные endpoint'ы

Для выполнения запросов к недокументированным endpoint'ам вы можете использовать `client.get`, `client.post` и другие
HTTP-глаголы. Параметры клиента будут учитываться (например, повторные попытки) при выполнении этого запроса.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Недокументированные параметры запроса

Если вы хотите явно отправить дополнительный параметр, вы можете сделать это с помощью опций запроса `extra_query`, `extra_body` и `extra_headers`.

#### Недокументированные свойства ответа

Для доступа к недокументированным свойствам ответа вы можете обращаться к дополнительным полям, например `response.unknown_prop`. Вы
также можете получить все дополнительные поля модели Pydantic в виде словаря с помощью
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Настройка HTTP-клиента

Вы можете напрямую переопределить [клиент httpx](https://www.python-httpx.org/api/#client) для настройки под ваш случай использования, включая:

- Поддержку [прокси](https://www.python-httpx.org/advanced/proxies/)
- Пользовательские [транспорты](https://www.python-httpx.org/advanced/transports/)
- Дополнительную [расширенную](https://www.python-httpx.org/advanced/clients/) функциональность

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

Вы также можете настраивать клиент для каждого запроса с помощью `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Управление HTTP-ресурсами

По умолчанию библиотека закрывает базовые HTTP-соединения, когда клиент [собирается сборщиком мусора](https://docs.python.org/3/reference/datamodel.html#object.__del__). При необходимости вы можете вручную закрыть клиент с помощью метода `.close()` или с помощью менеджера контекста, который закрывается при выходе.

```py
from perplexity import Perplexity

with Perplexity() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Версионирование

Этот пакет в целом следует соглашениям [SemVer](https://semver.org/spec/v2.0.0.html), хотя некоторые обратно несовместимые изменения могут выпускаться как минорные версии:

1. Изменения, которые затрагивают только статические типы, не нарушая поведение во время выполнения.
2. Изменения во внутренних компонентах библиотеки, которые технически являются публичными, но не предназначены или не документированы для внешнего использования. _(Пожалуйста, откройте issue на GitHub, чтобы сообщить нам, если вы полагаетесь на такие внутренние компоненты.)_
3. Изменения, которые, как мы ожидаем, не повлияют на подавляющее большинство пользователей на практике.

Мы серьёзно относимся к обратной совместимости и стремимся обеспечить вам плавный процесс обновления.

Мы будем рады вашим отзывам; пожалуйста, откройте [issue](https://www.github.com/perplexityai/perplexity-py/issues) с вопросами, сообщениями об ошибках или предложениями.

### Определение установленной версии

Если вы обновились до последней версии, но не видите ожидаемых новых функций, скорее всего, ваша среда Python всё ещё использует более старую версию.

Вы можете определить версию, используемую во время выполнения, с помощью:

```py
import perplexity
print(perplexity.__version__)
```

## Требования

Python 3.9 или выше.

## Участие в разработке

См. [документацию по участию](./CONTRIBUTING.md).
