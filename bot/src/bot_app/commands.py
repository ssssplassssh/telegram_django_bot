# Для hint-ів(підсказок)
from aiogram import types

from bot_app import messages

from . import dp

# обробник хендлерів, список команд, на які він буде реагувати
@dp.message_handler(commands=['start', 'help'])
# на вхід поступить повідомлення типу Message
async def send_welcome(message: types.Message):
    # очікуємо, reply - відповідь
    await message.reply(messages.WELCOME_MESSAGE)