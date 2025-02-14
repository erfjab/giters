from aiogram import Router
from aiogram.types import Message, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder


router = Router(name="start")


@router.message(CommandStart(ignore_case=True))
async def start(message: Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(
            text="🔍 Search Repositories", switch_inline_query_current_chat=""
        )
    )

    return await message.answer(
        text="Welcome!\nEnter the name of a repository to search on GitHub.",
        reply_markup=keyboard.as_markup(),
    )
