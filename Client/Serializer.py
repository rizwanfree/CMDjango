from rest_framework import serializers

from adminPanel.models import City
from .models import Client


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']

class ClientDataTableSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'contact_person', 'phone_number', 'mobile_number', 'email', 'city']