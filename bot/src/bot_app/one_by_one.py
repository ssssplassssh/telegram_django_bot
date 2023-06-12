from aiogram import types
from aiogram.dispatcher import FSMContext
from . data_fetcher import get_next
from bot_app.states import GameStates
from . keyboards import inline_kb
from . import dp
from .app import bot
# We tell the handler that it works with the state object, state, * - that it works in any state, and throw it into our function
@dp.message_handler(commands='train_all', state="*")
# FSMContext - 
async def train_all(message: types.Message, state: FSMContext):
    
    # In this line, the bot remembers that we are in the random_ten_set state
    await GameStates.all_words.set()
    
    # the result of calling our backend
    # the fact that we will wait for the execution of all asynchronous functions (coroutines) and receive a random word
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
        # reply_markup - answer by keyboard
        await message.reply(f"{data['step']}. Das wort ist {data['word']}", reply_markup=inline_kb)
        
# Processing of the response from the client side (processing of the callback)
# If something from this list arrived in response, then only then this asynchronous function is executed
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