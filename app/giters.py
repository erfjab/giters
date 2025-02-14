import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from app.settings import logger, env
from app.routers import setup_routers


async def main() -> None:
    """Initialize and run the bot."""
    try:
        logger.info("Config Bot")
        bot = Bot(
            token=env.BOT_TOKEN,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML, link_preview_is_disabled=True
            ),
        )
        dp = Dispatcher()
        dp.include_router(router=setup_routers())
        logger.info("Bot is run!")
        await dp.start_polling(bot)
    except (ConnectionError, TimeoutError, asyncio.TimeoutError) as conn_err:
        logger.error("Polling error (connection issue): %s", conn_err)
    except RuntimeError as runtime_err:
        logger.error("Runtime error during polling: %s", runtime_err)
    except asyncio.CancelledError:
        logger.warning("Polling was cancelled.")
