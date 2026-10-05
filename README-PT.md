# Biblioteca Python da API Perplexity

**Idiomas / Languages:** [English](./README.md) · [中文](./README-ZH.md) · [Español](./README-ES.md) · [Français](./README-FR.md) · [Português](./README-PT.md) · [Русский](./README-RU.md) · [Deutsch](./README-DE.md)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/perplexityai.svg?label=pypi%20(stable))](https://pypi.org/project/perplexityai/)

A biblioteca Python Perplexity oferece acesso conveniente à API REST Perplexity a partir de qualquer aplicação Python 3.9+. A biblioteca inclui definições de tipos para todos os parâmetros de solicitação e campos de resposta, e oferece clientes síncronos e assíncronos com tecnologia [httpx](https://github.com/encode/httpx).

Ela é gerada com [Stainless](https://www.stainless.com/).

## Documentação

A documentação da API REST pode ser encontrada em [docs.perplexity.ai](https://docs.perplexity.ai/). A API completa desta biblioteca pode ser encontrada em [api.md](api.md).

## Instalação

```sh
# install from PyPI
pip install perplexityai
```

## Search API

Obtenha resultados de pesquisa na web:

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

A API completa desta biblioteca pode ser encontrada em [api.md](api.md).

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

Embora você possa fornecer um argumento de palavra-chave `api_key`,
recomendamos usar [python-dotenv](https://pypi.org/project/python-dotenv/)
para adicionar `PERPLEXITY_API_KEY="My API Key"` ao seu arquivo `.env`,
de modo que sua chave de API não fique armazenada no controle de versão.

## Uso assíncrono

Basta importar `AsyncPerplexity` em vez de `Perplexity` e usar `await` em cada chamada à API:

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

A funcionalidade entre os clientes síncronos e assíncronos é, de resto, idêntica.

### Com aiohttp

Por padrão, o cliente assíncrono usa `httpx` para solicitações HTTP. No entanto, para melhor desempenho de concorrência, você também pode usar `aiohttp` como backend HTTP.

Você pode habilitar isso instalando `aiohttp`:

```sh
# install from PyPI
pip install perplexityai[aiohttp]
```

Em seguida, você pode habilitá-lo instanciando o cliente com `http_client=DefaultAioHttpClient()`:

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

## Respostas em streaming

Oferecemos suporte a respostas em streaming usando Server Side Events (SSE).

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

O cliente assíncrono usa exatamente a mesma interface.

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

## Uso de tipos

Parâmetros de solicitação aninhados são [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). As respostas são [modelos Pydantic](https://docs.pydantic.dev), que também fornecem métodos auxiliares para coisas como:

- Serializar de volta para JSON, `model.to_json()`
- Converter para um dicionário, `model.to_dict()`

Solicitações e respostas tipadas fornecem autocompletar e documentação no seu editor. Se quiser ver erros de tipo no VS Code para ajudar a detectar bugs mais cedo, defina `python.analysis.typeCheckingMode` como `basic`.

## Parâmetros aninhados

Parâmetros aninhados são dicionários, tipados com `TypedDict`, por exemplo:

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

## Tratamento de erros

Quando a biblioteca não consegue se conectar à API (por exemplo, devido a problemas de conexão de rede ou timeout), uma subclasse de `perplexity.APIConnectionError` é lançada.

Quando a API retorna um código de status de falha (ou seja, resposta 4xx ou 5xx), uma subclasse de `perplexity.APIStatusError` é lançada, contendo as propriedades `status_code` e `response`.

Todos os erros herdam de `perplexity.APIError`.

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

Os códigos de erro são os seguintes:

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

### Tentativas novamente

Certos erros são automaticamente repetidos 2 vezes por padrão, com um backoff exponencial curto.
Erros de conexão (por exemplo, devido a um problema de conectividade de rede), 408 Request Timeout, 409 Conflict,
429 Rate Limit e erros internos >=500 são todos repetidos por padrão.

Você pode usar a opção `max_retries` para configurar ou desabilitar as configurações de repetição:

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

### Timeouts

Por padrão, as solicitações expiram após 15 minutos. Você pode configurar isso com a opção `timeout`,
que aceita um float ou um objeto [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration):

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

Em caso de timeout, um `APITimeoutError` é lançado.

Observe que solicitações que expiram são [repetidas duas vezes por padrão](#tentativas-novamente).

## Avançado

### Logging

Usamos o módulo [`logging`](https://docs.python.org/3/library/logging.html) da biblioteca padrão.

Você pode habilitar o logging definindo a variável de ambiente `PERPLEXITY_LOG` como `info`.

```shell
$ export PERPLEXITY_LOG=info
```

Ou como `debug` para logging mais detalhado.

### Como saber se `None` significa `null` ou ausente

Em uma resposta da API, um campo pode ser explicitamente `null` ou estar totalmente ausente; em ambos os casos, seu valor é `None` nesta biblioteca. Você pode diferenciar os dois casos com `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Acessando dados brutos da resposta (por exemplo, cabeçalhos)

O objeto Response "bruto" pode ser acessado prefixando `.with_raw_response.` a qualquer chamada de método HTTP, por exemplo,

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

Esses métodos retornam um objeto [`APIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py).

O cliente assíncrono retorna um [`AsyncAPIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py) com a mesma estrutura; a única diferença são métodos com `await` para ler o conteúdo da resposta.

#### `.with_streaming_response`

A interface acima lê avidamente o corpo completo da resposta quando você faz a solicitação, o que nem sempre é o desejado.

Para fazer streaming do corpo da resposta, use `.with_streaming_response` em vez disso, o que requer um gerenciador de contexto e só lê o corpo da resposta quando você chama `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` ou `.parse()`. No cliente assíncrono, estes são métodos assíncronos.

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

O gerenciador de contexto é necessário para que a resposta seja fechada de forma confiável.

### Fazendo solicitações personalizadas/não documentadas

Esta biblioteca é tipada para acesso conveniente à API documentada.

Se precisar acessar endpoints, parâmetros ou propriedades de resposta não documentados, a biblioteca ainda pode ser usada.

#### Endpoints não documentados

Para fazer solicitações a endpoints não documentados, você pode usar `client.get`, `client.post` e outros
verbos HTTP. As opções do cliente serão respeitadas (como repetições) ao fazer esta solicitação.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Parâmetros de solicitação não documentados

Se quiser enviar explicitamente um parâmetro extra, você pode fazê-lo com as opções de solicitação `extra_query`, `extra_body` e `extra_headers`.

#### Propriedades de resposta não documentadas

Para acessar propriedades de resposta não documentadas, você pode acessar os campos extras como `response.unknown_prop`. Você
também pode obter todos os campos extras no modelo Pydantic como um dicionário com
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configurando o cliente HTTP

Você pode substituir diretamente o [cliente httpx](https://www.python-httpx.org/api/#client) para personalizá-lo para o seu caso de uso, incluindo:

- Suporte a [proxies](https://www.python-httpx.org/advanced/proxies/)
- [Transports](https://www.python-httpx.org/advanced/transports/) personalizados
- Funcionalidade [avançada](https://www.python-httpx.org/advanced/clients/) adicional

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

Você também pode personalizar o cliente por solicitação usando `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Gerenciando recursos HTTP

Por padrão, a biblioteca fecha as conexões HTTP subjacentes sempre que o cliente é [coletado pelo garbage collector](https://docs.python.org/3/reference/datamodel.html#object.__del__). Você pode fechar manualmente o cliente usando o método `.close()` se desejar, ou com um gerenciador de contexto que fecha ao sair.

```py
from perplexity import Perplexity

with Perplexity() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versionamento

Este pacote geralmente segue as convenções [SemVer](https://semver.org/spec/v2.0.0.html), embora certas alterações incompatíveis com versões anteriores possam ser lançadas como versões menores:

1. Alterações que afetam apenas tipos estáticos, sem quebrar o comportamento em tempo de execução.
2. Alterações nos internals da biblioteca que são tecnicamente públicos, mas não destinados ou documentados para uso externo. _(Por favor, abra uma issue no GitHub para nos informar se você depende de tais internals.)_
3. Alterações que não esperamos impactar a vasta maioria dos usuários na prática.

Levamos a compatibilidade com versões anteriores a sério e trabalhamos para garantir que você possa contar com uma experiência de atualização tranquila.

Estamos interessados no seu feedback; por favor, abra uma [issue](https://www.github.com/perplexityai/perplexity-py/issues) com perguntas, bugs ou sugestões.

### Determinando a versão instalada

Se você atualizou para a versão mais recente, mas não está vendo os novos recursos que esperava, é provável que seu ambiente Python ainda esteja usando uma versão mais antiga.

Você pode determinar a versão usada em tempo de execução com:

```py
import perplexity
print(perplexity.__version__)
```

## Requisitos

Python 3.9 ou superior.

## Contribuindo

Consulte [a documentação de contribuição](./CONTRIBUTING.md).
