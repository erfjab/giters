from eiogram import Router
from eiogram.types import Message
from eiogram.filters import Command

from src.keys import BotKB

router = Router()


@router.message(Command("start"))
async def start_handlers(message: Message):
    return await message.answer(
        text="Welcome!\nEnter the name of a repository to search on GitHub.",
        reply_markup=BotKB.search_repositories(),
    )
