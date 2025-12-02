from django.urls import path, include
from rest_framework import routers
from .views import CountryViewSet, AirlineViewSet, AirportViewSet, AirplaneViewSet, FlightViewSet, TicketViewSet

router = routers.DefaultRouter()
router.register('countries', CountryViewSet)
router.register('airlines', AirlineViewSet)
router.register('airports', AirportViewSet)
router.register('airplanes', AirplaneViewSet)
router.register('flights', FlightViewSet)
router.register('tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]