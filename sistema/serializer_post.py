from rest_framework import serializers
from sistema import models as sis_models
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

# MSIS'numero' => (Modelos de la aplicación 'sistema')  + Número del modelo

#1 MSIS'16'
class apiDatosUbicacion(serializers.ModelSerializer):
    class Meta:
        model = sis_models.DatosUbicacion
        fields = '__all__'

#2 MSIS'17'
class apiUbicacionRural(serializers.ModelSerializer):
    class Meta:
        model = sis_models.UbicacionRural
        fields = '__all__'

#3 MSIS'18'
class apiUbicacionUrbana(serializers.ModelSerializer):
    class Meta:
        model = sis_models.UbicacionUrbana
        fields = '__all__'

#4 MSIS'20'
class apiTelefonoCelularContacto(serializers.ModelSerializer):
    class Meta:
        model = sis_models.TelefonoCelularContacto
        fields = '__all__'

#5 MSIS'21'
class apiCorreoElectronicoContacto(serializers.ModelSerializer):
    class Meta:
        model = sis_models.CorreoElectronicoContacto
        fields = '__all__'

#6 MSIS'22'
class apiDatosContacto(serializers.ModelSerializer):
    class Meta:
        model = sis_models.DatosContacto
        fields = '__all__'

#7 MSIS'23'
class apiIdentificacionPersona(serializers.ModelSerializer):
    class Meta:
        model = sis_models.IdentificacionPersona
        fields = '__all__'

#8 MSIS'24'
class apiFileDocumentoIdentidad(serializers.ModelSerializer):
    class Meta:
        model = sis_models.FileDocumentoIdentidad
        fields = '__all__'

#9 MSIS'25'
class apiNombrePersona(serializers.ModelSerializer):
    class Meta:
        model = sis_models.NombrePersona
        fields = '__all__'

#10 MSIS'26'
class apiDatosBasicosPersona(serializers.ModelSerializer):
    class Meta:
        model = sis_models.DatosBasicosPersona
        fields = '__all__'

#11 MSIS'27'
class apiLugarNacimientoPersona(serializers.ModelSerializer):
    class Meta:
        model = sis_models.LugarNacimientoPersona
        fields = '__all__'

#12 MSIS'28'
class apiFechaNacimientoPersona(serializers.ModelSerializer):
    class Meta:
        model = sis_models.FechaNacimientoPersona
        fields = '__all__'

#13 MSIS'29'
class apiDatosNacimientoPersona(serializers.ModelSerializer):
    class Meta:
        model = sis_models.DatosNacimientoPersona
        fields = '__all__'

#14 MSIS'30'
class apiDatosComplemetariosPersona(serializers.ModelSerializer):
    class Meta:
        model = sis_models.DatosComplemetariosPersona
        fields = '__all__'

#15 MSIS'31'
class apiNombreRepresentanteLegalMenor(serializers.ModelSerializer):
    class Meta:
        model = sis_models.NombreRepresentanteLegalMenor
        fields = '__all__'

#16 MSIS'32'
class apiIdentificacionRepresentante(serializers.ModelSerializer):
    class Meta:
        model = sis_models.IdentificacionRepresentante
        fields = '__all__'

#17 MSIS'33'
class apiDatosRepresentanteLegal(serializers.ModelSerializer):
    class Meta:
        model = sis_models.DatosRepresentanteLegal
        fields = '__all__'

#18 MSIS'34'
class apiNombreColectivo(serializers.ModelSerializer):
    class Meta:
        model = sis_models.NombreColectivo
        fields = '__all__'

#19 MSIS'35'
class apiDatosbasicosColectivos(serializers.ModelSerializer):
    class Meta:
        model = sis_models.DatosbasicosColectivos
        fields = '__all__'

#20 MSIS'36'
class apiIdentificacionColectivo(serializers.ModelSerializer):
    class Meta:
        model = sis_models.IdentificacionColectivo
        fields = '__all__'

#21 MSIS'37'
class apiColectivoFDiferencial(serializers.ModelSerializer):
    class Meta:
        model = sis_models.ColectivoFDiferencial
        fields = '__all__'

#22 MSIS'38'
class apicantidadGenero(serializers.ModelSerializer):
    class Meta:
        model = sis_models.cantidadGenero
        fields = '__all__'

#23 MSIS'39'
class apicantidadSexo(serializers.ModelSerializer):
    class Meta:
        model = sis_models.cantidadSexo
        fields = '__all__'

#24 MSIS'40'
class apiTotalIntegrantes(serializers.ModelSerializer):
    class Meta:
        model = sis_models.TotalIntegrantes
        fields = '__all__'

#25 MSIS'41'
class apiNombrePersonaColectivo(serializers.ModelSerializer):
    class Meta:
        model = sis_models.NombrePersonaColectivo
        fields = '__all__'

#26 MSIS'42'
class apiIdentificacionPersonaColectivo(serializers.ModelSerializer):
    class Meta:
        model = sis_models.IdentificacionPersonaColectivo
        fields = '__all__'

#27 MSIS'43'
class apiPersonaColectivo(serializers.ModelSerializer):
    class Meta:
        model = sis_models.PersonaColectivo
        fields = '__all__'
    
#28 MSIS'44'
class apiPersonaColectivoRepresentante(serializers.ModelSerializer):
    class Meta:
        model = sis_models.PersonaColectivoRepresentante
        fields = '__all__'