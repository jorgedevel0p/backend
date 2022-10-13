from django.urls import path
from apps.pedidos_proveedor.api.api import pedido_proveedor_api_view, pedido_proveedor_detail_api_view

urlpatterns = [
  path('pedido_proveedor/', pedido_proveedor_api_view, name = 'pedido_proveedor_api'),
  path('pedido_proveedor/<int:pk>', pedido_proveedor_detail_api_view, name = 'pedido_proveedor_detail_api_view'),
]