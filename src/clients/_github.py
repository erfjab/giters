import logging
from typing import List, Dict, Any

import httpx


class GithubClient:
    @classmethod
    async def search(cls, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        url = f"https://api.github.com/search/repositories?q={query}&per_page={limit}"

        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                response = await client.get(url=url)
                response.raise_for_status()

                if "X-RateLimit-Remaining" in response.headers:
                    remaining = int(response.headers["X-RateLimit-Remaining"])
                    if remaining <= 0:
                        logging.warning("GitHub API rate limit exceeded")
                        return []

                result: dict = response.json()
                return result.get("items", [])
            except httpx.HTTPStatusError as e:
                logging.error(f"HTTP error occurred: {e}")
                return []
            except httpx.RequestError as e:
                logging.error(f"Request error occurred: {e}")
                return []
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                return []
