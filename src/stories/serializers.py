from rest_framework import serializers

from .models import Story, StoryCharacter, Premise, Plot, Act, Chapter, Scene
from characters.serializers import CharacterSerializer


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = '__all__'

class PremiseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Premise
        fields = '__all__'


class PlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plot
        fields = '__all__'


class ActSerializer(serializers.ModelSerializer):

    class Meta:
        model = Act
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chapter
        fields = '__all__'

class SceneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scene
        fields = '__all__'

