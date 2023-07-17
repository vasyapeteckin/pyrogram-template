from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message


@Client.on_message(filters.incoming & filters.private & filters.chat('me'), group=1)
async def echo(client: Client, message: Message):
    print(message)
    await message.reply(text=message.text)

