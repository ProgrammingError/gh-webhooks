import logging

from decouple import config
from telethon import TelegramClient
from aiogram import Bot, Dispatcher, types

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.markdown)
tgbot = Dispatcher(bot)
# tgbot.start(bot_token=BOT_TOKEN)
