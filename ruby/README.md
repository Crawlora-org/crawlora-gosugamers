# Crawlora GosuGamers API client for Ruby (`crawlora-gosugamers`)

This Ruby gem calls Crawlora's hosted GosuGamers API at `https://api.crawlora.net/api/v1`. It exposes 17 endpoints covering esports matches, results, tournaments, games, news, and articles; it does not call or scrape GosuGamers directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-gosugamers"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/gosugamers"

client = Crawlora::Gosugamers::Client.new
result = client.request("gosugamers-article", JSON.parse("{\"id\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 17 API operations.

```ruby
client = Crawlora::Gosugamers::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported GosuGamers API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-gosugamers/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-gosugamers) for account setup, the API operation reference, and release history.
