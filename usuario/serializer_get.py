from rest_framework import serializers
from usuario import models as usr_models
from django.contrib.contenttypes.models import ContentType
from datetime import datetime


# MUSR'numero' => (Modelos de la aplicación 'sistema')  + Número del modelo


# SERIALIZAORES DE LAS TABLAS ESTÁTICAS

#1 MUSR'1'
class ApiTipoVinculacion(serializers.ModelSerializer):         
    class Meta:
        model = usr_models.TipoVinculacion   
        fields = '__all__'                         
        read_only_fields = ('__all__',)             

#2 MUSR'2'
class ApiDependencia(serializers.ModelSerializer):         
    class Meta:
        model = usr_models.Dependencia   
        fields = '__all__'                         
        read_only_fields = ('__all__',)    

#3 MUSR'3'
class ApiGrupo(serializers.ModelSerializer):         
    class Meta:
        model = usr_models.Grupo   
        fields = '__all__'                         
        read_only_fields = ('__all__',)    
        
#4 MUSR'4'
class ApiRol(serializers.ModelSerializer):         
    class Meta:
        model = usr_models.Rol   
        fields = '__all__'                         
        read_only_fields = ('__all__',)    