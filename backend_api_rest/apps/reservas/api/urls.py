from django.urls import path
from apps.reservas.api.api import reserva_api_view, reserva_detail_api_view

urlpatterns = [
  path('reserva/', reserva_api_view, name = 'reserva_api'),
  path('reserva/<int:pk>', reserva_detail_api_view, name = 'reserva_detail_api_view'),
]