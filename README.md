# telegram_django_bot

BackEnd(Django Rest Framework) - REST API - tg bot aiogram  - Telegram Bot API- Telegram - Telegram App(mobile/Desktop)

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

Реалізація моделі і її реєстрація з редагуванням полів. 

Реалізація ендпоінтів(точки url по яким ми можемо звернутися, для того щоб отримати слово з БД з його родом)

Backend(DRF) буде працювати в 2 режимах, віддача випадкового слова з всієї БД і віддача слів по порядку.

Serializers бажано викладати в окремий модуль, але якщо він один, то можна в views.
Serializer - бере об'єкт і перетворює його в якийсь вид(формат) інформації(json), який комфортно передати по мережі(серіалізація), або зберегти на диск.
Десеріалізація - приймаємо дані з мережі або зчитуємо з диску і збираємо з цього об'єкт, об'єкти зберігаються в БД, представлються нам у вигляді Django ORM-об'єктів.