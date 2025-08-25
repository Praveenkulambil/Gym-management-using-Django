from django.urls import path
from . import views

urlpatterns = [
    path('add_measurement/', views.add_measurement, name='add_measurement'),
    path('measurement_list/', views.measurement_list, name='measurement_list'),
]
