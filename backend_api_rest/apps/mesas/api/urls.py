from django.urls import path
from apps.mesas.api.api import mesa_api_view, mesa_detail_api_view

urlpatterns = [
  path('mesa/', mesa_api_view, name = 'mesa_api'),
  path('mesa/<int:pk>', mesa_detail_api_view, name = 'mesa_detail_api_view'),
]