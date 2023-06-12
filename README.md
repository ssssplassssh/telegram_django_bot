# telegram_django_bot

This bot will help us remember the gender of German words.
We implement the backend using the Django Rest Framework and it will perform 2 functions: return a random word in German, indicating the word's gender, or return the next (from the provided pk) word in the database.
The telegram-bot task will request 10 words, check the correctness of the answers or request words in order until the training is reset or the words in the database run out.
This bot will help us remember the gender of German words.
We implement the backend using the Django Rest Framework and it will perform 2 functions: return a random word in German, indicating the word's gender, or return the next (from the provided pk) word in the database.
The telegram-bot task will request 10 words, check the correctness of the answers or request words in order until the training is reset or the words in the database run out.

Backend(Django Rest Framework) - REST API - tg bot aiogram  - Telegram Bot API - Telegram - Telegram App(mobile/Desktop)

poetry init

poetry add django

django-admin startproject bot

python3 manage.py startapp base

SuperUser:
ihor
igorrosolovskij2016@gmail.com
Tdshtratata123

poetry add psycpog2

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': '',
       'USER': 'postgres',
       'PASSWORD': 'Tdshtratata123',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}

poetry add djangorestframework

INSTALLED_APPS = [
    ...
    'rest_framework',
]

Implementation of the model and its registration with field editing.

Implementation of endpoints (url points that we can refer to in order to get a word from the database with its genus)

Backend (DRF) will work in 2 modes, giving a random word from the entire database and giving words in order.

It is desirable to put Serializers in a separate module, but if it is one, then it is possible in views.
Serializer - takes an object and turns it into some type (format) of information (json), which is convenient to transmit over the network (serialization) or save to disk.
Deserialization - we receive data from the network or read from the disk and collect an object from it, the objects are stored in the database, they are presented to us in the form of Django ORM objects.

# Folder Bot
The folder was created to implement the bot on aiogram
local_settings.py - configuration with the bot's API_KEY (don't forget to add this module to .gitignore)

app.py - file with bot
main.py - file to run the bot
__init__.py - file to designate a folder as a module and import capabilities. We also carry out imports and include logging

We create a module (commands.py) of commands, in which the handlers of the main commands will be placed, with the help of which we will communicate with the bot (/start,/help,/stop)

messages.py - file for storing messages

random_ten.py - handler of the same game mode, random 10 words

keyboards.py - file to create a keyboard

states.py - a file for information about the current state (start, random_ten, all_words)

We will access our backend using an asynchronous http client, which is already installed in aiogram(aiohttp)

data_fetcher.py - the file will contain the implementation of the get_random() function

In order for the state we are in to be stored in app.py, dp = Dispatcher(bot, storage=MemoryStorage()) - the place where we store data about the state, the simplest way (although not reliable). The second method is Redis

Next, the implementation of the function of passing through all words (after that)