from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls', namespace='usuario')),
    path('reuniones/', include('reuniones.urls', namespace='reuniones')),
    path('sistema/', include('sistema.urls', namespace='sistema')),
    path('registro/', include('registro.urls', namespace='registro')),
]
