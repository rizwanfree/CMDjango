from rest_framework import serializers

from adminPanel.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']
