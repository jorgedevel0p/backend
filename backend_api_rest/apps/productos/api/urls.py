from django.urls import path
from apps.productos.api.api import producto_api_view, producto_detail_api_view
urlpatterns = [
    path('producto/', producto_api_view, name = 'producto_api'),
    path('producto/<int:pk>', producto_detail_api_view, name = 'producto_detail_api_view'),
]