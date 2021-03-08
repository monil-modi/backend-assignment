from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import House, Thermostat, Room, Light
from .serializers import *


class BaseViewSet(viewsets.ModelViewSet):
    """
    The base view set
    """
    queryset = None
    serializer_class = None

    #
    # Use basic superuser authentication for secure use of the API
    #
    permission_classes = [IsAuthenticated]


class HouseViewSet(BaseViewSet):
    """
    A View for House
    """

    queryset = House.objects.all().order_by('-id')
    serializer_class = HouseSerializer


class RoomViewSet(BaseViewSet):
    """
    A View for Room
    """

    queryset = Room.objects.all().order_by('-id')
    serializer_class = RoomSerializer


class ThermostatViewSet(BaseViewSet):
    """
    A View for Thermostat
    """

    queryset = Thermostat.objects.all().order_by('-id')
    serializer_class = ThermostatSerializer


class LightViewSet(BaseViewSet):
    """
    A View for Light.
    """

    queryset = Light.objects.all().order_by('-id')
    serializer_class = LightSerializer
