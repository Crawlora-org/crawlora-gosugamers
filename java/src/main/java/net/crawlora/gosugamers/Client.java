package net.crawlora.gosugamers;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the GosuGamers endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 17;
    public static final List<String> OPERATION_IDS = List.of(
            "gosugamers-article",
            "gosugamers-articles",
            "gosugamers-encounters",
            "gosugamers-games",
            "gosugamers-match",
            "gosugamers-match-game",
            "gosugamers-matches",
            "gosugamers-player",
            "gosugamers-rankings",
            "gosugamers-results",
            "gosugamers-stage-groups",
            "gosugamers-team",
            "gosugamers-team-results",
            "gosugamers-tournament",
            "gosugamers-tournament-participants",
            "gosugamers-tournament-talents",
            "gosugamers-tournaments"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("gosugamers-article", new Operation("gosugamers-article", "GET", "/gosugamers/article", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-articles", new Operation("gosugamers-articles", "GET", "/gosugamers/articles", Map.ofEntries(Map.entry("section", new Param("section", "query", false, "string", List.of("dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india", "entertainment", "genshin-impact", "honkai-star-rail", "zenless-zone-zero", "honor-of-kings", "umamusume-pretty-derby"), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("news", "features"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("page_size", new Param("page_size", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-encounters", new Operation("gosugamers-encounters", "GET", "/gosugamers/encounters", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"), "csv")), Map.entry("match_id", new Param("match_id", "query", true, "string", List.of(), "csv")), Map.entry("team1_id", new Param("team1_id", "query", true, "string", List.of(), "csv")), Map.entry("team2_id", new Param("team2_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-games", new Operation("gosugamers-games", "GET", "/gosugamers/games", Map.of(), List.of("application/json")));
        operations.put("gosugamers-match", new Operation("gosugamers-match", "GET", "/gosugamers/match", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"), "csv")), Map.entry("tournament_id", new Param("tournament_id", "query", true, "string", List.of(), "csv")), Map.entry("match_id", new Param("match_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-match-game", new Operation("gosugamers-match-game", "GET", "/gosugamers/match-game", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-matches", new Operation("gosugamers-matches", "GET", "/gosugamers/matches", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("page_size", new Param("page_size", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-player", new Operation("gosugamers-player", "GET", "/gosugamers/player", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"), "csv")), Map.entry("player_id", new Param("player_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-rankings", new Operation("gosugamers-rankings", "GET", "/gosugamers/rankings", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"), "csv")), Map.entry("region_id", new Param("region_id", "query", false, "integer", List.of(), "csv")), Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("page_size", new Param("page_size", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-results", new Operation("gosugamers-results", "GET", "/gosugamers/results", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("page_size", new Param("page_size", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-stage-groups", new Operation("gosugamers-stage-groups", "GET", "/gosugamers/stage-groups", Map.ofEntries(Map.entry("tournament_id", new Param("tournament_id", "query", true, "string", List.of(), "csv")), Map.entry("stage_id", new Param("stage_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-team", new Operation("gosugamers-team", "GET", "/gosugamers/team", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"), "csv")), Map.entry("team_id", new Param("team_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-team-results", new Operation("gosugamers-team-results", "GET", "/gosugamers/team-results", Map.ofEntries(Map.entry("team_id", new Param("team_id", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("page_size", new Param("page_size", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-tournament", new Operation("gosugamers-tournament", "GET", "/gosugamers/tournament", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"), "csv")), Map.entry("tournament_id", new Param("tournament_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-tournament-participants", new Operation("gosugamers-tournament-participants", "GET", "/gosugamers/tournament-participants", Map.ofEntries(Map.entry("game", new Param("game", "query", true, "string", List.of("dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"), "csv")), Map.entry("tournament_id", new Param("tournament_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-tournament-talents", new Operation("gosugamers-tournament-talents", "GET", "/gosugamers/tournament-talents", Map.ofEntries(Map.entry("tournament_id", new Param("tournament_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("gosugamers-tournaments", new Operation("gosugamers-tournaments", "GET", "/gosugamers/tournaments", Map.ofEntries(Map.entry("game", new Param("game", "query", false, "string", List.of("dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"), "csv")), Map.entry("state", new Param("state", "query", false, "string", List.of("all", "ongoing", "upcoming", "past"), "csv")), Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("page_size", new Param("page_size", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown GosuGamers operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object article(Map<String, ?> params) { return request("gosugamers-article", params); }
    public Object articles(Map<String, ?> params) { return request("gosugamers-articles", params); }
    public Object encounters(Map<String, ?> params) { return request("gosugamers-encounters", params); }
    public Object games(Map<String, ?> params) { return request("gosugamers-games", params); }
    public Object match(Map<String, ?> params) { return request("gosugamers-match", params); }
    public Object matchGame(Map<String, ?> params) { return request("gosugamers-match-game", params); }
    public Object matches(Map<String, ?> params) { return request("gosugamers-matches", params); }
    public Object player(Map<String, ?> params) { return request("gosugamers-player", params); }
    public Object rankings(Map<String, ?> params) { return request("gosugamers-rankings", params); }
    public Object results(Map<String, ?> params) { return request("gosugamers-results", params); }
    public Object stageGroups(Map<String, ?> params) { return request("gosugamers-stage-groups", params); }
    public Object team(Map<String, ?> params) { return request("gosugamers-team", params); }
    public Object teamResults(Map<String, ?> params) { return request("gosugamers-team-results", params); }
    public Object tournament(Map<String, ?> params) { return request("gosugamers-tournament", params); }
    public Object tournamentParticipants(Map<String, ?> params) { return request("gosugamers-tournament-participants", params); }
    public Object tournamentTalents(Map<String, ?> params) { return request("gosugamers-tournament-talents", params); }
    public Object tournaments(Map<String, ?> params) { return request("gosugamers-tournaments", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
