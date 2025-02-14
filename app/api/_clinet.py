import requests
import random


class GithubClient:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens

    def search(self, query: str, limit: int = 10):
        token = random.choice(self.tokens) if self.tokens else None
        headers = {"Authorization": f"token {token}"} if token else {}

        url = f"https://api.github.com/search/repositories?q={query}+in:name,description&per_page={limit}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json().get("items")
        return []
