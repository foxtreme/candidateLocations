from rest_framework import viewsets
from .serializers import CitySerializer
from .models import City
# Create your views here.


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('name')
    serializer_class = CitySerializer
