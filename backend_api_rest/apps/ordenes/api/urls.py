from django.urls import path
from apps.ordenes.api.api import orden_api_view, orden_detail_api_view
urlpatterns = [
    path('orden/', orden_api_view, name = 'orden_api'),
    path('orden/<int:pk>', orden_detail_api_view, name='orden_detail_api_view')
]