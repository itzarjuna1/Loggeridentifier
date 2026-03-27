from pyrogram import Client
import config

async def send_log(client: Client, text: str):
    try:
        await client.send_message(config.LOGGER_GC, text)
    except Exception as e:
        print(f"Logger Error: {e}")