from ._clinet import GithubClient
from app.settings import env

GitApi = GithubClient(tokens=env.GIT_TOKENS)

__all__ = ["GitApi"]
