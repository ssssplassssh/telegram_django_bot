from aiogram import executor
from bot_app import dp


if __name__ == '__main__': # This construct checks whether the file was run directly and not imported as a module. This is required so that the code inside this condition is only executed when the file is run directly.
     # starts receiving messages from users using the start_polling method of the executor object. The object responsible for message processing is passed, and it is indicated that the bot should skip all unprocessed messages that have arrived to it so far
    executor.start_polling(dp, skip_updates=True)