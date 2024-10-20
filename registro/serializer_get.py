from rest_framework import serializers
from registro import models as reg_models

# MREG'numero' => (Modelos de la aplicación 'registro')  + Número del modelo


# SERIALIZAORES DE LAS TABLAS ESTÁTICAS

#1 MREG'1'
class apiEstadoGeneral(serializers.ModelSerializer):
    class Meta:
        model = reg_models.EstadoGeneral
        fields = '__all__'
        read_only_fields = ('__all__',)

#2 MREG'2'
class apiEstadoEspecifico(serializers.ModelSerializer):
    class Meta:
        model = reg_models.EstadoEspecifico
        fields = '__all__'
        read_only_fields = ('__all__',)

#3 MREG'3'
class apiTipoRuta(serializers.ModelSerializer):
    class Meta:
        model = reg_models.TipoRuta
        fields = '__all__'
        read_only_fields = ('__all__',)

#4 MREG'4'
class apiCanalSolicitud(serializers.ModelSerializer):
    class Meta:
        model = reg_models.CanalSolicitud
        fields = '__all__'
        read_only_fields = ('__all__',)


#5 MREG'5'
class apiTipoResultadoLlamada(serializers.ModelSerializer):
    class Meta:
        model = reg_models.TipoResultadoLlamada
        fields = '__all__'
        read_only_fields = ('__all__',)



# SEERIALIZADORES DE LAS TABLAS DINÁMICAS QUE VAN MOSTRAR DATOS