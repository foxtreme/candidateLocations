from rest_framework import viewsets
from .serializers import CitySerializer, UniversitySerializer
from .models import City, University
# Create your views here.


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all().order_by('name')
    serializer_class = UniversitySerializer

