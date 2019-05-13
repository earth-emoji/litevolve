from rest_framework import serializers

from .models import (NaturalLaw,
                     CelestialBody,
                     NaturalPhenomena,
                     Season,
                     NaturalObject,
                     Species,
                     Place,
                     Universe)


class UniverseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universe
        fields = '__all__'


class NaturalLawSerializer(serializers.ModelSerializer):
    class Meta: 
        model = NaturalLaw
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

# many to many serializers
class UniverseLawSerializer(serializers.Serializer):
    natural_law = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, instance, validated_data):
        # .save() will update the existing `comment` instance.
        # serializer = UniverseLawSerializer(universe, data=data)
        instance.natural_laws.add(validated_data.get('natural_law'))
        return instance
