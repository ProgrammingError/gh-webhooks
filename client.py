import logging

from telethon import TelegramClient

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
APP_ID = config("API_ID")
API_HASH = config("API_HASH")
BOT_TOKEN = config("TOKEN")
tgbot = TelegramClient("kensur", api_id=APP_ID, api_hash=API_HASH).start(
    bot_token=BOT_TOKEN
)

tgbot.run_until_disconnected()
