from rest_framework import serializers

from .models import Character, CharacterAppearance, CharacterPsychology, CharacterRelationship


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class CharacterAppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterAppearance
        fields = '__all__'


class CharacterPsychologySerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterPsychology
        fields = '__all__'


class CharacterRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterRelationship
        fields = '__all__'
