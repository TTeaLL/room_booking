from rest_framework import fields, serializers
from .models import Room, Booking
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    bookings = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bookings']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_number', 'price', 'seat_number')


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'room', 'start_date', 'end_date', 'is_checkout']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(BookingSerializer, self).create(validated_data)

