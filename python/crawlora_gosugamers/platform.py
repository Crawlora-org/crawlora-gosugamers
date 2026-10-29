"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class GosuGamersClient(CrawloraClient):
    """Synchronous GosuGamers API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-gosugamers-python/0.1.0')
        super().__init__(*args, **kwargs)

    def article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-article', params, response_type=response_type, timeout=timeout, headers=headers)

    def articles(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-articles', params, response_type=response_type, timeout=timeout, headers=headers)

    def encounters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-encounters', params, response_type=response_type, timeout=timeout, headers=headers)

    def games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-games', params, response_type=response_type, timeout=timeout, headers=headers)

    def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-match', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_game(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-match-game', params, response_type=response_type, timeout=timeout, headers=headers)

    def matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-player', params, response_type=response_type, timeout=timeout, headers=headers)

    def rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    def results(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-results', params, response_type=response_type, timeout=timeout, headers=headers)

    def stage_groups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-stage-groups', params, response_type=response_type, timeout=timeout, headers=headers)

    def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-team', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_results(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-team-results', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-tournament', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_participants(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-tournament-participants', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_talents(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-tournament-talents', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('gosugamers-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncGosuGamersClient(AsyncCrawloraClient):
    """Asynchronous GosuGamers API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-gosugamers-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-article', params, response_type=response_type, timeout=timeout, headers=headers)

    async def articles(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-articles', params, response_type=response_type, timeout=timeout, headers=headers)

    async def encounters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-encounters', params, response_type=response_type, timeout=timeout, headers=headers)

    async def games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-games', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-match', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_game(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-match-game', params, response_type=response_type, timeout=timeout, headers=headers)

    async def matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-player', params, response_type=response_type, timeout=timeout, headers=headers)

    async def rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def results(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-results', params, response_type=response_type, timeout=timeout, headers=headers)

    async def stage_groups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-stage-groups', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-team', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_results(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-team-results', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-tournament', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_participants(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-tournament-participants', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_talents(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-tournament-talents', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('gosugamers-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)
