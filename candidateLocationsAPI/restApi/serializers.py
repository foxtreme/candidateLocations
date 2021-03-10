from rest_framework import serializers
from .models import City, University, Economy


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'province', 'country', 'universities')


class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = ('id', 'name', 'type')


class EconomySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Economy
        fields = ('city', 'unemployment_rate', 'activities')
