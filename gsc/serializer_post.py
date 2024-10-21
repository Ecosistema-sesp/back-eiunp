from rest_framework import serializers
from gsc import models as gsc_models

# MGSC'numero' => (Modelos de la aplicación 'gsc')  + Número del modelo


#1 MGSC'15'
class apiDireccionNotificacionPersona(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.DireccionNotificacionPersona
        fields = '__all__'

#2 MGSC'16'
class apiNombreIdentitario(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.NombreIdentitario
        fields = '__all__'

#3 MGSC'17'
class apiPersonasCargo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.PersonasCargo
        fields = '__all__'
        
#4 MGSC'18'
class apiDispacidadPersona(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.DispacidadPersona
        fields = '__all__'
        
#5 MGSC'19'
class apiGrupoEtnicoPersona(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.GrupoEtnicoPersona
        fields = '__all__'
        
#6 MGSC'20'
class apiGrupoIndigena(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.GrupoIndigena
        fields = '__all__'
        
#7 MGSC'21'
class apiEtnicoIndigena(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.EtnicoIndigena
        fields = '__all__'
        
#8 MGSC'22'
class apiOtroGrupoPersona(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.OtroGrupoPersona
        fields = '__all__'
        
#9 MGSC'23'
class apiEtnicoConcejo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.EtnicoConcejo
        fields = '__all__'
                      
#10 MGSC'24'
class apiOrganizacion(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.Organizacion
        fields = '__all__'
        
#11 MGSC'25'
class apiOtraOrganizacion(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.OtraOrganizacion
        fields = '__all__'
        
#12 MGSC'26'
class apiPersoneriaJuridica(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.PersoneriaJuridica
        fields = '__all__'
        
#13 MGSC'27'
class apiOrganizacionPersona(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.OrganizacionPersona
        fields = '__all__'
        
#14 MGSC'28'
class apiMedidaCuatelarPersona(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.MedidaCuatelarPersona
        fields = '__all__'
    
#15 MGSC'29'
class apiActividadAmbientalPersona(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.ActividadAmbientalPersona
        fields = '__all__'
        
#16 MGSC'30'
class apiIdRiesgo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.IdRiesgo
        fields = '__all__'
        
#17 MGSC'31'
class apiEvidencias(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.Evidencias
        fields = '__all__'
        
#18 MGSC'32'
class apiIdentificacionSituacion(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.IdentificacionSituacion
        fields = '__all__'
        
#19 MGSC'33'
class apiOtraSituacionRiesgo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.OtraSituacionRiesgo
        fields = '__all__'
        
#20 MGSC'34'
class apiIdentificacionMedio(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.IdentificacionMedio
        fields = '__all__'
        
#21 MGSC'35'
class apiRelatosHechos(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.RelatosHechos
        fields = '__all__'
        
#22 MGSC'36'
class apiIdPoblacion(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.IdPoblacion
        fields = '__all__'
        
#23 MGSC'37'
class apiIdentificacionPoblacionObjeto(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.IdentificacionPoblacionObjeto
        fields = '__all__'
        
#24 MGSC'38'
class apiFilePoblacion(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.FilePoblacion
        fields = '__all__'
        
#25 MGSC'39'
class apiOrganizacionPolitica(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.OrganizacionPolitica
        fields = '__all__'
        
#26 MGSC'40'
class apiCargoOrganizacion(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.CargoOrganizacion
        fields = '__all__'

#27 MGSC'41'
class apiDatosPnis(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.DatosPnis
        fields = '__all__'
        
#28 MGSC'42'
class apiConsentimiento(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.Consentimiento
        fields = '__all__'
        
#29 MGSC'43'
class apifuncionColectivo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.funcionColectivo
        fields = '__all__'
        
#30 MGSC'44'
class apiEntidadAcreditadora(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.EntidadAcreditadora
        fields = '__all__'
        
#31 MGSC'45'
class apiCantidadPersonasDiscapacidad(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.CantidadPersonasDiscapacidad
        fields = '__all__'
        
#32 MGSC'46'
class apiCantidadPersonasIndigena(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.CantidadPersonasIndigena
        fields = '__all__'
        
#33 MGSC'47'
class apicantidadPersonasAfrocolombianos(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.cantidadPersonasAfrocolombianos
        fields = '__all__'
        
#34 MGSC'48'
class apicantidadPersonasNegro(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.cantidadPersonasNegro
        fields = '__all__'
        
#35 MGSC'49'
class apicantidadPersonasRaizal(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.cantidadPersonasRaizal
        fields = '__all__'
        
#36 MGSC'50'
class apicantidadPersonasPalenquero(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.cantidadPersonasPalenquero
        fields = '__all__'
        
#37 MGSC'51'
class apicantidadPersonasRomGitano(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.cantidadPersonasRomGitano
        fields = '__all__'
        
#38 MGSC'52'
class apiCorrespondenciaColectivo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.CorrespondenciaColectivo
        fields = '__all__'
        
#39 MGSC'53'
class apiMedidaCautelarColectivo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.MedidaCautelarColectivo
        fields = '__all__'

#40 MGSC'54'
class apimcComisionInternacional(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.mcComisionInternacional
        fields = '__all__'
        
#41 MGSC'55'
class apimcCorteInternacional(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.mcCorteInternacional
        fields = '__all__'
        
#42 MGSC'56'
class apimcJuezRepublica(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.mcJuezRepublica
        fields = '__all__'
        
#43 MGSC'57'
class apiEntidadSolicitanteColectivo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.EntidadSolicitanteColectivo
        fields = '__all__'
        
#44 MGSC'58'
class apiActividadPersonaColectivo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.ActividadPersonaColectivo
        fields = '__all__'
        
#45 MGSC'59'
class apiIdPoblacionColectivo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.IdPoblacionColectivo
        fields = '__all__'
        
#46 MGSC'60'
class apiPoblacionColectivo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.PoblacionColectivo
        fields = '__all__'
    
#47 MGSC'61'
class apiPoblacionColectivoSesp(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.PoblacionColectivoSesp
        fields = '__all__'
        
#48 MGSC'62'
class apiActividadesColectivo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.ActividadesColectivo
        fields = '__all__'

#49 MGSC'63'
class apiHechoVictimizanteColectivo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.HechoVictimizanteColectivo
        fields = '__all__'
        
#50 MGSC'64'
class apiConsentimientoColectivo(serializers.ModelSerializer):
    class Meta:
        model = gsc_models.HechoVictimizanteColectivo
        fields = '__all__'