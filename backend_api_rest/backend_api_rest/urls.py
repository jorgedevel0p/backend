"""backend_api_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from .views.login import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.api.urls')),
    path('api/', include('apps.productos.api.urls')),
    path('api/', include('apps.mesas.api.urls')),
    path('api/', include('apps.boletas.api.urls')),
    path('api/', include('apps.cajas.api.urls')),
    path('api/', include('apps.detalle_ordenes.api.urls')),
    path('api/', include('apps.detalle_pedidos.api.urls')),
    path('api/', include('apps.ingredientes.api.urls')),
    path('api/', include('apps.ordenes.api.urls')),
    path('api/', include('apps.platos.api.urls')),
    path('api/', include('apps.proveedores.api.urls')),

    # path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
