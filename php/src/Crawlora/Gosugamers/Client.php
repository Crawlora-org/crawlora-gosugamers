<?php

declare(strict_types=1);

namespace Crawlora\Gosugamers;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'gosugamers';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 17;
    public const OPERATION_IDS = ["gosugamers-article", "gosugamers-articles", "gosugamers-encounters", "gosugamers-games", "gosugamers-match", "gosugamers-match-game", "gosugamers-matches", "gosugamers-player", "gosugamers-rankings", "gosugamers-results", "gosugamers-stage-groups", "gosugamers-team", "gosugamers-team-results", "gosugamers-tournament", "gosugamers-tournament-participants", "gosugamers-tournament-talents", "gosugamers-tournaments"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"gosugamers-article": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-article", "method": "GET", "params": [{"description": "Numeric article id from gosugamers-articles", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "79434"}], "path": "/gosugamers/article", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-articles": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-articles", "method": "GET", "params": [{"description": "Article section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india, entertainment, genshin-impact, honkai-star-rail, zenless-zone-zero, honor-of-kings, umamusume-pretty-derby; omit for all", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india", "entertainment", "genshin-impact", "honkai-star-rail", "zenless-zone-zero", "honor-of-kings", "umamusume-pretty-derby"], "in": "query", "name": "section", "type": "string"}, {"description": "Article type; one of news, features; omit for both", "enum": ["news", "features"], "in": "query", "name": "type", "type": "string"}, {"description": "1-based page; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/articles", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india", "entertainment", "genshin-impact", "honkai-star-rail", "zenless-zone-zero", "honor-of-kings", "umamusume-pretty-derby"], "in": "query", "name": "section", "type": "string"}, {"enum": ["news", "features"], "in": "query", "name": "type", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "gosugamers-encounters": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-encounters", "method": "GET", "params": [{"description": "Game section of the match; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"description": "Numeric id of the match whose other meetings are wanted; that match is left out", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "660816"}, {"description": "Numeric id of the first team", "in": "query", "name": "team1_id", "required": true, "type": "string", "x-example": "38335"}, {"description": "Numeric id of the second team", "in": "query", "name": "team2_id", "required": true, "type": "string", "x-example": "37547"}], "path": "/gosugamers/encounters", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "match_id", "required": true, "type": "string"}, {"in": "query", "name": "team1_id", "required": true, "type": "string"}, {"in": "query", "name": "team2_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-games": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-games", "method": "GET", "params": [], "path": "/gosugamers/games", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "gosugamers-match": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-match", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "dota2"}, {"description": "Numeric tournament id from gosugamers-matches or gosugamers-results (tournament.id)", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "63208"}, {"description": "Numeric match id from gosugamers-matches or gosugamers-results (id)", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "663299"}], "path": "/gosugamers/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "match_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-match-game": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-match-game", "method": "GET", "params": [{"description": "Numeric game id from the games list of gosugamers-match", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "1361936"}], "path": "/gosugamers/match-game", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-matches": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-matches", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india; omit for all games", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"description": "1-based page; page 1 with the default size is read from the public page, any other page or size from the site's JSON API; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "gosugamers-player": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-player", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "dota2"}, {"description": "Numeric player id from gosugamers-team (roster[].id)", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "368742"}], "path": "/gosugamers/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "player_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-rankings": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-rankings", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"description": "Ranking region id from the regions list of the response; 0 is Global; defaults to 0", "in": "query", "minimum": 0, "name": "region_id", "type": "integer"}, {"description": "Team name prefix, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "Te"}, {"description": "1-based page; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "region_id", "type": "integer"}, {"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "gosugamers-results": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-results", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india; omit for all games", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"description": "1-based page; page 1 with the default size is read from the public page, any other page or size from the site's JSON API; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/results", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "gosugamers-stage-groups": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-stage-groups", "method": "GET", "params": [{"description": "Numeric tournament id from gosugamers-tournaments or gosugamers-matches", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "63147"}, {"description": "Numeric stage id (stages[].id) from gosugamers-tournament", "in": "query", "name": "stage_id", "required": true, "type": "string", "x-example": "28413"}], "path": "/gosugamers/stage-groups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "stage_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-team": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-team", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "dota2"}, {"description": "Numeric team id from gosugamers-matches, gosugamers-results or gosugamers-match (teams[].id)", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "51203"}], "path": "/gosugamers/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "team_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-team-results": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-team-results", "method": "GET", "params": [{"description": "Numeric team id from gosugamers-rankings, gosugamers-results or gosugamers-team", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "37547"}, {"description": "1-based page; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/team-results", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "gosugamers-tournament": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-tournament", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "dota2"}, {"description": "Numeric tournament id from gosugamers-matches or gosugamers-results (tournament.id)", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "63208"}], "path": "/gosugamers/tournament", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-tournament-participants": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-tournament-participants", "method": "GET", "params": [{"description": "Game section of the tournament; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"description": "Numeric tournament id from gosugamers-tournaments, gosugamers-matches or gosugamers-results", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "63147"}], "path": "/gosugamers/tournament-participants", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-tournament-talents": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-tournament-talents", "method": "GET", "params": [{"description": "Numeric tournament id from gosugamers-tournaments, gosugamers-matches or gosugamers-results", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "63147"}], "path": "/gosugamers/tournament-talents", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-tournaments": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-tournaments", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india; omit for all games", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"description": "Tournament state; one of all, ongoing, upcoming, past; defaults to all", "enum": ["all", "ongoing", "upcoming", "past"], "in": "query", "name": "state", "type": "string"}, {"description": "Tournament name prefix, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "VCT"}, {"description": "1-based page; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"enum": ["all", "ongoing", "upcoming", "past"], "in": "query", "name": "state", "type": "string"}, {"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-gosugamers-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function article(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-article", $params, $responseType);
    }
    public function articles(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-articles", $params, $responseType);
    }
    public function encounters(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-encounters", $params, $responseType);
    }
    public function games(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-games", $params, $responseType);
    }
    public function match(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-match", $params, $responseType);
    }
    public function match_game(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-match-game", $params, $responseType);
    }
    public function matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-matches", $params, $responseType);
    }
    public function player(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-player", $params, $responseType);
    }
    public function rankings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-rankings", $params, $responseType);
    }
    public function results(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-results", $params, $responseType);
    }
    public function stage_groups(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-stage-groups", $params, $responseType);
    }
    public function team(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-team", $params, $responseType);
    }
    public function team_results(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-team-results", $params, $responseType);
    }
    public function tournament(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-tournament", $params, $responseType);
    }
    public function tournament_participants(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-tournament-participants", $params, $responseType);
    }
    public function tournament_talents(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-tournament-talents", $params, $responseType);
    }
    public function tournaments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("gosugamers-tournaments", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
