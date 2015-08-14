from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        field = ('id', 'name')


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        field = ('id', 'name', 'abbr_name')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        field = ('id', 'name')


class ZipSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    state = StateSerializer()
    city = CitySerializer()

    class Meta:
        model = Zip
        field = ('id', 'country', 'state', 'city', 'name')