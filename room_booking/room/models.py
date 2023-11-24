from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    room_number = models.IntegerField(default=1)
    price = models.FloatField(default=1000)
    seat_number = models.IntegerField(default=1)

    def __str__(self) -> str:
        return str(self.room_number)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_cancelled = models.BooleanField(default=False)

