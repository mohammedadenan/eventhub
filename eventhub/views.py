from django.shortcuts import render
from eventhub.models import *
from eventhub.serializer import *
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework.response import Response
from rest_framework import status
from eventhub.permissions import IsOrganizer,IsCustomer

# Create your views here.


class SignUpViewSet(ViewSet):
    def create(self,request):
        dser=Usersierializer(data=request.data)
        if dser.is_valid():
            User.objects.create_user(**dser.validated_data)
            return Response(data=dser.data,status=status.HTTP_201_CREATED)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)


class BookingModelViewSet(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsCustomer]
    serializer_class=BookingRequestSerializer
    queryset=BookingRequest.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class EventViewSet(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOrganizer]
    serializer_class=EventSerializer
    queryset=Event.objects.all()

    def perform_create(self, serializer):
        return serializer.save(organizer=self.request.user)
   
    def get_queryset(self):
        return self.queryset.filter(organizer=self.request.user)

    
class BookingHistory(APIView):

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,):
        bookings=BookingRequest.objects.filter(user=request.user.id)
        serializer=BookingRequestSerializer(bookings,many=True)
        return Response(serializer.data)