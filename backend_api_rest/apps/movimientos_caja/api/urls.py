from django.urls import path
from apps.movimientos_caja.api.api import movimiento_caja_api_view, movimiento_caja_detail_api_view

urlpatterns = [
  path('movimiento_caja/', movimiento_caja_api_view, name = 'movimiento_caja_api'),
  path('movimiento_caja/<int:pk>', movimiento_caja_detail_api_view, name = 'movimiento_caja_detail_api_view'),
]