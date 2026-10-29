import os

from crawlora_gosugamers import GosuGamersClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with GosuGamersClient(api_key=api_key) as client:
    games = client.games()
    print('games', games)
    matches = client.matches()
    print('matches', matches)
