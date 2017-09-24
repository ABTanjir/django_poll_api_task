from rest_framework import serializers
from django.db import models
from .models import Poll
from .models import choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = choice
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Poll
        fields = '__all__'