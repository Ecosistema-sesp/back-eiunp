from django.urls import path, include
from usuario import views
from rest_framework import routers

app_name = 'usuario'

urlpatterns = [
    path('', views.Inicio, name='inicio' ),
    #path('usuario', include(routers.urls)),
]