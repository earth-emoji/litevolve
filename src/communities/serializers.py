from rest_framework import serializers

from .models import Society, SocialGroup, Religion

class SocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Society
        fields = '__all__'

class SocialGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialGroup
        fields = '__all__'

class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = '__all__'