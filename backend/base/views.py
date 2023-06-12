import random
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseNotFound

from base import models

# Create your views here.

class WordSerializator(serializers.ModelSerializer):
    
    # specify the objects of which model we are going to serialize
    class Meta:
        model = models.Word
        # pk - it's id
        fields = ['pk', 'gender', 'word']
        
# We create a view that will accept a user request and return a random word (serialized) suitable for passing through the REST API protocol

class RandomWord(APIView):
    # get - method for calling (getting)
    def get(self, *args, **kwargs):
        # we get all the words
        all_words = models.Word.objects.all()
        # We choose a random word
        ranfom_word = random.choice(all_words)
        # We serialize it and make it an object
        serialized_random_word = WordSerializator(ranfom_word, many=False)
        # many=False - indicates that this is a single object, not a list
        # We return this serialized object that was randomly selected as an answer
        return Response(serialized_random_word.data)
  
  
# A class that will return the next word so that it is possible to go through all the words in the database one by one
class NextWord(APIView):
    # pk - is needed as the id of the previous word to output the next one
    # format=None from the documentation
    def get(self, request, pk, format=None):
        # choose the next word from the current word (by pk)
        # takes all the words of those whose pk is more than what was sent to us
        # first() - we take the first of all the following words
        word = models.Word.objects.filter(pk__gt=pk).first()
        # if nothing was sent
        if not word:
            return HttpResponseNotFound()
        # if the object exists, then we serialize it and respond
        ser_word = WordSerializator(word, many=False)
        return Response(ser_word.data)