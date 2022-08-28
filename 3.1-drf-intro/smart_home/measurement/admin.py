from django.contrib import admin
from .models import Sensor, Measurements

# Register your models here.


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass


@admin.register(Measurements)
class MeasurementsAdmin(admin.ModelAdmin):
    pass
