from eiogram import Router
from . import commands


def setup_handlers() -> Router:
    router = Router()
    router.include_router(commands.router)
    return router
