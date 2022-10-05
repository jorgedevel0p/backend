from django.urls import path
from apps.detalle_pedidos.api.api import detalle_pedido_api_view, detalle_pedido_detail_api_view

urlpatterns = [
  path('detalle_pedido/', detalle_pedido_api_view, name = 'detalle_pedido_api'),
  path('detalle_pedido/<int:pk>', detalle_pedido_detail_api_view, name = 'detalle_pedido_detail_api_view'),
]