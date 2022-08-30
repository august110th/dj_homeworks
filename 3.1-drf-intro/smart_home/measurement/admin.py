from django.contrib import admin
from .models import Sensor, Measurements


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass


@admin.register(Measurements)
class MeasurementsAdmin(admin.ModelAdmin):
    pass
