from django.urls import path
from apps.proveedores.api.api import proveedor_api_view, proveedor_detail_api_view

urlpatterns = [
  path('proveedor/', proveedor_api_view, name = 'proveedor_api'),
  path('proveedor/<int:pk>', proveedor_detail_api_view, name = 'proveedor_detail_api_view'),
]