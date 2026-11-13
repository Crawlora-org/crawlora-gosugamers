"""Typed GosuGamers client for the Crawlora hosted API."""

from .platform import GosuGamersClient, AsyncGosuGamersClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = GosuGamersClient
AsyncClient = AsyncGosuGamersClient
__version__ = '0.2.0'
DISPLAY_NAME = 'GosuGamers'
PLATFORM = 'gosugamers'
CONTRACT_REVISION = 'sha256:4852bc089ee8d4c64d25328e6822569725709334855eb43fa757c85fda8e6216'

__all__ = [
    "GosuGamersClient", "AsyncGosuGamersClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
