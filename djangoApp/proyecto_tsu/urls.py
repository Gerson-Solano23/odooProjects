from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion_tsu.urls')),  # Incluye las rutas de tu app
]