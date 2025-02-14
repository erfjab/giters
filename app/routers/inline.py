from secrets import token_hex

from aiogram import Router, types
from aiogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.api import GitApi

router = Router(name="inline")


@router.inline_query()
async def get(query: types.InlineQuery):
    search = query.query.strip()
    results = []

    if not search:
        results = [
            InlineQueryResultArticle(
                id="giters",
                title="Welcome, enter a repo name",
                description="Enter the name of a repository to search on GitHub.",
                input_message_content=InputTextMessageContent(
                    message_text="🔍 I'm Giters! Just enter the name of a repo, and I'll search for it.",
                ),
                thumbnail_url="https://i.pinimg.com/originals/2a/dc/b5/2adcb5b7d4783c60ae9e57b6b7458274.jpg",
            )
        ]
        return await query.answer(
            results=results,
            cache_time=10,
        )

    repos = GitApi.search(search)
    if not repos:
        return await query.answer(
            results=[],
            switch_pm_text="No repos found. Enter a valid repo name.",
            switch_pm_parameter="repo_not_found",
            cache_time=10,
        )
    for repo in repos:
        message_text = (
            f"📁 <b>{repo['name']}</b>\n"
            f"👤 By: {repo['owner']['login']}\n"
            f"⭐ Stars: {repo['stargazers_count']}\n"
            f"🍴 Forks: {repo['forks_count']}\n"
            f"📝 Description: {repo['description']}\n"
            f"🌐 <a href='{repo['html_url']}'>Repo Link</a>"
        )

        keyboard = InlineKeyboardBuilder()
        keyboard.add(InlineKeyboardButton(text="🔗 Go to Repo", url=repo["html_url"]))
        keyboard.add(
            InlineKeyboardButton(
                text="🔍 Search Repositories", switch_inline_query_current_chat=""
            )
        )
        result = InlineQueryResultArticle(
            id=token_hex(5),
            title=f"📁 {repo['name'].title()}",
            description=f"⭐ {repo['stargazers_count']} by {repo['owner']['login']}",
            input_message_content=InputTextMessageContent(message_text=message_text),
            reply_markup=keyboard.as_markup(),
            thumbnail_url="https://i.pinimg.com/originals/2a/dc/b5/2adcb5b7d4783c60ae9e57b6b7458274.jpg",
        )
        results.append(result)

    await query.answer(results=results, cache_time=10)
