from rest_framework import serializers

from .models import (CelestialBody, Dimension, Element, NaturalLaw,
                     NaturalObject, NaturalPhenomena, Particle, Place, Season,
                     Species, Universe)


class UniverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universe
        fields = '__all__'

class DimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimension
        fields = '__all__'

class NaturalLawSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaturalLaw
        fields = '__all__'


class ParticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Particle
        fields = '__all__'


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
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


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
