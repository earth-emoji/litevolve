from rest_framework import serializers

from .models import Rule, CelestialBody, NaturalPhenomena, Season, NaturalObject, Species

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'

class CelestialBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = CelestialBody
        fields = '__all__'

class NaturalPhenomenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalPhenomena
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

class NaturalObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalObject
        fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'