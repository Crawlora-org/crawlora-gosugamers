# GosuGamers clients for Crawlora

Official Crawlora client packages for the hosted GosuGamers API. Access 17 API endpoints covering esports matches, results, tournaments, games, news, and articles from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape GosuGamers locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by GosuGamers or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/gosugamers`](javascript/README.md)
- Python: [`crawlora-gosugamers`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-gosugamers`](go.mod)
- Ruby: [`crawlora-gosugamers`](ruby/README.md)
- Java: [`net.crawlora:crawlora-gosugamers:0.1.0`](java/README.md)
- PHP: [`crawlora/gosugamers`](php/README.md)
- Rust: [`crawlora-gosugamers`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 17 selected public GosuGamers API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
