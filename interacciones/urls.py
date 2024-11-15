from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('interacciones.urls')),  # Esta línea incluye las URLs de "interacciones"
]
]
