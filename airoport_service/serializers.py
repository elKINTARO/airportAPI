from rest_framework import serializers
from .models import Country, Airline, Airport, Airplane, Flight, Ticket

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('id', 'name', 'country', 'airlines')

class AirportListSerializer(AirportSerializer):
    country = serializers.SlugRelatedField(read_only=True, slug_field='name')
    airlines = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ('id', 'name', 'airline', 'capacity')

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class FlightListSerializer(FlightSerializer):
    origin = serializers.SlugRelatedField(read_only=True, slug_field='name')
    destination = serializers.SlugRelatedField(read_only=True, slug_field='name')
    airplane = serializers.SlugRelatedField(read_only=True, slug_field='name')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'flight', 'passanger', 'row', 'seat', 'status', 'booking_time')
        read_only_fields = ('booking_time', )