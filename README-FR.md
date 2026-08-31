# Bibliothèque Python de l'API Perplexity

**Langues / Languages:** [English](./README.md) · [中文](./README-ZH.md) · [Español](./README-ES.md) · [Français](./README-FR.md) · [Português](./README-PT.md) · [Русский](./README-RU.md) · [Deutsch](./README-DE.md)

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/perplexityai.svg?label=pypi%20(stable))](https://pypi.org/project/perplexityai/)

La bibliothèque Python Perplexity offre un accès pratique à l'API REST Perplexity depuis toute application Python 3.9 ou supérieure. La bibliothèque inclut des définitions de types pour tous les paramètres de requête et les champs de réponse,
et propose des clients synchrones et asynchrones basés sur [httpx](https://github.com/encode/httpx).

Elle est générée avec [Stainless](https://www.stainless.com/).

## Documentation

La documentation de l'API REST se trouve sur [docs.perplexity.ai](https://docs.perplexity.ai/). L'API complète de cette bibliothèque est décrite dans [api.md](api.md).

## Installation

```sh
# install from PyPI
pip install perplexityai
```

## API de recherche

Obtenir des résultats de recherche web :

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

## Complétions de chat

L'API complète de cette bibliothèque est décrite dans [api.md](api.md).

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

Bien que vous puissiez fournir un argument nommé `api_key`,
nous recommandons d'utiliser [python-dotenv](https://pypi.org/project/python-dotenv/)
pour ajouter `PERPLEXITY_API_KEY="My API Key"` à votre fichier `.env`
afin que votre clé API ne soit pas stockée dans le contrôle de version.

## Utilisation asynchrone

Importez simplement `AsyncPerplexity` au lieu de `Perplexity` et utilisez `await` avec chaque appel API :

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

Les fonctionnalités des clients synchrones et asynchrones sont par ailleurs identiques.

### Avec aiohttp

Par défaut, le client asynchrone utilise `httpx` pour les requêtes HTTP. Cependant, pour de meilleures performances de concurrence, vous pouvez également utiliser `aiohttp` comme backend HTTP.

Vous pouvez l'activer en installant `aiohttp` :

```sh
# install from PyPI
pip install perplexityai[aiohttp]
```

Puis activez-le en instanciant le client avec `http_client=DefaultAioHttpClient()` :

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

## Réponses en streaming

Nous prenons en charge les réponses en streaming via Server Side Events (SSE).

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

Le client asynchrone utilise exactement la même interface.

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

## Utilisation des types

Les paramètres de requête imbriqués sont des [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Les réponses sont des [modèles Pydantic](https://docs.pydantic.dev) qui fournissent également des méthodes utilitaires pour :

- Sérialiser en JSON, `model.to_json()`
- Convertir en dictionnaire, `model.to_dict()`

Les requêtes et réponses typées offrent l'autocomplétion et la documentation dans votre éditeur. Si vous souhaitez voir les erreurs de type dans VS Code pour détecter les bugs plus tôt, définissez `python.analysis.typeCheckingMode` sur `basic`.

## Paramètres imbriqués

Les paramètres imbriqués sont des dictionnaires, typés avec `TypedDict`, par exemple :

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

## Gestion des erreurs

Lorsque la bibliothèque ne parvient pas à se connecter à l'API (par exemple, en raison de problèmes de connexion réseau ou d'un délai d'attente dépassé), une sous-classe de `perplexity.APIConnectionError` est levée.

Lorsque l'API renvoie un code d'état autre que le succès (c'est-à-dire une réponse 4xx ou 5xx),
une sous-classe de `perplexity.APIStatusError` est levée, contenant les propriétés `status_code` et `response`.

Toutes les erreurs héritent de `perplexity.APIError`.

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

Les codes d'erreur sont les suivants :

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

### Nouvelles tentatives

Certaines erreurs sont automatiquement réessayées 2 fois par défaut, avec un court backoff exponentiel.
Les erreurs de connexion (par exemple, dues à un problème de connectivité réseau), le délai d'attente 408 Request Timeout, le conflit 409 Conflict,
la limite de débit 429 Rate Limit et les erreurs internes >=500 sont toutes réessayées par défaut.

Vous pouvez utiliser l'option `max_retries` pour configurer ou désactiver les paramètres de nouvelle tentative :

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

### Délais d'attente

Par défaut, les requêtes expirent après 15 minutes. Vous pouvez configurer cela avec l'option `timeout`,
qui accepte un float ou un objet [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) :

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

En cas de dépassement du délai, une `APITimeoutError` est levée.

Notez que les requêtes qui expirent sont [réessayées deux fois par défaut](#nouvelles-tentatives).

## Avancé

### Journalisation

Nous utilisons le module standard [`logging`](https://docs.python.org/3/library/logging.html).

Vous pouvez activer la journalisation en définissant la variable d'environnement `PERPLEXITY_LOG` sur `info`.

```shell
$ export PERPLEXITY_LOG=info
```

Ou sur `debug` pour une journalisation plus verbeuse.

### Comment savoir si `None` signifie `null` ou absent

Dans une réponse API, un champ peut être explicitement `null`, ou totalement absent ; dans les deux cas, sa valeur est `None` dans cette bibliothèque. Vous pouvez distinguer les deux cas avec `.model_fields_set` :

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accès aux données brutes de la réponse (p. ex. en-têtes)

L'objet Response « brut » est accessible en préfixant `.with_raw_response.` à tout appel de méthode HTTP, par exemple :

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

Ces méthodes renvoient un objet [`APIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py).

Le client asynchrone renvoie un [`AsyncAPIResponse`](https://github.com/perplexityai/perplexity-py/tree/main/src/perplexity/_response.py) avec la même structure, la seule différence étant des méthodes `await` pour lire le contenu de la réponse.

#### `.with_streaming_response`

L'interface ci-dessus lit intégralement le corps de la réponse lors de la requête, ce qui n'est pas toujours souhaitable.

Pour streamer le corps de la réponse, utilisez plutôt `.with_streaming_response`, qui nécessite un gestionnaire de contexte et ne lit le corps de la réponse qu'une fois que vous appelez `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` ou `.parse()`. Dans le client asynchrone, ce sont des méthodes async.

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

Le gestionnaire de contexte est requis pour que la réponse soit fermée de manière fiable.

### Requêtes personnalisées ou non documentées

Cette bibliothèque est typée pour un accès pratique à l'API documentée.

Si vous devez accéder à des points de terminaison, paramètres ou propriétés de réponse non documentés, la bibliothèque reste utilisable.

#### Points de terminaison non documentés

Pour faire des requêtes vers des points de terminaison non documentés, vous pouvez utiliser `client.get`, `client.post` et d'autres
verbes HTTP. Les options du client seront respectées (comme les nouvelles tentatives) lors de cette requête.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Paramètres de requête non documentés

Si vous souhaitez envoyer explicitement un paramètre supplémentaire, vous pouvez le faire avec les options de requête `extra_query`, `extra_body` et `extra_headers`.

#### Propriétés de réponse non documentées

Pour accéder aux propriétés de réponse non documentées, vous pouvez accéder aux champs supplémentaires comme `response.unknown_prop`. Vous
pouvez également obtenir tous les champs supplémentaires du modèle Pydantic sous forme de dictionnaire avec
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuration du client HTTP

Vous pouvez directement remplacer le [client httpx](https://www.python-httpx.org/api/#client) pour l'adapter à votre cas d'usage, notamment :

- Prise en charge des [proxies](https://www.python-httpx.org/advanced/proxies/)
- [Transports](https://www.python-httpx.org/advanced/transports/) personnalisés
- Fonctionnalités [avancées](https://www.python-httpx.org/advanced/clients/) supplémentaires

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

Vous pouvez également personnaliser le client par requête avec `with_options()` :

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Gestion des ressources HTTP

Par défaut, la bibliothèque ferme les connexions HTTP sous-jacentes lorsque le client est [collecté par le ramasse-miettes](https://docs.python.org/3/reference/datamodel.html#object.__del__). Vous pouvez fermer manuellement le client avec la méthode `.close()` si vous le souhaitez, ou avec un gestionnaire de contexte qui ferme à la sortie.

```py
from perplexity import Perplexity

with Perplexity() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versionnement

Ce package suit généralement les conventions [SemVer](https://semver.org/spec/v2.0.0.html), bien que certains changements rétro-incompatibles puissent être publiés en versions mineures :

1. Changements qui n'affectent que les types statiques, sans casser le comportement à l'exécution.
2. Changements aux internes de la bibliothèque qui sont techniquement publics mais non destinés ni documentés pour un usage externe. _(Veuillez ouvrir une issue GitHub pour nous indiquer si vous vous appuyez sur ces internes.)_
3. Changements que nous n'attendons pas impacter la grande majorité des utilisateurs en pratique.

Nous prenons la rétrocompatibilité au sérieux et travaillons dur pour que vous puissiez compter sur une mise à niveau fluide.

Vos retours nous intéressent ; ouvrez une [issue](https://www.github.com/perplexityai/perplexity-py/issues) pour des questions, des bugs ou des suggestions.

### Déterminer la version installée

Si vous avez mis à jour vers la dernière version mais ne voyez pas les nouvelles fonctionnalités attendues, votre environnement Python utilise probablement encore une version plus ancienne.

Vous pouvez déterminer la version utilisée à l'exécution avec :

```py
import perplexity
print(perplexity.__version__)
```

## Prérequis

Python 3.9 ou supérieur.

## Contribution

Voir [la documentation de contribution](./CONTRIBUTING.md).
