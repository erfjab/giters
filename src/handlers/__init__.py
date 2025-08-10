from eiogram import Router
from . import commands, inline


def setup_handlers() -> Router:
    router = Router()
    router.include_router(commands.router)
    router.include_router(inline.router)
    return router
