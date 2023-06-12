import random
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseNotFound


from base import models


# Create your views here.

class WordSerializator(serializers.ModelSerializer):
    
    # вказуємо об'кти якої моделі ми збираємося серіалізувати
    class Meta:
        model = models.Word
        # pk - це id
        fields = ['pk', 'gender', 'word']
        
# Створюємо в'ю, яке буде приймати запит користувача і віддавати випадкове слово(серіалізоване), придатне до передачі по протоколу REST API

class RandomWord(APIView):
    # get - метод для звертання(отримання)
    def get(self, *args, **kwargs):
        # отримуємо усі слова
        all_words = models.Word.objects.all()
        # Вибираємо рандомно слово
        ranfom_word = random.choice(all_words)
        # Серіалізуємо його і робимо його об'єктом
        serialized_random_word = WordSerializator(ranfom_word, many=False)
        # many=False - вказує що це один об'єкт, а не список 
        # Повертаємо це у вигляді відповіді цей серіалізований об'єкт, що був рандомно вибраний 
        return Response(serialized_random_word.data)
  
  
# Клас, який буде віддавати наступне слово, щоб була можливість пройти усі слова в БД одне за одним
class NextWord(APIView):
    # pk - потрібне як id попереднього слова, щоб видати наступне
    # format=None з документації
    def get(self, request, pk, format=None):
        # вибираємо наступне слово від поточного слова(по pk)
        # бере всі слово у яких pk більше ніж те що нам надіслали
        # first() - зі всіх наступних слів беремо перше
        word = models.Word.objects.filter(pk__gt=pk).first()
        # якщо нічого не надіслалося
        if not word:
            return HttpResponseNotFound()
        # якщо об'єкт існує, то серіалізуємо його і відповідаємо
        ser_word = WordSerializator(word, many=False)
        return Response(ser_word.data)