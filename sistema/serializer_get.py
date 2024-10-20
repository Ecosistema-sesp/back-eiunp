from rest_framework import serializers
from sistema import models as sis_models
from django.contrib.contenttypes.models import ContentType
from datetime import datetime


# MSIS'numero' => (Modelos de la aplicación 'sistema')  + Número del modelo


# SERIALIZAORES DE LAS TABLAS ESTÁTICAS
 
#1 MSIS'1'
class ApiPais(serializers.ModelSerializer):         
    class Meta:
        model = sis_models.Pais                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)             

#2 MSIS'2'
class ApiDepartamento(serializers.ModelSerializer):
    class Meta:
        model = sis_models.Departamento
        fields = '__all__'
        read_only_fields = ('__all__',)

#3 MSIS'3'
class ApiMunicipio(serializers.ModelSerializer):
    class Meta:
        model = sis_models.Municipio
        fields = '__all__'
        read_only_fields = ('__all__',)

#4 MSIS'4'
class ApiZona(serializers.ModelSerializer):
    class Meta:
        model = sis_models.ZonaUbicacion
        fields = '__all__'
        read_only_fields = ('__all__',)

#5 MSIS'5'
class ApiTipoIdentificacion(serializers.ModelSerializer):
    class Meta:
        model = sis_models.TipoIdentificacion
        fields = '__all__'
        read_only_fields = ('__all__',)

#6 MSIS'6'
class ApiTipoGenero(serializers.ModelSerializer):
    class Meta:
        model = sis_models.TipoGenero
        fields = '__all__'
        read_only_fields = ('__all__',)

#7 MSIS'7'
class ApiEstadoCivil(serializers.ModelSerializer):
    class Meta:
        model = sis_models.EstadoCivil
        fields = '__all__'
        read_only_fields = ('__all__',)

#8 MSIS'8'
class ApiGpRh(serializers.ModelSerializer):
    class Meta:
        model = sis_models.GpRh
        fields = '__all__'
        read_only_fields = ('__all__',)

#9 MSIS'9'
class ApiFondoPensiones(serializers.ModelSerializer):
    class Meta:
        model = sis_models.FondoPensiones
        fields = '__all__'
        read_only_fields = ('__all__',)

#10 MSIS'10'
class ApiEps(serializers.ModelSerializer):
    class Meta:
        model = sis_models.Eps
        fields = '__all__'
        read_only_fields = ('__all__',)

#11 MSIS'11'
class apiTipoSexo(serializers.ModelSerializer):
    class Meta:
        model = sis_models.TipoSexo
        fields = '__all__'
        read_only_fields = ('__all__',)

#12 MSIS'12'
class apiTipoOrientacionSexual(serializers.ModelSerializer):
    class Meta:
        model = sis_models.TipoOrientacionSexual
        fields = '__all__'
        read_only_fields = ('__all__',)

#13 MSIS'13'
class apiTipoRangoEtario(serializers.ModelSerializer):
    class Meta:
        model = sis_models.TipoRangoEtario
        fields = '__all__'
        read_only_fields = ('__all__',)

#14 MSIS'14'
class apiTipoFactorDiferencial(serializers.ModelSerializer):
    class Meta:
        model = sis_models.TipoFactorDiferencial
        fields = '__all__'
        read_only_fields = ('__all__',)

#15 MSIS'15'
class apiTipoIdentificacionColectivo(serializers.ModelSerializer):
    class Meta:
        model = sis_models.TipoIdentificacionColectivo
        fields = '__all__'
        read_only_fields = ('__all__',)


# SEERIALIZADORES DE LAS TABLAS DINÁMICAS QUE VAN MOSTRAR DATOS

