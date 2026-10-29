require "json"
require "net/http"
require "uri"

module Crawlora
  module Gosugamers
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"gosugamers-article": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-article", "method": "GET", "params": [{"description": "Numeric article id from gosugamers-articles", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "79434"}], "path": "/gosugamers/article", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-articles": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-articles", "method": "GET", "params": [{"description": "Article section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india, entertainment, genshin-impact, honkai-star-rail, zenless-zone-zero, honor-of-kings, umamusume-pretty-derby; omit for all", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india", "entertainment", "genshin-impact", "honkai-star-rail", "zenless-zone-zero", "honor-of-kings", "umamusume-pretty-derby"], "in": "query", "name": "section", "type": "string"}, {"description": "Article type; one of news, features; omit for both", "enum": ["news", "features"], "in": "query", "name": "type", "type": "string"}, {"description": "1-based page; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/articles", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india", "entertainment", "genshin-impact", "honkai-star-rail", "zenless-zone-zero", "honor-of-kings", "umamusume-pretty-derby"], "in": "query", "name": "section", "type": "string"}, {"enum": ["news", "features"], "in": "query", "name": "type", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "gosugamers-encounters": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-encounters", "method": "GET", "params": [{"description": "Game section of the match; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"description": "Numeric id of the match whose other meetings are wanted; that match is left out", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "660816"}, {"description": "Numeric id of the first team", "in": "query", "name": "team1_id", "required": true, "type": "string", "x-example": "38335"}, {"description": "Numeric id of the second team", "in": "query", "name": "team2_id", "required": true, "type": "string", "x-example": "37547"}], "path": "/gosugamers/encounters", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "match_id", "required": true, "type": "string"}, {"in": "query", "name": "team1_id", "required": true, "type": "string"}, {"in": "query", "name": "team2_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-games": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-games", "method": "GET", "params": [], "path": "/gosugamers/games", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "gosugamers-match": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-match", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "dota2"}, {"description": "Numeric tournament id from gosugamers-matches or gosugamers-results (tournament.id)", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "63208"}, {"description": "Numeric match id from gosugamers-matches or gosugamers-results (id)", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "663299"}], "path": "/gosugamers/match", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "match_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-match-game": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-match-game", "method": "GET", "params": [{"description": "Numeric game id from the games list of gosugamers-match", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "1361936"}], "path": "/gosugamers/match-game", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-matches": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-matches", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india; omit for all games", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"description": "1-based page; page 1 with the default size is read from the public page, any other page or size from the site's JSON API; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "gosugamers-player": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-player", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "dota2"}, {"description": "Numeric player id from gosugamers-team (roster[].id)", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "368742"}], "path": "/gosugamers/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "player_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-rankings": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-rankings", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"description": "Ranking region id from the regions list of the response; 0 is Global; defaults to 0", "in": "query", "minimum": 0, "name": "region_id", "type": "integer"}, {"description": "Team name prefix, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "Te"}, {"description": "1-based page; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "region_id", "type": "integer"}, {"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "gosugamers-results": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-results", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india; omit for all games", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"description": "1-based page; page 1 with the default size is read from the public page, any other page or size from the site's JSON API; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/results", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "gosugamers-stage-groups": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-stage-groups", "method": "GET", "params": [{"description": "Numeric tournament id from gosugamers-tournaments or gosugamers-matches", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "63147"}, {"description": "Numeric stage id (stages[].id) from gosugamers-tournament", "in": "query", "name": "stage_id", "required": true, "type": "string", "x-example": "28413"}], "path": "/gosugamers/stage-groups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "stage_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-team": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-team", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "dota2"}, {"description": "Numeric team id from gosugamers-matches, gosugamers-results or gosugamers-match (teams[].id)", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "51203"}], "path": "/gosugamers/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "team_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-team-results": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-team-results", "method": "GET", "params": [{"description": "Numeric team id from gosugamers-rankings, gosugamers-results or gosugamers-team", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "37547"}, {"description": "1-based page; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/team-results", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "team_id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "gosugamers-tournament": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-tournament", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string", "x-example": "dota2"}, {"description": "Numeric tournament id from gosugamers-matches or gosugamers-results (tournament.id)", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "63208"}], "path": "/gosugamers/tournament", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-tournament-participants": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-tournament-participants", "method": "GET", "params": [{"description": "Game section of the tournament; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"description": "Numeric tournament id from gosugamers-tournaments, gosugamers-matches or gosugamers-results", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "63147"}], "path": "/gosugamers/tournament-participants", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-tournament-talents": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-tournament-talents", "method": "GET", "params": [{"description": "Numeric tournament id from gosugamers-tournaments, gosugamers-matches or gosugamers-results", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "63147"}], "path": "/gosugamers/tournament-talents", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "gosugamers-tournaments": {"bodyParam": null, "bodyRequired": false, "id": "gosugamers-tournaments", "method": "GET", "params": [{"description": "Game section; one of dota2, counterstrike, lol, valorant, mobile-legends, pubg-mobile, wild-rift, free-fire, battlegrounds-mobile-india; omit for all games", "enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"description": "Tournament state; one of all, ongoing, upcoming, past; defaults to all", "enum": ["all", "ongoing", "upcoming", "past"], "in": "query", "name": "state", "type": "string"}, {"description": "Tournament name prefix, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "VCT"}, {"description": "1-based page; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size, 1 to 100; defaults to 10", "in": "query", "maximum": 100, "minimum": 1, "name": "page_size", "type": "integer"}], "path": "/gosugamers/tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["dota2", "counterstrike", "lol", "valorant", "mobile-legends", "pubg-mobile", "wild-rift", "free-fire", "battlegrounds-mobile-india"], "in": "query", "name": "game", "type": "string"}, {"enum": ["all", "ongoing", "upcoming", "past"], "in": "query", "name": "state", "type": "string"}, {"in": "query", "name": "q", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "page_size", "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["gosugamers-article", "gosugamers-articles", "gosugamers-encounters", "gosugamers-games", "gosugamers-match", "gosugamers-match-game", "gosugamers-matches", "gosugamers-player", "gosugamers-rankings", "gosugamers-results", "gosugamers-stage-groups", "gosugamers-team", "gosugamers-team-results", "gosugamers-tournament", "gosugamers-tournament-participants", "gosugamers-tournament-talents", "gosugamers-tournaments"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-gosugamers-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('article') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-article', params, response_type: response_type)
      end
      define_method('articles') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-articles', params, response_type: response_type)
      end
      define_method('encounters') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-encounters', params, response_type: response_type)
      end
      define_method('games') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-games', params, response_type: response_type)
      end
      define_method('match') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-match', params, response_type: response_type)
      end
      define_method('match_game') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-match-game', params, response_type: response_type)
      end
      define_method('matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-matches', params, response_type: response_type)
      end
      define_method('player') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-player', params, response_type: response_type)
      end
      define_method('rankings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-rankings', params, response_type: response_type)
      end
      define_method('results') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-results', params, response_type: response_type)
      end
      define_method('stage_groups') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-stage-groups', params, response_type: response_type)
      end
      define_method('team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-team', params, response_type: response_type)
      end
      define_method('team_results') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-team-results', params, response_type: response_type)
      end
      define_method('tournament') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-tournament', params, response_type: response_type)
      end
      define_method('tournament_participants') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-tournament-participants', params, response_type: response_type)
      end
      define_method('tournament_talents') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-tournament-talents', params, response_type: response_type)
      end
      define_method('tournaments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('gosugamers-tournaments', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
