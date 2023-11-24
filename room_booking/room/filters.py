import django_filters
from .models import Room


class RoomFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter(field_name='price')
    seat_number = django_filters.NumberFilter(field_name='seat_number')

    class Meta:
        model = Room
        fields = ['price', 'seat_number']