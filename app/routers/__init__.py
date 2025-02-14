from aiogram import Router

from . import base, inline


def setup_routers():
    router = Router()
    router.include_router(base.router)
    router.include_router(inline.router)
    return router
