# @crawlora-org/gosugamers — GosuGamers API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted GosuGamers API.
It exposes 17 API endpoints for esports matches, results, tournaments, games, news, and articles through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-javascript-homepage). It does not run a browser or scrape GosuGamers locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by GosuGamers or its owners.

## Install

```sh
npm install @crawlora-org/gosugamers
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { GosuGamersClient } from "@crawlora-org/gosugamers";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new GosuGamersClient({ apiKey });
const result1 = await client.games({});
console.log(result1);
const result2 = await client.matches({});
console.log(result2);
```

The client also exports `Client` as an alias for `GosuGamersClient`. Operation
methods are available directly in camelCase and through the `gosugamers`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-gosugamers/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-gosugamers/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported GosuGamers API endpoints

This package exposes each route below as a direct method and through the `gosugamers` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-gosugamers/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
