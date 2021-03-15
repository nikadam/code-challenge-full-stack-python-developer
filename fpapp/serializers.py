from rest_framework import serializers

from fpapp.models import FavoriteList, CurrentList


class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = '__all__'


class CurrentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentList
        fields = '__all__'
