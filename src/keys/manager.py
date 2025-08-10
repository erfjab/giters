from eiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from eiogram.utils.inline_builder import InlineKeyboardBuilder


class BotKB:
    @classmethod
    def search_repositories(cls) -> InlineKeyboardMarkup:
        kb = InlineKeyboardBuilder()
        kb.row(
            InlineKeyboardButton(
                text="🔍 Search Repositories", switch_inline_query_current_chat="Linux"
            ),
            InlineKeyboardButton(text="🚀 Owner", url="https://t.me/ErfJabs"),
            size=1,
        )
        return kb.as_markup()

    @classmethod
    def no_results(cls) -> InlineKeyboardMarkup:
        kb = InlineKeyboardBuilder()
        kb.row(
            InlineKeyboardButton(
                text="🔄 Try Again", switch_inline_query_current_chat="Linux"
            ),
            size=1,
        )
        return kb.as_markup()

    @classmethod
    def repo_info(cls, repo: dict) -> InlineKeyboardMarkup:
        kb = InlineKeyboardBuilder()
        kb.row(
            InlineKeyboardButton(text="🔗 View on GitHub", url=repo["html_url"]),
            InlineKeyboardButton(
                text="🔍 Search Again", switch_inline_query_current_chat="Linux"
            ),
            size=1,
        )
        return kb.as_markup()
