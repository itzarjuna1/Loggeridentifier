from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client
from bot import app

from utils.logging import send_log

@app.on_message(filters.command("isloggerworking", prefixes=["/", ".", "!", "?"]))
async def logger_check(client: Client, message: Message):
    text = (
        "✅ **Logger is Working!**\n\n"
        f"👤 User: {message.from_user.mention}\n"
        f"🆔 ID: `{message.from_user.id}`\n"
        f"💬 Chat: `{message.chat.id}`\n"
        f"⚡ Command: /isloggerworking"
    )

    await send_log(client, text)
    await message.reply_text("✅ Logger GC is working!")