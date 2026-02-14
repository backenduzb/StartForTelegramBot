import asyncio

from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from config.routers import ROUTERS
from config.settings import (
    BOT_TOKEN,
    DEBUG,
    DEFAULT_BOT_PROPERTIES,
    WEB_SERVER_HOST,
    WEB_SERVER_PORT,
    WEBHOOK_SECRET,
)
from utils.createadmin import create_admin
from utils.db import init_db
from utils.webhook import set_webhook

dp = Dispatcher()
dp.include_routers(*ROUTERS)
bot = Bot(
    token=BOT_TOKEN,
    default=DEFAULT_BOT_PROPERTIES,
)


async def start_polling() -> None:
    global dp, bot
    import logging
    import sys
    await init_db()
    await create_admin(
        username="@python_dev_junior",
        tg_id=6400925437
    )
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)


async def start_webhook():
    await init_db()
    await create_admin(
        username="@python_dev_junior",
        tg_id=6400925437
    )
    
    dp.startup.register(set_webhook)

    app = web.Application()

    webhook_handlers = SimpleRequestHandler(
        secret_token=WEBHOOK_SECRET,
        dispatcher=dp,
        bot=bot,
    )
    webhook_handlers.register(app, path="/webhook")

    setup_application(app, dp, bot=bot)
    web.run_app(
        app,
        host=WEB_SERVER_HOST,
        port=WEB_SERVER_PORT,
    )


if __name__ == "__main__":
    if not DEBUG:
        asyncio.run(start_webhook())
    else:
        asyncio.run(start_polling())
