from eiogram.types import InlineKeyboardButton
from eiogram.utils.inline_builder import InlineKeyboardBuilder


class BotKB:
    @classmethod
    def search_repositories(cls):
        kb = InlineKeyboardBuilder()
        kb.row(
            InlineKeyboardButton(
                text="🔍 Search Repositories", switch_inline_query_current_chat="Linux"
            ),
            InlineKeyboardButton(text="🚀 Owner", url="https://t.me/ErfJabs"),
            size=1,
        )
        return kb.as_markup()
