from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client

@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply_text("👋 Hello! Logger Bot is running.")