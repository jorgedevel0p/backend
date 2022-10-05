from django.urls import path
from apps.detalle_ordenes.api.api import detalle_orden_api_view, detalle_orden_detail_api_view

urlpatterns = [
  path('detalle_orden/', detalle_orden_api_view, name = 'detalle_orden_api'),
  path('detalle_orden/<int:pk>', detalle_orden_detail_api_view, name = 'detalle_orden_detail_api_view'),
]