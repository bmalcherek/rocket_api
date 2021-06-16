from rest_framework import serializers
from . import models


class RocketModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RocketModel
        fields = '__all__'


class BoosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booster
        fields = '__all__'


class LaunchPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LaunchPlatform
        fields = '__all__'


class PayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payload
        fields = '__all__'


class LaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Launch
        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Token
        fields = '__all__'
