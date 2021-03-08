from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import House, Thermostat, Room, Light

__all__ = [
    'HouseSerializer',
    'ThermostatSerializer',
    'RoomSerializer',
    'LightSerializer',
]


class AbstractSerializer(serializers.HyperlinkedModelSerializer):
    """
    Base serializer.
    """

    class Meta:
        model = None
        ordering = ['-id']
        fields = '__all__'


class ThermostatSerializer(AbstractSerializer):
    """
    Thermostat model serializer
    """

    class Meta:
        model = Thermostat
        fields = '__all__'


class LightSerializer(AbstractSerializer):
    """
    Light model serializer
    """

    class Meta:
        model = Light
        fields = '__all__'


class RoomSerializer(AbstractSerializer):
    """
    Room model serializer
    """

    lights = LightSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'


class HouseSerializer(AbstractSerializer):
    """
    House model serializer.
    """
    #
    # Calling House API will give all the details for the dashboard
    # instead of calling multiple APIs
    #
    thermostats = ThermostatSerializer(many=True, read_only=True)
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = '__all__'
