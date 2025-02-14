from github import Github
from github.PaginatedList import PaginatedList
from github.Repository import Repository
import random


class GithubClient:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens

    def search(self, query: str) -> PaginatedList[Repository]:
        token = random.choice(self.tokens)
        client = Github(token)
        return client.search_repositories(query=query)
