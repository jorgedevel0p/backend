from django.urls import path
from apps.cajas.api.api import caja_api_view, caja_detail_api_view

urlpatterns = [
  path('caja/', caja_api_view, name = 'caja_api'),
  path('caja/<int:pk>', caja_detail_api_view, name = 'caja_detail_api_view'),
]