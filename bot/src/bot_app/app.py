from aiogram import Bot, Dispatcher, executor
from bot_app.local_settings import API_KEY
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Створює об'єкт Bot з використанням API_KEY. Об'єкт використовується для взаємодії з Telegram Bot API.Токен бота передається як параметр конструктора.
bot = Bot(API_KEY) 

# Створює об'єкт Dispatcher з використанням об'єкта bot. Об'єкт відповідає за обробку повідомлень та подій, що надходять до бота.
dp = Dispatcher(bot, storage=MemoryStorage())

