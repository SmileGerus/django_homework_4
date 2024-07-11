from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SensorList, SensorDetail, MeasurementList, MeasurementDetail

urlpatterns = [
    path('sensors/', SensorList.as_view()),
    path('sensors/<int:pk>/', SensorDetail.as_view()),
    path('measurements/', MeasurementList.as_view()),
    path('measurements/<int:pk>/', MeasurementDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
