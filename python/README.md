# crawlora-gosugamers — GosuGamers API client for Python

Python client for Crawlora's hosted GosuGamers API. It exposes 17 API endpoints covering esports matches, results, tournaments, games, news, and articles. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-python-homepage); the package does not run a browser or scrape
GosuGamers locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
GosuGamers or its owners.

## Install

```sh
python -m pip install crawlora-gosugamers
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_gosugamers import GosuGamersClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with GosuGamersClient(api_key=api_key) as client:
    result_1 = client.games()
    print(result_1)
    result_2 = client.matches()
    print(result_2)
```

The package also exports `Client` as an alias for `GosuGamersClient`. Operation
methods are available directly in snake_case and through the `gosugamers`
group. The async package client is `AsyncGosuGamersClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-gosugamers/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-gosugamers/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_gosugamers import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.games()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-gosugamers/blob/main/examples/python.py) for a complete usage example.

## Supported GosuGamers API endpoints

This package exposes every route below through direct snake_case methods and the `gosugamers` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-gosugamers/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/gosugamers/article` | `gosugamers-article` | GosuGamers article |
| `GET` | `/gosugamers/articles` | `gosugamers-articles` | GosuGamers news and features archive |
| `GET` | `/gosugamers/encounters` | `gosugamers-encounters` | GosuGamers head-to-head meetings |
| `GET` | `/gosugamers/games` | `gosugamers-games` | GosuGamers game sections |
| `GET` | `/gosugamers/match` | `gosugamers-match` | GosuGamers esports match detail |
| `GET` | `/gosugamers/match-game` | `gosugamers-match-game` | GosuGamers single game (map) of a match |
| `GET` | `/gosugamers/matches` | `gosugamers-matches` | GosuGamers upcoming and live esports matches |
| `GET` | `/gosugamers/player` | `gosugamers-player` | GosuGamers esports player profile |
| `GET` | `/gosugamers/rankings` | `gosugamers-rankings` | GosuGamers team rankings |
| `GET` | `/gosugamers/results` | `gosugamers-results` | GosuGamers recent esports match results |
| `GET` | `/gosugamers/stage-groups` | `gosugamers-stage-groups` | GosuGamers tournament stage groups |
| `GET` | `/gosugamers/team` | `gosugamers-team` | GosuGamers esports team profile |
| `GET` | `/gosugamers/team-results` | `gosugamers-team-results` | GosuGamers team match history |
| `GET` | `/gosugamers/tournament` | `gosugamers-tournament` | GosuGamers esports tournament detail |
| `GET` | `/gosugamers/tournament-participants` | `gosugamers-tournament-participants` | GosuGamers tournament participants |
| `GET` | `/gosugamers/tournament-talents` | `gosugamers-tournament-talents` | GosuGamers tournament broadcast talents |
| `GET` | `/gosugamers/tournaments` | `gosugamers-tournaments` | GosuGamers esports tournament directory |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
