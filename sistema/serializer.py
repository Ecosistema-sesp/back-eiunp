from rest_framework import serializers
from sistema import models as sis_models
from django.contrib.contenttypes.models import ContentType
from datetime import datetime


class ApiPais(serializers.ModelSerializer):         
    class Meta:
        model = sis_models.Pais                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)             

class ApiDepartamento(serializers.ModelSerializer):
    class Meta:
        model = sis_models.Departamento
        fields = '__all__'
        read_only_fields = ('__all__',)

class ApiMunicipio(serializers.ModelSerializer):
    class Meta:
        model = sis_models.Municipio
        fields = '__all__'
        read_only_fields = ('__all__',)

class ApiZona(serializers.ModelSerializer):
    class Meta:
        model = sis_models.ZonaUbicacion
        fields = '__all__'
        read_only_fields = ('__all__',)
