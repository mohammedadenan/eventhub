from rest_framework import serializers
from django.contrib.auth.models import User
from eventhub.models import *

class Usersierializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]
        read_only_fields=["id"]

        def create(self,validated_data):
            return User.objects.create_user(**validated_data)

class BookingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookingRequest
        fields='__all__'
        read_only_fields=["user","status","rejection_resson"]

class EventSerializer(serializers.ModelSerializer):
    booking=serializers.SerializerMethodField()
    class Meta:
        model=Event
        fields=["location","amount","status","organizer","booking"]
        read_only_fields=["organizer","booking"]

    def get_booking(self,obj):
        return obj.booking.user.username

