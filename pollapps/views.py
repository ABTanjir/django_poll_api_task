
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Poll
from .models import choice

from .serializers import PollSerializer
from .serializers import ChoiceSerializer

class PollList(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many = True)
        return Response(serializer.data)

class pollById(APIView):
    def get(self, request, p_id):
        polls = Poll.objects.filter(id = p_id)
        pserializer = PollSerializer(polls, many = True)

        choices = choice.objects.filter(choice = p_id)
        serializer = ChoiceSerializer(choices, many = True)
        
        return Response(pserializer.data + serializer.data)
