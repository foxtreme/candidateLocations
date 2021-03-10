from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cities', views.CityViewSet)
router.register(r'universities', views.UniversityViewSet)
router.register(r'economies', views.EconomyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]