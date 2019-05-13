from rest_framework import serializers

from .models import Story, StoryCharacter
from characters.serializers import CharacterSerializer

class StorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Story
        fields = '__all__'

    