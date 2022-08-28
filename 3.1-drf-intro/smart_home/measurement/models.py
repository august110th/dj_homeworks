from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    objects = models.Manager


class Measurements(models.Model):
    temperature = models.IntegerField()
    created_at = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    objects = models.Manager
