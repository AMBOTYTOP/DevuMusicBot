from pyrogram import filters
from pyrogram.types import Message

from DevuMusicBot import app
from DevuMusicBot.core.call import PubliceMusic

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await PubliceMusic.stop_stream_force(message.chat.id)
