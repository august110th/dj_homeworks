from rest_framework import serializers
from .models import Sensor, Measurements


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurements
        fields = ['temperature', 'created_at', 'sensor']


class SensorDataSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

