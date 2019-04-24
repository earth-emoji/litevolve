from rest_framework import serializers

from .models import Rule, History, CelestialBody, NaturalPhenomena

class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class CelestialBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = CelestialBody
        fields = '__all__'

class NaturalPhenomenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalPhenomena
        fields = '__all__'