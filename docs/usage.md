# GosuGamers API endpoint reference and client usage

This reference lists all 17 public GosuGamers API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/gosugamers`, `crawlora-gosugamers`, and `crawlora-gosugamers` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape GosuGamers locally; Crawlora is independent from and not endorsed by GosuGamers or its owners.

The package tracks the public API contract revision `sha256:de5fed9f9e96ee896300f2d020f44d15ab18d3f5c885548c7cf5a6ef6a90df3d` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `gosugamers`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `article` | `article` | `gosugamers.article` | `GET /gosugamers/article` | `id` (query, required) | GosuGamers article |
| `articles` | `articles` | `gosugamers.articles` | `GET /gosugamers/articles` | `section` (query, optional; values: `dota2`, `counterstrike`, `lol`, `valorant`, `mobile-legends`, `pubg-mobile`, `wild-rift`, `free-fire`, `battlegrounds-mobile-india`, `entertainment`, `genshin-impact`, `honkai-star-rail`, `zenless-zone-zero`, `honor-of-kings`, `umamusume-pretty-derby`), `type` (query, optional; values: `news`, `features`), `page` (query, optional), `page_size` (query, optional) | GosuGamers news and features archive |
| `encounters` | `encounters` | `gosugamers.encounters` | `GET /gosugamers/encounters` | `game` (query, required; values: `dota2`, `counterstrike`, `lol`, `valorant`, `mobile-legends`, `pubg-mobile`, `wild-rift`, `free-fire`, `battlegrounds-mobile-india`), `match_id` (query, required), `team1_id` (query, required), `team2_id` (query, required) | GosuGamers head-to-head meetings |
| `games` | `games` | `gosugamers.games` | `GET /gosugamers/games` | — | GosuGamers game sections |
| `match` | `match` | `gosugamers.match_` | `GET /gosugamers/match` | `game` (query, required; values: `dota2`, `counterstrike`, `lol`, `valorant`, `mobile-legends`, `pubg-mobile`, `wild-rift`, `free-fire`, `battlegrounds-mobile-india`), `tournament_id` (query, required), `match_id` (query, required) | GosuGamers esports match detail |
| `matches` | `matches` | `gosugamers.matches` | `GET /gosugamers/matches` | `game` (query, optional; values: `dota2`, `counterstrike`, `lol`, `valorant`, `mobile-legends`, `pubg-mobile`, `wild-rift`, `free-fire`, `battlegrounds-mobile-india`), `page` (query, optional), `page_size` (query, optional) | GosuGamers upcoming and live esports matches |
| `matchGame` | `match_game` | `gosugamers.match_game` | `GET /gosugamers/match-game` | `game_id` (query, required) | GosuGamers single game (map) of a match |
| `player` | `player` | `gosugamers.player` | `GET /gosugamers/player` | `game` (query, required; values: `dota2`, `counterstrike`, `lol`, `valorant`, `mobile-legends`, `pubg-mobile`, `wild-rift`, `free-fire`, `battlegrounds-mobile-india`), `player_id` (query, required) | GosuGamers esports player profile |
| `rankings` | `rankings` | `gosugamers.rankings` | `GET /gosugamers/rankings` | `game` (query, required; values: `dota2`, `counterstrike`, `lol`, `valorant`, `mobile-legends`, `pubg-mobile`, `wild-rift`, `free-fire`, `battlegrounds-mobile-india`), `region_id` (query, optional), `q` (query, optional), `page` (query, optional), `page_size` (query, optional) | GosuGamers team rankings |
| `results` | `results` | `gosugamers.results` | `GET /gosugamers/results` | `game` (query, optional; values: `dota2`, `counterstrike`, `lol`, `valorant`, `mobile-legends`, `pubg-mobile`, `wild-rift`, `free-fire`, `battlegrounds-mobile-india`), `page` (query, optional), `page_size` (query, optional) | GosuGamers recent esports match results |
| `stageGroups` | `stage_groups` | `gosugamers.stage_groups` | `GET /gosugamers/stage-groups` | `tournament_id` (query, required), `stage_id` (query, required) | GosuGamers tournament stage groups |
| `team` | `team` | `gosugamers.team` | `GET /gosugamers/team` | `game` (query, required; values: `dota2`, `counterstrike`, `lol`, `valorant`, `mobile-legends`, `pubg-mobile`, `wild-rift`, `free-fire`, `battlegrounds-mobile-india`), `team_id` (query, required) | GosuGamers esports team profile |
| `teamResults` | `team_results` | `gosugamers.team_results` | `GET /gosugamers/team-results` | `team_id` (query, required), `page` (query, optional), `page_size` (query, optional) | GosuGamers team match history |
| `tournament` | `tournament` | `gosugamers.tournament` | `GET /gosugamers/tournament` | `game` (query, required; values: `dota2`, `counterstrike`, `lol`, `valorant`, `mobile-legends`, `pubg-mobile`, `wild-rift`, `free-fire`, `battlegrounds-mobile-india`), `tournament_id` (query, required) | GosuGamers esports tournament detail |
| `tournamentParticipants` | `tournament_participants` | `gosugamers.tournament_participants` | `GET /gosugamers/tournament-participants` | `game` (query, required; values: `dota2`, `counterstrike`, `lol`, `valorant`, `mobile-legends`, `pubg-mobile`, `wild-rift`, `free-fire`, `battlegrounds-mobile-india`), `tournament_id` (query, required) | GosuGamers tournament participants |
| `tournaments` | `tournaments` | `gosugamers.tournaments` | `GET /gosugamers/tournaments` | `game` (query, optional; values: `dota2`, `counterstrike`, `lol`, `valorant`, `mobile-legends`, `pubg-mobile`, `wild-rift`, `free-fire`, `battlegrounds-mobile-india`), `state` (query, optional; values: `all`, `ongoing`, `upcoming`, `past`), `q` (query, optional), `page` (query, optional), `page_size` (query, optional) | GosuGamers esports tournament directory |
| `tournamentTalents` | `tournament_talents` | `gosugamers.tournament_talents` | `GET /gosugamers/tournament-talents` | `tournament_id` (query, required) | GosuGamers tournament broadcast talents |

## Client forms

- JavaScript: import `GosuGamersClient` (also exported as `Client`) from `@crawlora-org/gosugamers`; use `new GosuGamersClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `GosuGamersClient` (also exported as `Client`) from `crawlora_gosugamers`; use `with GosuGamersClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncGosuGamersClient`, used with `async with` and `await`.
- Rust: add `crawlora-gosugamers` with Cargo; import `Client` and the generated operation parameter struct, then call `client.gosugamers.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-gosugamers/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
