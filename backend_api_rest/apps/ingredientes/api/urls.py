from django.urls import path
from apps.ingredientes.api.api import ingrediente_api_view, ingrediente_detail_api_view

urlpatterns = [
  path('ingrediente/', ingrediente_api_view, name = 'ingrediente_api'),
  path('ingrediente/<int:pk>', ingrediente_detail_api_view, name = 'ingrediente_detail_api_view'),
]