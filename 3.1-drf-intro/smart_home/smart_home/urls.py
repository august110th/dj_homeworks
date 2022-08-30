from django.contrib import admin
from django.urls import path, include
from measurement.views import SensorInfoView, MeasurementsView, SensorView, MeasurementsCreateView, SensorCreate, MeasurementsDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),  # подключаем маршруты из приложения measurement
    path('sensors/', SensorInfoView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('measurement_upd/', MeasurementsDataView.as_view()),
    path('sensor_add/', SensorCreate.as_view()),
    path('measurement_add/', MeasurementsCreateView.as_view())
]
