from pyrogram import Client
import config

app = Client(
    "logger-bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# Import handlers
import handlers.logger
import handlers.start

print("Bot Started...")

app.run()