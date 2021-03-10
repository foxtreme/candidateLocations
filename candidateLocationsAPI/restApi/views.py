from rest_framework import viewsets
from .serializers import CitySerializer, EconomySerializer, UniversitySerializer
from .models import City, Economy, University
# Create your views here.


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all().order_by('name')
    serializer_class = UniversitySerializer


class EconomyViewSet(viewsets.ModelViewSet):
    queryset = Economy.objects.all().order_by('city')
    serializer_class = EconomySerializer
