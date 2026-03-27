from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client
from bot import app

@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply_text("👋 Hello! Logger Bot is running.")