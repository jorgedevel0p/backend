from django.urls import path
from apps.facturas.api.api import factura_api_view, factura_detail_api_view

urlpatterns = [
  path('factura/', factura_api_view, name = 'factura_api'),
  path('factura/<int:pk>', factura_detail_api_view, name = 'factura_detail_api_view'),
]