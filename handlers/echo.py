from loader import bot
from telebot.types import Message


@bot.message_handler(content_types=["text"])
async def echo(message: Message):
    text = message.text
    await bot.send_message(chat_id=message.from_user.id, text=text)
