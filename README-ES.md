# Biblioteca Python de la API de Perplexity

**Idiomas / Languages:** [English](./README.md) · [中文](./README-ZH.md) · [Español](./README-ES.md) · [Français](./README-FR.md) · [Português](./README-PT.md) · [Русский](./README-RU.md) · [Deutsch](./README-DE.md)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/perplexityai.svg?label=pypi%20(stable))](https://pypi.org/project/perplexityai/)

La biblioteca Python de Perplexity ofrece un acceso cómodo a la API REST de Perplexity desde cualquier aplicación Python 3.9 o superior. La biblioteca incluye definiciones de tipos para todos los parámetros de solicitud y campos de respuesta, y proporciona clientes síncronos y asíncronos basados en [httpx](https://github.com/encode/httpx).

Está generada con [Stainless](https://www.stainless.com/).

## Documentación

La documentación de la API REST está disponible en [docs.perplexity.ai](https://docs.perplexity.ai/). La API completa de esta biblioteca se encuentra en [api.md](api.md).

## Instalación

```sh
# install from PyPI
pip install perplexityai
```

## API de búsqueda

Obtenga resultados de búsqueda web:

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

## Completaciones de chat

La API completa de esta biblioteca se encuentra en [api.md](api.md).

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

Aunque puede proporcionar un argumento con nombre `api_key`,
recomendamos usar [python-dotenv](https://pypi.org/project/python-dotenv/)
para añadir `PERPLEXITY_API_KEY="My API Key"` a su archivo `.env`
de modo que su clave de API no quede almacenada en el control de versiones.

## Uso asíncrono

Simplemente importe `AsyncPerplexity` en lugar de `Perplexity` y use `await` en cada llamada a la API:

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

La funcionalidad entre los clientes síncrono y asíncrono es idéntica en lo demás.

### Con aiohttp

Por defecto, el cliente asíncrono usa `httpx` para las solicitudes HTTP. Sin embargo, para mejorar el rendimiento de concurrencia también puede usar `aiohttp` como backend HTTP.

Puede habilitarlo instalando `aiohttp`:

```sh
# install from PyPI
pip install perplexityai[aiohttp]
```

A continuación puede habilitarlo instanciando el cliente con `http_client=DefaultAioHttpClient()`:

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

## Respuestas en streaming

Ofrecemos soporte para respuestas en streaming mediante Server Side Events (SSE).

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

El cliente asíncrono usa exactamente la misma interfaz.

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

Los parámetros de solicitud anidados son [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Las respuestas son [modelos Pydantic](https://docs.pydantic.dev) que también ofrecen métodos auxiliares para cosas como:

- Serializar de nuevo a JSON, `model.to_json()`
- Convertir a un diccionario, `model.to_dict()`

Las solicitudes y respuestas tipadas proporcionan autocompletado y documentación dentro de su editor. Si desea ver errores de tipo en VS Code para detectar errores antes, configure `python.analysis.typeCheckingMode` en `basic`.

## Parámetros anidados

Los parámetros anidados son diccionarios, tipados con `TypedDict`, por ejemplo:

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

## Manejo de errores

Cuando la biblioteca no puede conectarse a la API (por ejemplo, debido a problemas de conexión de red o un tiempo de espera agotado), se lanza una subclase de `perplexity.APIConnectionError`.

Cuando la API devuelve un código de estado distinto de éxito (es decir, respuesta 4xx o 5xx), se lanza una subclase de `perplexity.APIStatusError`, que contiene las propiedades `status_code` y `response`.

Todos los errores heredan de `perplexity.APIError`.

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

Los códigos de error son los siguientes:

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

### Reintentos

Ciertos errores se reintentan automáticamente 2 veces por defecto, con un breve retroceso exponencial.
Los errores de conexión (por ejemplo, debido a un problema de conectividad de red), 408 Request Timeout, 409 Conflict,
429 Rate Limit y errores internos >=500 se reintentan por defecto.

Puede usar la opción `max_retries` para configurar o deshabilitar los ajustes de reintento:

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

### Tiempos de espera

Por defecto, las solicitudes agotan el tiempo de espera tras 15 minutos. Puede configurarlo con la opción `timeout`,
que acepta un float o un objeto [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration):

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

Al agotarse el tiempo de espera, se lanza un `APITimeoutError`.

Tenga en cuenta que las solicitudes que agotan el tiempo de espera se [reintentan dos veces por defecto](#reintentos).

## Avanzado

### Registro

Usamos el módulo estándar [`logging`](https://docs.python.org/3/library/logging.html).

Puede habilitar el registro estableciendo la variable de entorno `PERPLEXITY_LOG` en `info`.

```shell
$ export PERPLEXITY_LOG=info
```

O en `debug` para un registro más detallado.

### Cómo saber si `None` significa `null` o ausente

En una respuesta de la API, un campo puede ser explícitamente `null` o estar completamente ausente; en cualquiera de los dos casos, su valor es `None` en esta biblioteca. Puede diferenciar ambos casos con `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Acceso a datos de respuesta sin procesar (p. ej. cabeceras)

Se puede acceder al objeto Response "sin procesar" anteponiendo `.with_raw_response.` a cualquier llamada a un método HTTP, p. ej.,

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

Estos métodos devuelven un objeto [`APIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py).

El cliente asíncrono devuelve un [`AsyncAPIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py) con la misma estructura; la única diferencia son métodos que admiten `await` para leer el contenido de la respuesta.

#### `.with_streaming_response`

La interfaz anterior lee de forma anticipada el cuerpo completo de la respuesta cuando realiza la solicitud, lo cual puede no ser siempre lo que desea.

Para transmitir el cuerpo de la respuesta en streaming, use `.with_streaming_response` en su lugar, lo cual requiere un administrador de contexto y solo lee el cuerpo de la respuesta cuando llama a `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` o `.parse()`. En el cliente asíncrono, estos son métodos async.

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

El administrador de contexto es necesario para que la respuesta se cierre de forma fiable.

### Realizar solicitudes personalizadas o no documentadas

Esta biblioteca está tipada para un acceso cómodo a la API documentada.

Si necesita acceder a endpoints, parámetros o propiedades de respuesta no documentados, la biblioteca sigue siendo utilizable.

#### Endpoints no documentados

Para realizar solicitudes a endpoints no documentados, puede usar `client.get`, `client.post` y otros
verbos HTTP. Las opciones del cliente se respetarán (como los reintentos) al hacer esta solicitud.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Parámetros de solicitud no documentados

Si desea enviar explícitamente un parámetro adicional, puede hacerlo con las opciones de solicitud `extra_query`, `extra_body` y `extra_headers`.

#### Propiedades de respuesta no documentadas

Para acceder a propiedades de respuesta no documentadas, puede acceder a los campos adicionales como `response.unknown_prop`. También
puede obtener todos los campos adicionales del modelo Pydantic como un diccionario con
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuración del cliente HTTP

Puede sobrescribir directamente el [cliente httpx](https://www.python-httpx.org/api/#client) para personalizarlo según su caso de uso, incluyendo:

- Soporte para [proxies](https://www.python-httpx.org/advanced/proxies/)
- [Transportes](https://www.python-httpx.org/advanced/transports/) personalizados
- Funcionalidad [avanzada](https://www.python-httpx.org/advanced/clients/) adicional

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

También puede personalizar el cliente por solicitud usando `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Gestión de recursos HTTP

Por defecto, la biblioteca cierra las conexiones HTTP subyacentes cuando el cliente es [recogido por el recolector de basura](https://docs.python.org/3/reference/datamodel.html#object.__del__). Puede cerrar manualmente el cliente con el método `.close()` si lo desea, o con un administrador de contexto que cierra al salir.

```py
from perplexity import Perplexity

with Perplexity() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versionado

Este paquete sigue en general las convenciones de [SemVer](https://semver.org/spec/v2.0.0.html), aunque ciertos cambios incompatibles con versiones anteriores pueden publicarse como versiones menores:

1. Cambios que solo afectan a tipos estáticos, sin romper el comportamiento en tiempo de ejecución.
2. Cambios en los internos de la biblioteca que son técnicamente públicos pero no están destinados ni documentados para uso externo. _(Abra un issue en GitHub para informarnos si depende de dichos internos.)_
3. Cambios que no esperamos que afecten en la práctica a la gran mayoría de usuarios.

Nos tomamos en serio la compatibilidad hacia atrás y trabajamos para que pueda confiar en una experiencia de actualización fluida.

Valoramos sus comentarios; abra un [issue](https://www.github.com/perplexityai/perplexity-py/issues) con preguntas, errores o sugerencias.

### Determinar la versión instalada

Si ha actualizado a la última versión pero no ve las funciones nuevas que esperaba, es probable que su entorno de Python siga usando una versión anterior.

Puede determinar la versión que se usa en tiempo de ejecución con:

```py
import perplexity
print(perplexity.__version__)
```

## Requisitos

Python 3.9 o superior.

## Contribuir

Consulte [la documentación de contribución](./CONTRIBUTING.md).
