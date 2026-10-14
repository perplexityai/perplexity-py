# Perplexity Python-API-Bibliothek

**Sprachen / Languages:** [English](./README.md) · [中文](./README-ZH.md) · [Español](./README-ES.md) · [Français](./README-FR.md) · [Português](./README-PT.md) · [Русский](./README-RU.md) · [Deutsch](./README-DE.md)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/perplexityai.svg?label=pypi%20(stable))](https://pypi.org/project/perplexityai/)

Die Perplexity Python-Bibliothek bietet bequemen Zugriff auf die Perplexity REST API aus jeder Python-3.9+-Anwendung. Die Bibliothek enthält Typdefinitionen für alle Anfrageparameter und Antwortfelder und bietet sowohl synchrone als auch asynchrone Clients auf Basis von [httpx](https://github.com/encode/httpx).

Sie wird mit [Stainless](https://www.stainless.com/) generiert.

## Dokumentation

Die REST-API-Dokumentation finden Sie unter [docs.perplexity.ai](https://docs.perplexity.ai/). Die vollständige API dieser Bibliothek finden Sie in [api.md](api.md).

## Installation

```sh
# install from PyPI
pip install perplexityai
```

## Search API

Websuchergebnisse abrufen:

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

Die vollständige API dieser Bibliothek finden Sie in [api.md](api.md).

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

Obwohl Sie ein `api_key`-Schlüsselwortargument übergeben können,
empfehlen wir die Verwendung von [python-dotenv](https://pypi.org/project/python-dotenv/),
um `PERPLEXITY_API_KEY="My API Key"` zu Ihrer `.env`-Datei hinzuzufügen,
damit Ihr API-Schlüssel nicht in der Versionskontrolle gespeichert wird.

## Asynchrone Nutzung

Importieren Sie einfach `AsyncPerplexity` anstelle von `Perplexity` und verwenden Sie `await` bei jedem API-Aufruf:

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

Die Funktionalität zwischen den synchronen und asynchronen Clients ist ansonsten identisch.

### Mit aiohttp

Standardmäßig verwendet der asynchrone Client `httpx` für HTTP-Anfragen. Für bessere Concurrency-Leistung können Sie jedoch auch `aiohttp` als HTTP-Backend verwenden.

Sie können dies aktivieren, indem Sie `aiohttp` installieren:

```sh
# install from PyPI
pip install perplexityai[aiohttp]
```

Dann können Sie es aktivieren, indem Sie den Client mit `http_client=DefaultAioHttpClient()` instanziieren:

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

## Streaming-Antworten

Wir unterstützen Streaming-Antworten mit Server Side Events (SSE).

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

Der asynchrone Client verwendet genau dieselbe Schnittstelle.

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

## Verwendung von Typen

Verschachtelte Anfrageparameter sind [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Antworten sind [Pydantic-Modelle](https://docs.pydantic.dev), die auch Hilfsmethoden für Dinge wie bereitstellen:

- Serialisierung zurück in JSON, `model.to_json()`
- Konvertierung in ein Dictionary, `model.to_dict()`

Typisierte Anfragen und Antworten bieten Autovervollständigung und Dokumentation in Ihrem Editor. Wenn Sie Typfehler in VS Code sehen möchten, um Fehler früher zu erkennen, setzen Sie `python.analysis.typeCheckingMode` auf `basic`.

## Verschachtelte Parameter

Verschachtelte Parameter sind Dictionaries, typisiert mit `TypedDict`, zum Beispiel:

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

## Fehlerbehandlung

Wenn die Bibliothek keine Verbindung zur API herstellen kann (z. B. aufgrund von Netzwerkverbindungsproblemen oder einem Timeout), wird eine Unterklasse von `perplexity.APIConnectionError` ausgelöst.

Wenn die API einen Nicht-Erfolgs-Statuscode zurückgibt (d. h. 4xx- oder 5xx-Antwort), wird eine Unterklasse von `perplexity.APIStatusError` ausgelöst, die die Eigenschaften `status_code` und `response` enthält.

Alle Fehler erben von `perplexity.APIError`.

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

Die Fehlercodes sind wie folgt:

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

### Wiederholungsversuche

Bestimmte Fehler werden standardmäßig automatisch 2-mal wiederholt, mit einem kurzen exponentiellen Backoff.
Verbindungsfehler (z. B. aufgrund eines Netzwerkverbindungsproblems), 408 Request Timeout, 409 Conflict,
429 Rate Limit und >=500 Internal-Fehler werden standardmäßig alle wiederholt.

Sie können die Option `max_retries` verwenden, um Wiederholungseinstellungen zu konfigurieren oder zu deaktivieren:

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

Standardmäßig laufen Anfragen nach 15 Minuten ab. Sie können dies mit der Option `timeout` konfigurieren,
die einen Float oder ein [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration)-Objekt akzeptiert:

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

Bei einem Timeout wird ein `APITimeoutError` ausgelöst.

Beachten Sie, dass Anfragen, die ablaufen, [standardmäßig zweimal wiederholt werden](#wiederholungsversuche).

## Erweitert

### Logging

Wir verwenden das Modul [`logging`](https://docs.python.org/3/library/logging.html) der Standardbibliothek.

Sie können Logging aktivieren, indem Sie die Umgebungsvariable `PERPLEXITY_LOG` auf `info` setzen.

```shell
$ export PERPLEXITY_LOG=info
```

Oder auf `debug` für ausführlicheres Logging.

### Wie man erkennt, ob `None` `null` oder fehlend bedeutet

In einer API-Antwort kann ein Feld explizit `null` sein oder vollständig fehlen; in beiden Fällen ist sein Wert in dieser Bibliothek `None`. Sie können die beiden Fälle mit `.model_fields_set` unterscheiden:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Zugriff auf Rohdaten der Antwort (z. B. Header)

Auf das „Roh“-Response-Objekt kann zugegriffen werden, indem `.with_raw_response.` jedem HTTP-Methodenaufruf vorangestellt wird, z. B.:

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

Diese Methoden geben ein [`APIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py)-Objekt zurück.

Der asynchrone Client gibt ein [`AsyncAPIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py) mit derselben Struktur zurück; der einzige Unterschied sind `await`-fähige Methoden zum Lesen des Antwortinhalts.

#### `.with_streaming_response`

Die obige Schnittstelle liest den vollständigen Antwortbody beim Senden der Anfrage sofort ein, was nicht immer gewünscht ist.

Um den Antwortbody zu streamen, verwenden Sie stattdessen `.with_streaming_response`, was einen Kontextmanager erfordert und den Antwortbody erst liest, wenn Sie `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` oder `.parse()` aufrufen. Im asynchronen Client sind dies asynchrone Methoden.

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

Der Kontextmanager ist erforderlich, damit die Antwort zuverlässig geschlossen wird.

### Benutzerdefinierte/undokumentierte Anfragen

Diese Bibliothek ist typisiert für bequemen Zugriff auf die dokumentierte API.

Wenn Sie auf undokumentierte Endpunkte, Parameter oder Antworteigenschaften zugreifen müssen, kann die Bibliothek dennoch verwendet werden.

#### Undokumentierte Endpunkte

Um Anfragen an undokumentierte Endpunkte zu senden, können Sie `client.get`, `client.post` und andere
HTTP-Verben verwenden. Client-Optionen werden bei dieser Anfrage berücksichtigt (z. B. Wiederholungsversuche).

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undokumentierte Anfrageparameter

Wenn Sie explizit einen zusätzlichen Parameter senden möchten, können Sie dies mit den Anfrageoptionen `extra_query`, `extra_body` und `extra_headers` tun.

#### Undokumentierte Antworteigenschaften

Um auf undokumentierte Antworteigenschaften zuzugreifen, können Sie auf die zusätzlichen Felder wie `response.unknown_prop` zugreifen. Sie
können auch alle zusätzlichen Felder im Pydantic-Modell als Dictionary mit
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra) abrufen.

### Konfiguration des HTTP-Clients

Sie können den [httpx-Client](https://www.python-httpx.org/api/#client) direkt überschreiben, um ihn für Ihren Anwendungsfall anzupassen, einschließlich:

- Unterstützung für [Proxies](https://www.python-httpx.org/advanced/proxies/)
- Benutzerdefinierte [Transports](https://www.python-httpx.org/advanced/transports/)
- Zusätzliche [erweiterte](https://www.python-httpx.org/advanced/clients/) Funktionalität

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

Sie können den Client auch pro Anfrage mit `with_options()` anpassen:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Verwaltung von HTTP-Ressourcen

Standardmäßig schließt die Bibliothek die zugrunde liegenden HTTP-Verbindungen, wenn der Client [vom Garbage Collector freigegeben](https://docs.python.org/3/reference/datamodel.html#object.__del__) wird. Sie können den Client bei Bedarf manuell mit der Methode `.close()` schließen oder mit einem Kontextmanager, der beim Verlassen schließt.

```py
from perplexity import Perplexity

with Perplexity() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versionierung

Dieses Paket folgt im Allgemeinen den [SemVer](https://semver.org/spec/v2.0.0.html)-Konventionen, obwohl bestimmte rückwärtsinkompatible Änderungen als Minor-Versionen veröffentlicht werden können:

1. Änderungen, die nur statische Typen betreffen, ohne das Laufzeitverhalten zu beeinträchtigen.
2. Änderungen an Bibliotheksinterna, die technisch öffentlich sind, aber nicht für die externe Nutzung vorgesehen oder dokumentiert sind. _(Bitte öffnen Sie ein GitHub-Issue, wenn Sie auf solche Interna angewiesen sind.)_
3. Änderungen, von denen wir nicht erwarten, dass sie die überwiegende Mehrheit der Benutzer in der Praxis betreffen.

Wir nehmen Rückwärtskompatibilität ernst und arbeiten daran, Ihnen ein reibungsloses Upgrade-Erlebnis zu bieten.

Wir freuen uns über Ihr Feedback; bitte öffnen Sie ein [Issue](https://www.github.com/perplexityai/perplexity-py/issues) mit Fragen, Fehlern oder Vorschlägen.

### Ermittlung der installierten Version

Wenn Sie auf die neueste Version aktualisiert haben, aber keine neuen Funktionen sehen, die Sie erwartet haben, verwendet Ihre Python-Umgebung wahrscheinlich noch eine ältere Version.

Sie können die zur Laufzeit verwendete Version wie folgt ermitteln:

```py
import perplexity
print(perplexity.__version__)
```

## Anforderungen

Python 3.9 oder höher.

## Mitwirken

Siehe [die Mitwirkungsdokumentation](./CONTRIBUTING.md).
