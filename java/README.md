# Crawlora GosuGamers API client for Java

The official Java client for Crawlora's hosted GosuGamers API. It exposes 17 endpoints covering esports matches, results, tournaments, games, news, and articles. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-gosugamers</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-java-console) to get an API key.

```java
import net.crawlora.gosugamers.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.games(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported GosuGamers API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-gosugamers/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-gosugamers)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=gosugamers-java-api-docs)
