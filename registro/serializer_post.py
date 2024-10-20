from rest_framework import serializers
from registro import models as reg_models
from django.contrib.contenttypes.models import ContentType
from datetime import datetime


# MREG'numero' => (Modelos de la aplicación 'registro')  + Número del modelo


#1 MREG'6'
class apiRegistro(serializers.ModelSerializer):
    class Meta:
        model = reg_models.Registro
        fields = '__all__'

#2 MREG'7'
class apiFechaTerminos(serializers.ModelSerializer):
    class Meta:
        model = reg_models.FechaTerminos
        fields = '__all__'

#3 MREG'8'
class apiTrazabilidadGeneral(serializers.ModelSerializer):
    class Meta:
        model = reg_models.TrazabilidadGeneral
        fields = '__all__'

#4 MREG'9'
class apiTrazabilidad(serializers.ModelSerializer):
    class Meta:
        model = reg_models.Trazabilidad
        fields = '__all__'

#5 MREG'10'
class apifechaDiligenciamientoFormulario(serializers.ModelSerializer):
    class Meta:
        model = reg_models.fechaDiligenciamientoFormulario
        fields = '__all__'

#6 MREG'11'
class apilugarDiligenciamientoFormulario(serializers.ModelSerializer):
    class Meta:
        model = reg_models.lugarDiligenciamientoFormulario
        fields = '__all__'

#7 MREG'12'
class apiDiligenciaFormulario(serializers.ModelSerializer):
    class Meta:
        model = reg_models.DiligenciaFormulario
        fields = '__all__'

#8 MREG'13'
class apiFormulario(serializers.ModelSerializer):
    class Meta:
        model = reg_models.Formulario
        fields = '__all__'

#9 MREG'14'
class apiFormularioIndividual(serializers.ModelSerializer):
    class Meta:
        model = reg_models.FormularioIndividual
        fields = '__all__'

#10 MREG'15'
class apiFormularioColectivo(serializers.ModelSerializer):
    class Meta:
        model = reg_models.FormularioColectivo
        fields = '__all__'

#11 MREG'16'
class apiRegistroLlamadas(serializers.ModelSerializer):
    class Meta:
        model = reg_models.RegistroLlamadas
        fields = '__all__'

#12 MREG'17'
class apiFechaHoraLlamada(serializers.ModelSerializer):
    class Meta:
        model = reg_models.FechaHoraLlamada
        fields = '__all__'

#13 MREG'18'
class apiMedioContactoLlamada(serializers.ModelSerializer):
    class Meta:
        model = reg_models.MedioContactoLlamada
        fields = '__all__'

#14 MREG'19'
class apiInformacionLlamada(serializers.ModelSerializer):
    class Meta:
        model = reg_models.InformacionLlamada
        fields = '__all__'

#15 MREG'20'
class apiTerceroRespondeLlamada(serializers.ModelSerializer):
    class Meta:
        model = reg_models.TerceroRespondeLlamada
        fields = '__all__'

#16 MREG'21'
class apiEntidadrespondeLlamada(serializers.ModelSerializer):
    class Meta:
        model = reg_models.EntidadrespondeLlamada
        fields = '__all__'

#17 MREG'22'
class apiUbicacionrespondeLlamada(serializers.ModelSerializer):
    class Meta:
        model = reg_models.UbicacionrespondeLlamada
        fields = '__all__'

#18 MREG'23'
class apiRespondeUrbanaLlamada(serializers.ModelSerializer):
    class Meta:
        model = reg_models.RespondeUrbanaLlamada
        fields = '__all__'

#19 MREG'24'
class apiRespondeRuralLlamada(serializers.ModelSerializer):
    class Meta:
        model = reg_models.RespondeRuralLlamada
        fields = '__all__'