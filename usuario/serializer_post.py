from rest_framework import serializers
from usuario import models as usr_models
from django.contrib.contenttypes.models import ContentType


# MUSR'numero' => (Modelos de la aplicación 'sistema')  + Número del modelo


#1 MSIS'5'
class apiTelefonoCelularContactoUsuario(serializers.ModelSerializer):
    class Meta:
        model = usr_models.TelefonoCelularContactoUsuario
        fields = '__all__'

#2 MSIS'6'
class apiCorreoElectronicoContactoUsuario(serializers.ModelSerializer):
    class Meta:
        model = usr_models.CorreoElectronicoContactoUsuario
        fields = '__all__'

#3 MSIS'7'
class apiDatosContactoUsuario(serializers.ModelSerializer):
    class Meta:
        model = usr_models.DatosContactoUsuario
        fields = '__all__'

#4 MSIS'8'
class apiDatosUbicacionUsuario(serializers.ModelSerializer):
    class Meta:
        model = usr_models.DatosUbicacionUsuario
        fields = '__all__'

#5 MSIS'9'
class apiUbicacionRural(serializers.ModelSerializer):
    class Meta:
        model = usr_models.UbicacionRural
        fields = '__all__'

#6 MSIS'10'
class apiUbicacionUrbana(serializers.ModelSerializer):
    class Meta:
        model = usr_models.UbicacionUrbana
        fields = '__all__'

#7 MSIS'11'
class apiIdentificacionUsuario(serializers.ModelSerializer):
    class Meta:
        model = usr_models.IdentificacionUsuario
        fields = '__all__'

#8 MSIS'12'
class apiNombrePersonaUsuario(serializers.ModelSerializer):
    class Meta:
        model = usr_models.NombrePersonaUsuario
        fields = '__all__'

#9 MSIS'13'
class apiDatosBasicosUsuario(serializers.ModelSerializer):
    class Meta:
        model = usr_models.DatosBasicosUsuario
        fields = '__all__'

#10 MSIS'14'
class apiDatosComplementariosUsuario(serializers.ModelSerializer):
    class Meta:
        model = usr_models.DatosComplementariosUsuario
        fields = '__all__'

#11 MSIS'15'
class apiContratoContratista(serializers.ModelSerializer):
    class Meta:
        model = usr_models.ContratoContratista
        fields = '__all__'

#12 MSIS'16'
class apiResolucionFuncionario(serializers.ModelSerializer):
    class Meta:
        model = usr_models.ResolucionFuncionario
        fields = '__all__'

#13 MSIS'17'
class apiPerfilUsuario(serializers.ModelSerializer):
    class Meta:
        model = usr_models.PerfilUsuario
        fields = '__all__'