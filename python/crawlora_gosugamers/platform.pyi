from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelGosugamersTournamentsResponse = TypedDict('ModelGosugamersTournamentsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'q': NotRequired[str],
    'source_url': NotRequired[str],
    'state': NotRequired[Literal['all', 'ongoing', 'upcoming', 'past']],
    'total_pages': NotRequired[int],
    'total_rows': NotRequired[int],
    'tournaments': NotRequired[list[ModelGosugamersTournamentRow]],
}, total=False)

ModelGosugamersTournamentRow = TypedDict('ModelGosugamersTournamentRow', {
    'featured': NotRequired[bool],
    'game': NotRequired[str],
    'game_name': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'participant_count': NotRequired[int],
    'prize_currency': NotRequired[str],
    'prize_pool': NotRequired[float],
    'prize_pool_usd': NotRequired[float],
    'slug': NotRequired[str],
    'start_time': NotRequired[str],
    'status': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelGosugamersTournamentTalentsResponse = TypedDict('ModelGosugamersTournamentTalentsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'talents': NotRequired[list[ModelGosugamersBroadcastTalent]],
    'tournament_id': NotRequired[str],
}, total=False)

ModelGosugamersBroadcastTalent = TypedDict('ModelGosugamersBroadcastTalent', {
    'country_code': NotRequired[str],
    'country_name': NotRequired[str],
    'game': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'language_code': NotRequired[str],
    'name': NotRequired[str],
    'roles': NotRequired[list[str]],
    'slug': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelGosugamersTournamentParticipantsResponse = TypedDict('ModelGosugamersTournamentParticipantsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'participants': NotRequired[list[ModelGosugamersParticipant]],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[str],
}, total=False)

ModelGosugamersParticipant = TypedDict('ModelGosugamersParticipant', {
    'country_code': NotRequired[str],
    'country_name': NotRequired[str],
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'ranking': NotRequired[int],
    'slug': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelGosugamersTournamentDetail = TypedDict('ModelGosugamersTournamentDetail', {
    'country': NotRequired[str],
    'description': NotRequired[str],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'game_name': NotRequired[str],
    'image_url': NotRequired[str],
    'lan': NotRequired[bool],
    'prize_pool_usd': NotRequired[float],
    'source_url': NotRequired[str],
    'sponsors': NotRequired[list[str]],
    'stages': NotRequired[list[ModelGosugamersStageInfo]],
    'start_time': NotRequired[str],
    'status': NotRequired[str],
    'tournament': NotRequired[ModelGosugamersTournamentRef],
    'upcoming_matches': NotRequired[list[ModelGosugamersMatchSummary]],
    'venue': NotRequired[str],
}, total=False)

ModelGosugamersMatchSummary = TypedDict('ModelGosugamersMatchSummary', {
    'finished': NotRequired[bool],
    'game': NotRequired[str],
    'group': NotRequired[str],
    'id': NotRequired[str],
    'match_number': NotRequired[int],
    'round': NotRequired[str],
    'stage': NotRequired[str],
    'start_time': NotRequired[str],
    'teams': NotRequired[list[ModelGosugamersTeam]],
    'tournament': NotRequired[ModelGosugamersTournamentRef],
    'url': NotRequired[str],
    'venue': NotRequired[str],
}, total=False)

ModelGosugamersTournamentRef = TypedDict('ModelGosugamersTournamentRef', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelGosugamersTeam = TypedDict('ModelGosugamersTeam', {
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'score': NotRequired[int],
    'slug': NotRequired[str],
    'tag': NotRequired[str],
    'winner': NotRequired[bool],
}, total=False)

ModelGosugamersStageInfo = TypedDict('ModelGosugamersStageInfo', {
    'id': NotRequired[str],
    'live': NotRequired[bool],
    'name': NotRequired[str],
    'order': NotRequired[int],
    'status': NotRequired[str],
}, total=False)

ModelGosugamersTeamResultsResponse = TypedDict('ModelGosugamersTeamResultsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'matches': NotRequired[list[ModelGosugamersMatchSummary]],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'source_url': NotRequired[str],
    'team_id': NotRequired[str],
    'total_pages': NotRequired[int],
    'total_rows': NotRequired[int],
}, total=False)

ModelGosugamersTeamDetail = TypedDict('ModelGosugamersTeamDetail', {
    'about': NotRequired[str],
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'draws': NotRequired[int],
    'earnings_usd': NotRequired[float],
    'elo_rating': NotRequired[int],
    'facebook': NotRequired[str],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'losses': NotRequired[int],
    'name': NotRequired[str],
    'region': NotRequired[str],
    'region_ranking': NotRequired[int],
    'roster': NotRequired[list[ModelGosugamersRosterPlayer]],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
    'streak': NotRequired[int],
    'tag': NotRequired[str],
    'twitter': NotRequired[str],
    'upcoming_matches': NotRequired[list[ModelGosugamersMatchSummary]],
    'url': NotRequired[str],
    'win_rate_percent': NotRequired[int],
    'wins': NotRequired[int],
    'world_ranking': NotRequired[int],
    'youtube': NotRequired[str],
}, total=False)

ModelGosugamersRosterPlayer = TypedDict('ModelGosugamersRosterPlayer', {
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'id': NotRequired[str],
    'joined_at': NotRequired[str],
    'left_at': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelGosugamersStageGroupsResponse = TypedDict('ModelGosugamersStageGroupsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'groups': NotRequired[list[ModelGosugamersStageGroup]],
    'source_url': NotRequired[str],
    'stage_id': NotRequired[str],
    'stage_name': NotRequired[str],
    'tournament_id': NotRequired[str],
}, total=False)

ModelGosugamersStageGroup = TypedDict('ModelGosugamersStageGroup', {
    'format': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'participant_count': NotRequired[int],
    'participants': NotRequired[list[ModelGosugamersParticipant]],
    'result_type': NotRequired[str],
    'start_time': NotRequired[str],
    'status': NotRequired[str],
}, total=False)

ModelGosugamersMatchListResponse = TypedDict('ModelGosugamersMatchListResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'matches': NotRequired[list[ModelGosugamersMatchSummary]],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'source_url': NotRequired[str],
    'total_pages': NotRequired[int],
    'total_rows': NotRequired[int],
}, total=False)

ModelGosugamersRankingsResponse = TypedDict('ModelGosugamersRankingsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'q': NotRequired[str],
    'region_id': NotRequired[int],
    'regions': NotRequired[list[ModelGosugamersRankRegion]],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelGosugamersRankedTeam]],
    'total_pages': NotRequired[int],
    'total_rows': NotRequired[int],
}, total=False)

ModelGosugamersRankedTeam = TypedDict('ModelGosugamersRankedTeam', {
    'elo': NotRequired[float],
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'previous_rank': NotRequired[int],
    'rank': NotRequired[int],
    'rank_change': NotRequired[int],
    'rank_change_name': NotRequired[str],
    'slug': NotRequired[str],
    'tag': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelGosugamersRankRegion = TypedDict('ModelGosugamersRankRegion', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelGosugamersPlayerDetail = TypedDict('ModelGosugamersPlayerDetail', {
    'about': NotRequired[str],
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'current_team': NotRequired[ModelGosugamersTeamStint],
    'draws': NotRequired[int],
    'earnings_usd': NotRequired[float],
    'elo_rating': NotRequired[int],
    'facebook': NotRequired[str],
    'fetched_at': NotRequired[str],
    'first_name': NotRequired[str],
    'game': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'last_name': NotRequired[str],
    'losses': NotRequired[int],
    'name': NotRequired[str],
    'previous_teams': NotRequired[list[ModelGosugamersTeamStint]],
    'region': NotRequired[str],
    'region_ranking': NotRequired[int],
    'source_url': NotRequired[str],
    'streak': NotRequired[int],
    'twitter': NotRequired[str],
    'url': NotRequired[str],
    'win_rate_percent': NotRequired[int],
    'wins': NotRequired[int],
    'world_ranking': NotRequired[int],
    'youtube': NotRequired[str],
}, total=False)

ModelGosugamersTeamStint = TypedDict('ModelGosugamersTeamStint', {
    'joined_at': NotRequired[str],
    'left_at': NotRequired[str],
    'name': NotRequired[str],
    'position': NotRequired[str],
    'slug': NotRequired[str],
    'tag': NotRequired[str],
    'team_id': NotRequired[str],
}, total=False)

ModelGosugamersMatchGameResponse = TypedDict('ModelGosugamersMatchGameResponse', {
    'battle_royale_teams': NotRequired[list[ModelGosugamersBattleRoyaleTeam]],
    'best_of': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'id': NotRequired[str],
    'map': NotRequired[ModelGosugamersGameMap],
    'match_number': NotRequired[int],
    'number': NotRequired[int],
    'player_based': NotRequired[bool],
    'round': NotRequired[str],
    'rounds': NotRequired[list[ModelGosugamersGameRound]],
    'source_url': NotRequired[str],
    'start_time': NotRequired[str],
    'teams': NotRequired[list[ModelGosugamersGameTeam]],
    'vods': NotRequired[list[ModelGosugamersGameVod]],
}, total=False)

ModelGosugamersGameVod = TypedDict('ModelGosugamersGameVod', {
    'channel': NotRequired[str],
    'host': NotRequired[int],
    'thumb_url': NotRequired[str],
    'title': NotRequired[str],
    'video_id': NotRequired[str],
}, total=False)

ModelGosugamersGameTeam = TypedDict('ModelGosugamersGameTeam', {
    'first_pick': NotRequired[bool],
    'id': NotRequired[str],
    'lineup': NotRequired[list[ModelGosugamersGamePlayer]],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'picks': NotRequired[list[ModelGosugamersGamePick]],
    'placement': NotRequired[int],
    'score': NotRequired[int],
    'side': NotRequired[str],
    'slug': NotRequired[str],
    'winner': NotRequired[bool],
}, total=False)

ModelGosugamersGamePick = TypedDict('ModelGosugamersGamePick', {
    'image_url': NotRequired[str],
    'pick': NotRequired[str],
    'player': NotRequired[ModelGosugamersGamePlayer],
    'slot': NotRequired[int],
    'type': NotRequired[int],
}, total=False)

ModelGosugamersGamePlayer = TypedDict('ModelGosugamersGamePlayer', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelGosugamersGameRound = TypedDict('ModelGosugamersGameRound', {
    'overtime': NotRequired[bool],
    'period': NotRequired[int],
    'team1_score': NotRequired[int],
    'team2_score': NotRequired[int],
}, total=False)

ModelGosugamersGameMap = TypedDict('ModelGosugamersGameMap', {
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelGosugamersBattleRoyaleTeam = TypedDict('ModelGosugamersBattleRoyaleTeam', {
    'country_code': NotRequired[str],
    'id': NotRequired[str],
    'kill_points': NotRequired[int],
    'kills': NotRequired[int],
    'name': NotRequired[str],
    'placement': NotRequired[int],
    'placement_points': NotRequired[int],
    'players': NotRequired[list[ModelGosugamersBattleRoyalePlayer]],
    'points_addition': NotRequired[int],
    'points_deduction': NotRequired[int],
    'slug': NotRequired[str],
    'total_points': NotRequired[int],
}, total=False)

ModelGosugamersBattleRoyalePlayer = TypedDict('ModelGosugamersBattleRoyalePlayer', {
    'country_code': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelGosugamersMatchDetail = TypedDict('ModelGosugamersMatchDetail', {
    'best_of': NotRequired[int],
    'fetched_at': NotRequired[str],
    'finished': NotRequired[bool],
    'game': NotRequired[str],
    'game_numbers': NotRequired[list[int]],
    'games': NotRequired[list[ModelGosugamersGameRef]],
    'group': NotRequired[str],
    'id': NotRequired[str],
    'opponents': NotRequired[list[ModelGosugamersOpponent]],
    'round': NotRequired[str],
    'source_url': NotRequired[str],
    'stage': NotRequired[str],
    'start_time': NotRequired[str],
    'streams': NotRequired[list[ModelGosugamersStream]],
    'tournament': NotRequired[ModelGosugamersTournamentRef],
    'url': NotRequired[str],
    'venue': NotRequired[str],
}, total=False)

ModelGosugamersStream = TypedDict('ModelGosugamersStream', {
    'language': NotRequired[str],
    'live': NotRequired[bool],
    'platform_id': NotRequired[int],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'viewer_count': NotRequired[int],
}, total=False)

ModelGosugamersOpponent = TypedDict('ModelGosugamersOpponent', {
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'placement': NotRequired[int],
    'score': NotRequired[int],
    'slug': NotRequired[str],
    'tag': NotRequired[str],
    'winner': NotRequired[bool],
    'world_ranking': NotRequired[int],
}, total=False)

ModelGosugamersGameRef = TypedDict('ModelGosugamersGameRef', {
    'id': NotRequired[str],
    'number': NotRequired[int],
}, total=False)

ModelGosugamersGamesResponse = TypedDict('ModelGosugamersGamesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'games': NotRequired[list[ModelGosugamersGame]],
    'source_url': NotRequired[str],
}, total=False)

ModelGosugamersGame = TypedDict('ModelGosugamersGame', {
    'name': NotRequired[str],
    'slug': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
}, total=False)

ModelGosugamersEncountersResponse = TypedDict('ModelGosugamersEncountersResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'game': NotRequired[str],
    'match_id': NotRequired[str],
    'matches': NotRequired[list[ModelGosugamersMatchSummary]],
    'source_url': NotRequired[str],
    'team1_id': NotRequired[str],
    'team2_id': NotRequired[str],
}, total=False)

ModelGosugamersArticlesResponse = TypedDict('ModelGosugamersArticlesResponse', {
    'articles': NotRequired[list[ModelGosugamersArticleSummary]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
    'section': NotRequired[str],
    'source_url': NotRequired[str],
    'total_pages': NotRequired[int],
    'total_rows': NotRequired[int],
    'type': NotRequired[Literal['news', 'features']],
}, total=False)

ModelGosugamersArticleSummary = TypedDict('ModelGosugamersArticleSummary', {
    'author': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'published_at': NotRequired[str],
    'section': NotRequired[str],
    'teaser': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[Literal['news', 'features']],
    'url': NotRequired[str],
}, total=False)

ModelGosugamersArticleDetail = TypedDict('ModelGosugamersArticleDetail', {
    'authors': NotRequired[list[ModelGosugamersArticleAuthor]],
    'fetched_at': NotRequired[str],
    'id': NotRequired[str],
    'image_caption': NotRequired[str],
    'image_url': NotRequired[str],
    'published_at': NotRequired[str],
    'related': NotRequired[list[ModelGosugamersRelatedArticle]],
    'section': NotRequired[str],
    'source_url': NotRequired[str],
    'teaser': NotRequired[str],
    'text': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[Literal['news', 'features']],
    'updated_at': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelGosugamersRelatedArticle = TypedDict('ModelGosugamersRelatedArticle', {
    'id': NotRequired[str],
    'section': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelGosugamersArticleAuthor = TypedDict('ModelGosugamersArticleAuthor', {
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

GosugamersArticleResponse = Any
GosugamersArticleParams = TypedDict('GosugamersArticleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

GosugamersArticlesResponse = Any
GosugamersArticlesParams = TypedDict('GosugamersArticlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'section': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india', 'entertainment', 'genshin-impact', 'honkai-star-rail', 'zenless-zone-zero', 'honor-of-kings', 'umamusume-pretty-derby']],
    'type': NotRequired[Literal['news', 'features']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersEncountersResponse = Any
GosugamersEncountersParams = TypedDict('GosugamersEncountersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'match_id': Required[str],
    'team1_id': Required[str],
    'team2_id': Required[str],
}, total=False)

GosugamersGamesResponse = Any
GosugamersGamesParams = TypedDict('GosugamersGamesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

GosugamersMatchResponse = Any
GosugamersMatchParams = TypedDict('GosugamersMatchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
    'match_id': Required[str],
}, total=False)

GosugamersMatchGameResponse = Any
GosugamersMatchGameParams = TypedDict('GosugamersMatchGameParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
}, total=False)

GosugamersMatchesResponse = Any
GosugamersMatchesParams = TypedDict('GosugamersMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersPlayerResponse = Any
GosugamersPlayerParams = TypedDict('GosugamersPlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'player_id': Required[str],
}, total=False)

GosugamersRankingsResponse = Any
GosugamersRankingsParams = TypedDict('GosugamersRankingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'region_id': NotRequired[int],
    'q': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersResultsResponse = Any
GosugamersResultsParams = TypedDict('GosugamersResultsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersStageGroupsResponse = Any
GosugamersStageGroupsParams = TypedDict('GosugamersStageGroupsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament_id': Required[str],
    'stage_id': Required[str],
}, total=False)

GosugamersTeamResponse = Any
GosugamersTeamParams = TypedDict('GosugamersTeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'team_id': Required[str],
}, total=False)

GosugamersTeamResultsResponse = Any
GosugamersTeamResultsParams = TypedDict('GosugamersTeamResultsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'team_id': Required[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersTournamentResponse = Any
GosugamersTournamentParams = TypedDict('GosugamersTournamentParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentParticipantsResponse = Any
GosugamersTournamentParticipantsParams = TypedDict('GosugamersTournamentParticipantsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentTalentsResponse = Any
GosugamersTournamentTalentsParams = TypedDict('GosugamersTournamentTalentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentsResponse = Any
GosugamersTournamentsParams = TypedDict('GosugamersTournamentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'state': NotRequired[Literal['all', 'ongoing', 'upcoming', 'past']],
    'q': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

class GosugamersGroup:
    @overload
    def article(self, **params: Unpack[GosugamersArticleStreamParams]) -> BinaryIO: ...
    @overload
    def article(self, **params: Unpack[GosugamersArticleTextResponseParams]) -> str: ...
    @overload
    def article(self, **params: Unpack[GosugamersArticleDefaultParams]) -> GosugamersArticleResponse: ...
    @overload
    def articles(self, **params: Unpack[GosugamersArticlesStreamParams]) -> BinaryIO: ...
    @overload
    def articles(self, **params: Unpack[GosugamersArticlesTextResponseParams]) -> str: ...
    @overload
    def articles(self, **params: Unpack[GosugamersArticlesDefaultParams]) -> GosugamersArticlesResponse: ...
    @overload
    def encounters(self, **params: Unpack[GosugamersEncountersStreamParams]) -> BinaryIO: ...
    @overload
    def encounters(self, **params: Unpack[GosugamersEncountersTextResponseParams]) -> str: ...
    @overload
    def encounters(self, **params: Unpack[GosugamersEncountersDefaultParams]) -> GosugamersEncountersResponse: ...
    @overload
    def games(self, **params: Unpack[GosugamersGamesStreamParams]) -> BinaryIO: ...
    @overload
    def games(self, **params: Unpack[GosugamersGamesTextResponseParams]) -> str: ...
    @overload
    def games(self, **params: Unpack[GosugamersGamesDefaultParams]) -> GosugamersGamesResponse: ...
    @overload
    def match(self, **params: Unpack[GosugamersMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[GosugamersMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[GosugamersMatchDefaultParams]) -> GosugamersMatchResponse: ...
    @overload
    def match_game(self, **params: Unpack[GosugamersMatchGameStreamParams]) -> BinaryIO: ...
    @overload
    def match_game(self, **params: Unpack[GosugamersMatchGameTextResponseParams]) -> str: ...
    @overload
    def match_game(self, **params: Unpack[GosugamersMatchGameDefaultParams]) -> GosugamersMatchGameResponse: ...
    @overload
    def matches(self, **params: Unpack[GosugamersMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def matches(self, **params: Unpack[GosugamersMatchesTextResponseParams]) -> str: ...
    @overload
    def matches(self, **params: Unpack[GosugamersMatchesDefaultParams]) -> GosugamersMatchesResponse: ...
    @overload
    def player(self, **params: Unpack[GosugamersPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[GosugamersPlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[GosugamersPlayerDefaultParams]) -> GosugamersPlayerResponse: ...
    @overload
    def rankings(self, **params: Unpack[GosugamersRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def rankings(self, **params: Unpack[GosugamersRankingsTextResponseParams]) -> str: ...
    @overload
    def rankings(self, **params: Unpack[GosugamersRankingsDefaultParams]) -> GosugamersRankingsResponse: ...
    @overload
    def results(self, **params: Unpack[GosugamersResultsStreamParams]) -> BinaryIO: ...
    @overload
    def results(self, **params: Unpack[GosugamersResultsTextResponseParams]) -> str: ...
    @overload
    def results(self, **params: Unpack[GosugamersResultsDefaultParams]) -> GosugamersResultsResponse: ...
    @overload
    def stage_groups(self, **params: Unpack[GosugamersStageGroupsStreamParams]) -> BinaryIO: ...
    @overload
    def stage_groups(self, **params: Unpack[GosugamersStageGroupsTextResponseParams]) -> str: ...
    @overload
    def stage_groups(self, **params: Unpack[GosugamersStageGroupsDefaultParams]) -> GosugamersStageGroupsResponse: ...
    @overload
    def team(self, **params: Unpack[GosugamersTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[GosugamersTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[GosugamersTeamDefaultParams]) -> GosugamersTeamResponse: ...
    @overload
    def team_results(self, **params: Unpack[GosugamersTeamResultsStreamParams]) -> BinaryIO: ...
    @overload
    def team_results(self, **params: Unpack[GosugamersTeamResultsTextResponseParams]) -> str: ...
    @overload
    def team_results(self, **params: Unpack[GosugamersTeamResultsDefaultParams]) -> GosugamersTeamResultsResponse: ...
    @overload
    def tournament(self, **params: Unpack[GosugamersTournamentStreamParams]) -> BinaryIO: ...
    @overload
    def tournament(self, **params: Unpack[GosugamersTournamentTextResponseParams]) -> str: ...
    @overload
    def tournament(self, **params: Unpack[GosugamersTournamentDefaultParams]) -> GosugamersTournamentResponse: ...
    @overload
    def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsTextResponseParams]) -> str: ...
    @overload
    def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsDefaultParams]) -> GosugamersTournamentParticipantsResponse: ...
    @overload
    def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsTextResponseParams]) -> str: ...
    @overload
    def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsDefaultParams]) -> GosugamersTournamentTalentsResponse: ...
    @overload
    def tournaments(self, **params: Unpack[GosugamersTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def tournaments(self, **params: Unpack[GosugamersTournamentsTextResponseParams]) -> str: ...
    @overload
    def tournaments(self, **params: Unpack[GosugamersTournamentsDefaultParams]) -> GosugamersTournamentsResponse: ...

OperationId = Literal[
    'gosugamers-article',
    'gosugamers-articles',
    'gosugamers-encounters',
    'gosugamers-games',
    'gosugamers-match',
    'gosugamers-match-game',
    'gosugamers-matches',
    'gosugamers-player',
    'gosugamers-rankings',
    'gosugamers-results',
    'gosugamers-stage-groups',
    'gosugamers-team',
    'gosugamers-team-results',
    'gosugamers-tournament',
    'gosugamers-tournament-participants',
    'gosugamers-tournament-talents',
    'gosugamers-tournaments',
]

class CrawloraClient:
    gosugamers: GosugamersGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-article'],
        params: GosugamersArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersArticleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-articles'],
        params: GosugamersArticlesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersArticlesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-encounters'],
        params: GosugamersEncountersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersEncountersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-games'],
        params: GosugamersGamesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersGamesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-match'],
        params: GosugamersMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersMatchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-match-game'],
        params: GosugamersMatchGameParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersMatchGameResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-matches'],
        params: GosugamersMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-player'],
        params: GosugamersPlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersPlayerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-rankings'],
        params: GosugamersRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersRankingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-results'],
        params: GosugamersResultsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersResultsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-stage-groups'],
        params: GosugamersStageGroupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersStageGroupsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-team'],
        params: GosugamersTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-team-results'],
        params: GosugamersTeamResultsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTeamResultsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-tournament'],
        params: GosugamersTournamentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTournamentResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-tournament-participants'],
        params: GosugamersTournamentParticipantsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTournamentParticipantsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-tournament-talents'],
        params: GosugamersTournamentTalentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTournamentTalentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['gosugamers-tournaments'],
        params: GosugamersTournamentsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTournamentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-article'],
        params: GosugamersArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersArticleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-articles'],
        params: GosugamersArticlesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersArticlesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-encounters'],
        params: GosugamersEncountersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersEncountersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-games'],
        params: GosugamersGamesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersGamesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-match'],
        params: GosugamersMatchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersMatchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-match-game'],
        params: GosugamersMatchGameParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersMatchGameResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-matches'],
        params: GosugamersMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-player'],
        params: GosugamersPlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersPlayerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-rankings'],
        params: GosugamersRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersRankingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-results'],
        params: GosugamersResultsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersResultsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-stage-groups'],
        params: GosugamersStageGroupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersStageGroupsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-team'],
        params: GosugamersTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-team-results'],
        params: GosugamersTeamResultsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTeamResultsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-tournament'],
        params: GosugamersTournamentParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTournamentResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-tournament-participants'],
        params: GosugamersTournamentParticipantsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTournamentParticipantsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-tournament-talents'],
        params: GosugamersTournamentTalentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTournamentTalentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['gosugamers-tournaments'],
        params: GosugamersTournamentsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> GosugamersTournamentsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class GosuGamersClient(CrawloraClient):
    def __enter__(self) -> GosuGamersClient: ...
    @overload
    def article(self, **params: Unpack[GosugamersArticleStreamParams]) -> BinaryIO: ...
    @overload
    def article(self, **params: Unpack[GosugamersArticleTextResponseParams]) -> str: ...
    @overload
    def article(self, **params: Unpack[GosugamersArticleDefaultParams]) -> GosugamersArticleResponse: ...
    @overload
    def articles(self, **params: Unpack[GosugamersArticlesStreamParams]) -> BinaryIO: ...
    @overload
    def articles(self, **params: Unpack[GosugamersArticlesTextResponseParams]) -> str: ...
    @overload
    def articles(self, **params: Unpack[GosugamersArticlesDefaultParams]) -> GosugamersArticlesResponse: ...
    @overload
    def encounters(self, **params: Unpack[GosugamersEncountersStreamParams]) -> BinaryIO: ...
    @overload
    def encounters(self, **params: Unpack[GosugamersEncountersTextResponseParams]) -> str: ...
    @overload
    def encounters(self, **params: Unpack[GosugamersEncountersDefaultParams]) -> GosugamersEncountersResponse: ...
    @overload
    def games(self, **params: Unpack[GosugamersGamesStreamParams]) -> BinaryIO: ...
    @overload
    def games(self, **params: Unpack[GosugamersGamesTextResponseParams]) -> str: ...
    @overload
    def games(self, **params: Unpack[GosugamersGamesDefaultParams]) -> GosugamersGamesResponse: ...
    @overload
    def match(self, **params: Unpack[GosugamersMatchStreamParams]) -> BinaryIO: ...
    @overload
    def match(self, **params: Unpack[GosugamersMatchTextResponseParams]) -> str: ...
    @overload
    def match(self, **params: Unpack[GosugamersMatchDefaultParams]) -> GosugamersMatchResponse: ...
    @overload
    def match_game(self, **params: Unpack[GosugamersMatchGameStreamParams]) -> BinaryIO: ...
    @overload
    def match_game(self, **params: Unpack[GosugamersMatchGameTextResponseParams]) -> str: ...
    @overload
    def match_game(self, **params: Unpack[GosugamersMatchGameDefaultParams]) -> GosugamersMatchGameResponse: ...
    @overload
    def matches(self, **params: Unpack[GosugamersMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def matches(self, **params: Unpack[GosugamersMatchesTextResponseParams]) -> str: ...
    @overload
    def matches(self, **params: Unpack[GosugamersMatchesDefaultParams]) -> GosugamersMatchesResponse: ...
    @overload
    def player(self, **params: Unpack[GosugamersPlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[GosugamersPlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[GosugamersPlayerDefaultParams]) -> GosugamersPlayerResponse: ...
    @overload
    def rankings(self, **params: Unpack[GosugamersRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def rankings(self, **params: Unpack[GosugamersRankingsTextResponseParams]) -> str: ...
    @overload
    def rankings(self, **params: Unpack[GosugamersRankingsDefaultParams]) -> GosugamersRankingsResponse: ...
    @overload
    def results(self, **params: Unpack[GosugamersResultsStreamParams]) -> BinaryIO: ...
    @overload
    def results(self, **params: Unpack[GosugamersResultsTextResponseParams]) -> str: ...
    @overload
    def results(self, **params: Unpack[GosugamersResultsDefaultParams]) -> GosugamersResultsResponse: ...
    @overload
    def stage_groups(self, **params: Unpack[GosugamersStageGroupsStreamParams]) -> BinaryIO: ...
    @overload
    def stage_groups(self, **params: Unpack[GosugamersStageGroupsTextResponseParams]) -> str: ...
    @overload
    def stage_groups(self, **params: Unpack[GosugamersStageGroupsDefaultParams]) -> GosugamersStageGroupsResponse: ...
    @overload
    def team(self, **params: Unpack[GosugamersTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[GosugamersTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[GosugamersTeamDefaultParams]) -> GosugamersTeamResponse: ...
    @overload
    def team_results(self, **params: Unpack[GosugamersTeamResultsStreamParams]) -> BinaryIO: ...
    @overload
    def team_results(self, **params: Unpack[GosugamersTeamResultsTextResponseParams]) -> str: ...
    @overload
    def team_results(self, **params: Unpack[GosugamersTeamResultsDefaultParams]) -> GosugamersTeamResultsResponse: ...
    @overload
    def tournament(self, **params: Unpack[GosugamersTournamentStreamParams]) -> BinaryIO: ...
    @overload
    def tournament(self, **params: Unpack[GosugamersTournamentTextResponseParams]) -> str: ...
    @overload
    def tournament(self, **params: Unpack[GosugamersTournamentDefaultParams]) -> GosugamersTournamentResponse: ...
    @overload
    def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsTextResponseParams]) -> str: ...
    @overload
    def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsDefaultParams]) -> GosugamersTournamentParticipantsResponse: ...
    @overload
    def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsTextResponseParams]) -> str: ...
    @overload
    def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsDefaultParams]) -> GosugamersTournamentTalentsResponse: ...
    @overload
    def tournaments(self, **params: Unpack[GosugamersTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def tournaments(self, **params: Unpack[GosugamersTournamentsTextResponseParams]) -> str: ...
    @overload
    def tournaments(self, **params: Unpack[GosugamersTournamentsDefaultParams]) -> GosugamersTournamentsResponse: ...

class AsyncGosuGamersClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncGosuGamersClient: ...
    gosugamers: _AsyncGosugamersGroup
    @overload
    async def article(self, **params: Unpack[GosugamersArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def article(self, **params: Unpack[GosugamersArticleTextResponseParams]) -> str: ...
    @overload
    async def article(self, **params: Unpack[GosugamersArticleDefaultParams]) -> GosugamersArticleResponse: ...
    @overload
    async def articles(self, **params: Unpack[GosugamersArticlesStreamParams]) -> BinaryIO: ...
    @overload
    async def articles(self, **params: Unpack[GosugamersArticlesTextResponseParams]) -> str: ...
    @overload
    async def articles(self, **params: Unpack[GosugamersArticlesDefaultParams]) -> GosugamersArticlesResponse: ...
    @overload
    async def encounters(self, **params: Unpack[GosugamersEncountersStreamParams]) -> BinaryIO: ...
    @overload
    async def encounters(self, **params: Unpack[GosugamersEncountersTextResponseParams]) -> str: ...
    @overload
    async def encounters(self, **params: Unpack[GosugamersEncountersDefaultParams]) -> GosugamersEncountersResponse: ...
    @overload
    async def games(self, **params: Unpack[GosugamersGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def games(self, **params: Unpack[GosugamersGamesTextResponseParams]) -> str: ...
    @overload
    async def games(self, **params: Unpack[GosugamersGamesDefaultParams]) -> GosugamersGamesResponse: ...
    @overload
    async def match(self, **params: Unpack[GosugamersMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[GosugamersMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[GosugamersMatchDefaultParams]) -> GosugamersMatchResponse: ...
    @overload
    async def match_game(self, **params: Unpack[GosugamersMatchGameStreamParams]) -> BinaryIO: ...
    @overload
    async def match_game(self, **params: Unpack[GosugamersMatchGameTextResponseParams]) -> str: ...
    @overload
    async def match_game(self, **params: Unpack[GosugamersMatchGameDefaultParams]) -> GosugamersMatchGameResponse: ...
    @overload
    async def matches(self, **params: Unpack[GosugamersMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matches(self, **params: Unpack[GosugamersMatchesTextResponseParams]) -> str: ...
    @overload
    async def matches(self, **params: Unpack[GosugamersMatchesDefaultParams]) -> GosugamersMatchesResponse: ...
    @overload
    async def player(self, **params: Unpack[GosugamersPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[GosugamersPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[GosugamersPlayerDefaultParams]) -> GosugamersPlayerResponse: ...
    @overload
    async def rankings(self, **params: Unpack[GosugamersRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[GosugamersRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[GosugamersRankingsDefaultParams]) -> GosugamersRankingsResponse: ...
    @overload
    async def results(self, **params: Unpack[GosugamersResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def results(self, **params: Unpack[GosugamersResultsTextResponseParams]) -> str: ...
    @overload
    async def results(self, **params: Unpack[GosugamersResultsDefaultParams]) -> GosugamersResultsResponse: ...
    @overload
    async def stage_groups(self, **params: Unpack[GosugamersStageGroupsStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_groups(self, **params: Unpack[GosugamersStageGroupsTextResponseParams]) -> str: ...
    @overload
    async def stage_groups(self, **params: Unpack[GosugamersStageGroupsDefaultParams]) -> GosugamersStageGroupsResponse: ...
    @overload
    async def team(self, **params: Unpack[GosugamersTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[GosugamersTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[GosugamersTeamDefaultParams]) -> GosugamersTeamResponse: ...
    @overload
    async def team_results(self, **params: Unpack[GosugamersTeamResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_results(self, **params: Unpack[GosugamersTeamResultsTextResponseParams]) -> str: ...
    @overload
    async def team_results(self, **params: Unpack[GosugamersTeamResultsDefaultParams]) -> GosugamersTeamResultsResponse: ...
    @overload
    async def tournament(self, **params: Unpack[GosugamersTournamentStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament(self, **params: Unpack[GosugamersTournamentTextResponseParams]) -> str: ...
    @overload
    async def tournament(self, **params: Unpack[GosugamersTournamentDefaultParams]) -> GosugamersTournamentResponse: ...
    @overload
    async def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsTextResponseParams]) -> str: ...
    @overload
    async def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsDefaultParams]) -> GosugamersTournamentParticipantsResponse: ...
    @overload
    async def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsTextResponseParams]) -> str: ...
    @overload
    async def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsDefaultParams]) -> GosugamersTournamentTalentsResponse: ...
    @overload
    async def tournaments(self, **params: Unpack[GosugamersTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournaments(self, **params: Unpack[GosugamersTournamentsTextResponseParams]) -> str: ...
    @overload
    async def tournaments(self, **params: Unpack[GosugamersTournamentsDefaultParams]) -> GosugamersTournamentsResponse: ...

class _AsyncGosugamersGroup:
    @overload
    async def article(self, **params: Unpack[GosugamersArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def article(self, **params: Unpack[GosugamersArticleTextResponseParams]) -> str: ...
    @overload
    async def article(self, **params: Unpack[GosugamersArticleDefaultParams]) -> GosugamersArticleResponse: ...
    @overload
    async def articles(self, **params: Unpack[GosugamersArticlesStreamParams]) -> BinaryIO: ...
    @overload
    async def articles(self, **params: Unpack[GosugamersArticlesTextResponseParams]) -> str: ...
    @overload
    async def articles(self, **params: Unpack[GosugamersArticlesDefaultParams]) -> GosugamersArticlesResponse: ...
    @overload
    async def encounters(self, **params: Unpack[GosugamersEncountersStreamParams]) -> BinaryIO: ...
    @overload
    async def encounters(self, **params: Unpack[GosugamersEncountersTextResponseParams]) -> str: ...
    @overload
    async def encounters(self, **params: Unpack[GosugamersEncountersDefaultParams]) -> GosugamersEncountersResponse: ...
    @overload
    async def games(self, **params: Unpack[GosugamersGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def games(self, **params: Unpack[GosugamersGamesTextResponseParams]) -> str: ...
    @overload
    async def games(self, **params: Unpack[GosugamersGamesDefaultParams]) -> GosugamersGamesResponse: ...
    @overload
    async def match(self, **params: Unpack[GosugamersMatchStreamParams]) -> BinaryIO: ...
    @overload
    async def match(self, **params: Unpack[GosugamersMatchTextResponseParams]) -> str: ...
    @overload
    async def match(self, **params: Unpack[GosugamersMatchDefaultParams]) -> GosugamersMatchResponse: ...
    @overload
    async def match_game(self, **params: Unpack[GosugamersMatchGameStreamParams]) -> BinaryIO: ...
    @overload
    async def match_game(self, **params: Unpack[GosugamersMatchGameTextResponseParams]) -> str: ...
    @overload
    async def match_game(self, **params: Unpack[GosugamersMatchGameDefaultParams]) -> GosugamersMatchGameResponse: ...
    @overload
    async def matches(self, **params: Unpack[GosugamersMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matches(self, **params: Unpack[GosugamersMatchesTextResponseParams]) -> str: ...
    @overload
    async def matches(self, **params: Unpack[GosugamersMatchesDefaultParams]) -> GosugamersMatchesResponse: ...
    @overload
    async def player(self, **params: Unpack[GosugamersPlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[GosugamersPlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[GosugamersPlayerDefaultParams]) -> GosugamersPlayerResponse: ...
    @overload
    async def rankings(self, **params: Unpack[GosugamersRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[GosugamersRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[GosugamersRankingsDefaultParams]) -> GosugamersRankingsResponse: ...
    @overload
    async def results(self, **params: Unpack[GosugamersResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def results(self, **params: Unpack[GosugamersResultsTextResponseParams]) -> str: ...
    @overload
    async def results(self, **params: Unpack[GosugamersResultsDefaultParams]) -> GosugamersResultsResponse: ...
    @overload
    async def stage_groups(self, **params: Unpack[GosugamersStageGroupsStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_groups(self, **params: Unpack[GosugamersStageGroupsTextResponseParams]) -> str: ...
    @overload
    async def stage_groups(self, **params: Unpack[GosugamersStageGroupsDefaultParams]) -> GosugamersStageGroupsResponse: ...
    @overload
    async def team(self, **params: Unpack[GosugamersTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[GosugamersTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[GosugamersTeamDefaultParams]) -> GosugamersTeamResponse: ...
    @overload
    async def team_results(self, **params: Unpack[GosugamersTeamResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_results(self, **params: Unpack[GosugamersTeamResultsTextResponseParams]) -> str: ...
    @overload
    async def team_results(self, **params: Unpack[GosugamersTeamResultsDefaultParams]) -> GosugamersTeamResultsResponse: ...
    @overload
    async def tournament(self, **params: Unpack[GosugamersTournamentStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament(self, **params: Unpack[GosugamersTournamentTextResponseParams]) -> str: ...
    @overload
    async def tournament(self, **params: Unpack[GosugamersTournamentDefaultParams]) -> GosugamersTournamentResponse: ...
    @overload
    async def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsTextResponseParams]) -> str: ...
    @overload
    async def tournament_participants(self, **params: Unpack[GosugamersTournamentParticipantsDefaultParams]) -> GosugamersTournamentParticipantsResponse: ...
    @overload
    async def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsTextResponseParams]) -> str: ...
    @overload
    async def tournament_talents(self, **params: Unpack[GosugamersTournamentTalentsDefaultParams]) -> GosugamersTournamentTalentsResponse: ...
    @overload
    async def tournaments(self, **params: Unpack[GosugamersTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournaments(self, **params: Unpack[GosugamersTournamentsTextResponseParams]) -> str: ...
    @overload
    async def tournaments(self, **params: Unpack[GosugamersTournamentsDefaultParams]) -> GosugamersTournamentsResponse: ...

GosugamersArticleDefaultParams = TypedDict('GosugamersArticleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

GosugamersArticleTextResponseParams = TypedDict('GosugamersArticleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

GosugamersArticleStreamParams = TypedDict('GosugamersArticleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

GosugamersArticlesDefaultParams = TypedDict('GosugamersArticlesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'section': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india', 'entertainment', 'genshin-impact', 'honkai-star-rail', 'zenless-zone-zero', 'honor-of-kings', 'umamusume-pretty-derby']],
    'type': NotRequired[Literal['news', 'features']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersArticlesTextResponseParams = TypedDict('GosugamersArticlesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'section': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india', 'entertainment', 'genshin-impact', 'honkai-star-rail', 'zenless-zone-zero', 'honor-of-kings', 'umamusume-pretty-derby']],
    'type': NotRequired[Literal['news', 'features']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersArticlesStreamParams = TypedDict('GosugamersArticlesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'section': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india', 'entertainment', 'genshin-impact', 'honkai-star-rail', 'zenless-zone-zero', 'honor-of-kings', 'umamusume-pretty-derby']],
    'type': NotRequired[Literal['news', 'features']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersEncountersDefaultParams = TypedDict('GosugamersEncountersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'match_id': Required[str],
    'team1_id': Required[str],
    'team2_id': Required[str],
}, total=False)

GosugamersEncountersTextResponseParams = TypedDict('GosugamersEncountersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'match_id': Required[str],
    'team1_id': Required[str],
    'team2_id': Required[str],
}, total=False)

GosugamersEncountersStreamParams = TypedDict('GosugamersEncountersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'match_id': Required[str],
    'team1_id': Required[str],
    'team2_id': Required[str],
}, total=False)

GosugamersGamesDefaultParams = TypedDict('GosugamersGamesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

GosugamersGamesTextResponseParams = TypedDict('GosugamersGamesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

GosugamersGamesStreamParams = TypedDict('GosugamersGamesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

GosugamersMatchDefaultParams = TypedDict('GosugamersMatchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
    'match_id': Required[str],
}, total=False)

GosugamersMatchTextResponseParams = TypedDict('GosugamersMatchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
    'match_id': Required[str],
}, total=False)

GosugamersMatchStreamParams = TypedDict('GosugamersMatchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
    'match_id': Required[str],
}, total=False)

GosugamersMatchGameDefaultParams = TypedDict('GosugamersMatchGameDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
}, total=False)

GosugamersMatchGameTextResponseParams = TypedDict('GosugamersMatchGameTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
}, total=False)

GosugamersMatchGameStreamParams = TypedDict('GosugamersMatchGameStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
}, total=False)

GosugamersMatchesDefaultParams = TypedDict('GosugamersMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersMatchesTextResponseParams = TypedDict('GosugamersMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersMatchesStreamParams = TypedDict('GosugamersMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersPlayerDefaultParams = TypedDict('GosugamersPlayerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'player_id': Required[str],
}, total=False)

GosugamersPlayerTextResponseParams = TypedDict('GosugamersPlayerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'player_id': Required[str],
}, total=False)

GosugamersPlayerStreamParams = TypedDict('GosugamersPlayerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'player_id': Required[str],
}, total=False)

GosugamersRankingsDefaultParams = TypedDict('GosugamersRankingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'region_id': NotRequired[int],
    'q': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersRankingsTextResponseParams = TypedDict('GosugamersRankingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'region_id': NotRequired[int],
    'q': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersRankingsStreamParams = TypedDict('GosugamersRankingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'region_id': NotRequired[int],
    'q': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersResultsDefaultParams = TypedDict('GosugamersResultsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersResultsTextResponseParams = TypedDict('GosugamersResultsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersResultsStreamParams = TypedDict('GosugamersResultsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersStageGroupsDefaultParams = TypedDict('GosugamersStageGroupsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament_id': Required[str],
    'stage_id': Required[str],
}, total=False)

GosugamersStageGroupsTextResponseParams = TypedDict('GosugamersStageGroupsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament_id': Required[str],
    'stage_id': Required[str],
}, total=False)

GosugamersStageGroupsStreamParams = TypedDict('GosugamersStageGroupsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament_id': Required[str],
    'stage_id': Required[str],
}, total=False)

GosugamersTeamDefaultParams = TypedDict('GosugamersTeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'team_id': Required[str],
}, total=False)

GosugamersTeamTextResponseParams = TypedDict('GosugamersTeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'team_id': Required[str],
}, total=False)

GosugamersTeamStreamParams = TypedDict('GosugamersTeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'team_id': Required[str],
}, total=False)

GosugamersTeamResultsDefaultParams = TypedDict('GosugamersTeamResultsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'team_id': Required[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersTeamResultsTextResponseParams = TypedDict('GosugamersTeamResultsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'team_id': Required[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersTeamResultsStreamParams = TypedDict('GosugamersTeamResultsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'team_id': Required[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersTournamentDefaultParams = TypedDict('GosugamersTournamentDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentTextResponseParams = TypedDict('GosugamersTournamentTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentStreamParams = TypedDict('GosugamersTournamentStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentParticipantsDefaultParams = TypedDict('GosugamersTournamentParticipantsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentParticipantsTextResponseParams = TypedDict('GosugamersTournamentParticipantsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentParticipantsStreamParams = TypedDict('GosugamersTournamentParticipantsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': Required[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentTalentsDefaultParams = TypedDict('GosugamersTournamentTalentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentTalentsTextResponseParams = TypedDict('GosugamersTournamentTalentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentTalentsStreamParams = TypedDict('GosugamersTournamentTalentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament_id': Required[str],
}, total=False)

GosugamersTournamentsDefaultParams = TypedDict('GosugamersTournamentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'state': NotRequired[Literal['all', 'ongoing', 'upcoming', 'past']],
    'q': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersTournamentsTextResponseParams = TypedDict('GosugamersTournamentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'state': NotRequired[Literal['all', 'ongoing', 'upcoming', 'past']],
    'q': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)

GosugamersTournamentsStreamParams = TypedDict('GosugamersTournamentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game': NotRequired[Literal['dota2', 'counterstrike', 'lol', 'valorant', 'mobile-legends', 'pubg-mobile', 'wild-rift', 'free-fire', 'battlegrounds-mobile-india']],
    'state': NotRequired[Literal['all', 'ongoing', 'upcoming', 'past']],
    'q': NotRequired[str],
    'page': NotRequired[int],
    'page_size': NotRequired[int],
}, total=False)
