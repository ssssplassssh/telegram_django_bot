from aiogram import types
from aiogram.dispatcher import FSMContext
from . data_fetcher import get_random, get_next
from bot_app.states import GameStates
from . keyboards import inline_kb
from . import dp
from .app import bot
# Вказуємо хендлерові що він працює з об'єктом стану, state, * - що він працює в будь-якому стані, і закидаємо це в нашу функцію
@dp.message_handler(commands='train_all', state="*")
# FSMContext - 
async def train_all(message: types.Message, state: FSMContext):
    
    # В цьому рядку бот запам'ятовує, що ми знаходимося в стані random_ten_set
    await GameStates.all_words.set()
    
    # результат звернення до нашого бекенду
    # те що ми дочекаємося виконання усіх асинхронних функцій(корутини) і отримаємо рандомне слово
    res = await get_next(0)
    # Передаємо дані з бекенда в стан, щоб наш бот запам'ятав в якому стані ми знаходимося
    if not res:
        await GameStates.start.set()
        await message.reply('All is done')
        return
    async with state.proxy() as data:
        data['step'] = 1
        data['pk'] = 1
        data['answer'] = res.get('gender')
        data['word'] = res.get('word')
        # reply_markup - відповідь клавіатурою
        await message.reply(f"{data['step']}. Das wort ist {data['word']}", reply_markup=inline_kb)
        
# Обробка відповіді зі сторони клієнта(обробка колбека)
# Якщо у відповідь прилетіло щось з даного списку, то тільки тоді виконується дана асинхронна функція
@dp.callback_query_handler(lambda c: c.data in ['das', 'die', 'der'], state=GameStates.all_words)
async def button_click_call_back_all(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data['answer']:
            await bot.send_message(callback_query.from_user.id, 'Ya\n')
            res = await get_next(data['pk'])
            if res:
                data['step'] += 1
                data['answer'] = res.get('gender')
                data['word'] = res.get('word')
                data['pk'] = res.get('pk')
                await bot.send_message(callback_query.from_user.id, f"{data['step']}. Das wort ist {data['word']}", reply_markup=inline_kb)
            else:
                await bot.send_message(callback_query.from_user.id, 'The game is over')
                await GameStates.start.set()
        else:
            await bot.send_message(callback_query.from_user.id, f'Nein\n', reply_markup=inline_kb)