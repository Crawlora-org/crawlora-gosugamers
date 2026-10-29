"""Typed GosuGamers client for the Crawlora hosted API."""

from .platform import GosuGamersClient, AsyncGosuGamersClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = GosuGamersClient
AsyncClient = AsyncGosuGamersClient
__version__ = '0.1.0'
DISPLAY_NAME = 'GosuGamers'
PLATFORM = 'gosugamers'
CONTRACT_REVISION = 'sha256:de5fed9f9e96ee896300f2d020f44d15ab18d3f5c885548c7cf5a6ef6a90df3d'

__all__ = [
    "GosuGamersClient", "AsyncGosuGamersClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
