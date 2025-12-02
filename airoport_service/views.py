from rest_framework import viewsets
from .models import Country, Airline, Airport, Airplane, Flight, Ticket
from .serializers import CountrySerializer, AirlineSerializer, AirportSerializer, AirportListSerializer, AirplaneSerializer, FlightSerializer, FlightListSerializer, TicketSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return AirportListSerializer
        return AirportSerializer

class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return FlightListSerializer
        return FlightSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer