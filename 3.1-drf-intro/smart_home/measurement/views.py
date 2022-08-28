# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Sensor, Measurements
from .serializers import SensorSerializer, MeasurementsSerializer, SensorDataSerializer


class SensorInfoView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request, **kwargs):
        return Response(Sensor.objects.all())


class MeasurementsView(ListCreateAPIView):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer

    def post(self, request, **kwargs):
        return Response(Measurements.objects.all())


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDataSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class SensorCreate(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDataSerializer

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MeasurementsDataView(RetrieveUpdateAPIView):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer
