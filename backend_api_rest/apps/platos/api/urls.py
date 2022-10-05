from django.urls import path
from apps.platos.api.api import plato_api_view, plato_detail_api_view

urlpatterns = [
  path('plato/', plato_api_view, name = 'plato_api'),
  path('plato/<int:pk>', plato_detail_api_view, name = 'plato_detail_api_view'),
]