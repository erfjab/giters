from github import Github
from github.Repository import Repository
import random


class GithubClient:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens

    def search(self, query: str) -> list[Repository]:
        token = random.choice(self.tokens) if len(self.tokens) > 0 else None
        client = Github(token)
        results = client.search_repositories(
            query=f"{query} in:name,description fork:true", sort="stars"
        )
        return results.get_page(0)[:10]
