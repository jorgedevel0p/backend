from django.urls import path
from apps.boletas.api.api import boleta_api_view, boleta_detail_api_view

urlpatterns = [
  path('boleta/', boleta_api_view, name = 'boleta_api'),
  path('boleta/<int:pk>', boleta_detail_api_view, name = 'boleta_detail_api_view'),
]