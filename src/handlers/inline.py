from datetime import datetime
from secrets import token_hex

from eiogram import Router
from eiogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    AnswerInlineQuery,
)

from src.clients import GithubClient
from src.keys import BotKB
from src.config import BOT, DEFAULT_THUMBNAIL

router = Router()


def _create_welcome_result() -> InlineQueryResultArticle:
    """Create the welcome result for empty queries."""
    return InlineQueryResultArticle(
        id="giters",
        title="Welcome, enter a repo name",
        description="Enter the name of a repository to search on GitHub.",
        input_message_content=InputTextMessageContent(
            message_text="🔍 I'm Giters! Just enter the name of a repo, and I'll search for it.",
        ),
        reply_markup=BotKB.search_repositories(),
        thumbnail_url=DEFAULT_THUMBNAIL,
    )


def _create_no_results_result() -> InlineQueryResultArticle:
    """Create the no results found result."""
    return InlineQueryResultArticle(
        id="no_results",
        title="No results found",
        input_message_content=InputTextMessageContent(
            message_text="No repositories found for your query."
        ),
        reply_markup=BotKB.no_results(),
        thumbnail_url=DEFAULT_THUMBNAIL,
    )


def _format_repo_message(repo: dict) -> str:
    """Format the repository information into a message string."""
    created_at = datetime.fromisoformat(repo["created_at"]).replace(tzinfo=None)
    days_ago = (datetime.now() - created_at).days

    return (
        f"<b>📁 {repo['name']} Repo</b>\n"
        f"<b>👤 By:</b> <code>{repo['owner']['login']}</code>\n"
        f"<b>⭐ Stars:</b> <code>{repo['stargazers_count']}</code>\n"
        f"<b>🍴 Forks:</b> <code>{repo['forks_count']}</code>\n"
        f"<b>📋 Language:</b> <code>{repo['language']}</code>\n"
        f"<b>📅 Created At:</b> <code>{repo['created_at']} [{days_ago} days ago]</code>\n"
        f"<b>📝 Description:</b> <code>{repo['description'] or 'No description'}</code>\n"
    )


def _create_repo_result(repo: dict) -> InlineQueryResultArticle:
    """Create an inline query result for a repository."""
    return InlineQueryResultArticle(
        id=token_hex(5),
        title=f"📁 {repo['name'].title()}",
        description=f"⭐ {repo['stargazers_count']} by {repo['owner']['login']}",
        input_message_content=InputTextMessageContent(
            message_text=_format_repo_message(repo), parse_mode="HTML"
        ),
        reply_markup=BotKB.repo_info(repo),
        thumbnail_url=repo["owner"].get("avatar_url", DEFAULT_THUMBNAIL),
    )


@router.inline_query()
async def inline_query_handler(query: InlineQuery):
    search = query.query.strip()

    if not search:
        return await BOT.answer_inline_query(
            AnswerInlineQuery(
                results=[_create_welcome_result()],
                inline_query_id=query.id,
                cache_time=10,
            )
        )

    search_results = await GithubClient.search(query=search)

    if not search_results:
        return await BOT.answer_inline_query(
            AnswerInlineQuery(
                results=[_create_no_results_result()],
                inline_query_id=query.id,
                cache_time=10,
            )
        )

    results = [_create_repo_result(repo) for repo in search_results]

    return await BOT.answer_inline_query(
        AnswerInlineQuery(results=results, inline_query_id=query.id, cache_time=10)
    )
