from django.db import models
from django.conf import settings

class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Countries"

class Airline(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Airport(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='airports') #країна одна, аєропортів багато
    airlines = models.ForeignKey(Airline, on_delete=models.CASCADE)#мені ту мені
    def __str__(self):
        return f"{self.name} {self.country.name}"

class Airplane(models.Model):
    name = models.CharField(max_length=50)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='airplanes')#одна авіакомпанія, багато літаків
    capacity = models.IntegerField(default=215)
    def __str__(self):
        return f"{self.name} {self.airline.name}"

class Flight(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = 'scheduled', 'Scheduled'
        BOARDING = 'boarding', 'Boarding'
        DEPARTED = 'departed', 'Departed'
        DELAYED = 'delayed', 'Delayed'
        CANCELLED = 'cancelled', 'Cancelled'
    route_number = models.CharField(max_length=50)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='flights')#один літак, багато рейсів
    departure_date = models.DateField()
    arrival_date = models.DateField()
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')

    status = models.CharField(max_length=16, choices=Status.choices, default=Status.SCHEDULED)
    def __str__(self):
        return f"{self.route_number} {self.origin} -> {self.destination}"

class Ticket(models.Model):
    class Status(models.TextChoices):
        BOOKED = 'booked', 'Booked'
        CANCELLED = 'cancelled', 'Cancelled'
        USED = 'used', 'Used'

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='tickets')
    passanger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='tickets')
    row = models.IntegerField()
    seat = models.CharField(max_length=4)

    status = models.CharField(max_length=16, choices=Status.choices, default=Status.BOOKED)
    booking_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('flight', 'row', 'seat')#унікальність місця
    def __str__(self):
        return f"Ticket for {self.flight} (Seat{self.row} {self.seat})"