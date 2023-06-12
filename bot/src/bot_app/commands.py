# For hints
from aiogram import types

from bot_app import messages

from . import dp

# handler , the list of commands it will respond to
@dp.message_handler(commands=['start', 'help'])
# a Message type message will be sent to the input
async def send_welcome(message: types.Message):
    # we are waiting, reply - an answer
    await message.reply(messages.WELCOME_MESSAGE)