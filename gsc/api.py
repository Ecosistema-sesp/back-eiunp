from rest_framework import viewsets
from gsc import models as gsc_models
from gsc import serializer_get as gscg_serializer
from gsc import serializer_post as gscp_serializer

#  MGSC'numero' => (Modelos de la aplicación 'gsc')  + Número del modelo
#  SPGSC'numero' => (Serializador post de la aplicación 'gsc) + Número de la serialización
#  SGGSC'numero' => (Serializador get de la aplicación 'gsc) + Número de la serialización


#1 MSIS'1' SGSIS'1'
class TipoDiscapacidadPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.TipoDiscapacidad.objects.all()          
    serializer_class = gscg_serializer.ApiTipoDiscapacidad                                
    http_method_names = ['get']

#2 MSIS'2' SGSIS'2'
class TipoGrupoEtnicoPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.TipoGrupoEtnico.objects.all()          
    serializer_class = gscg_serializer.ApiTipoGrupoEtnico                                
    http_method_names = ['get']


#3 MSIS'3' SGSIS'3'
class TipoOrganizacionPersonaPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.TipoOrganizacionPersona.objects.all()          
    serializer_class = gscg_serializer.ApiTipoOrganizacionPersona                                
    http_method_names = ['get']

#4 MSIS'4' SGSIS'4'
class TipoMedidaCautelarPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.TipoMedidaCautelar.objects.all()          
    serializer_class = gscg_serializer.ApiTipoMedidaCautelar                                
    http_method_names = ['get']

#5 MSIS'5' SGSIS'5'
class TipoSituacionesRiesgoPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.TipoSituacionesRiesgo.objects.all()          
    serializer_class = gscg_serializer.ApiTipoSituacionesRiesgo                                
    http_method_names = ['get']
    
#6 MSIS'6' SGSIS'6'
class TipoMediosSituacionPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.TipoMediosSituacion.objects.all()          
    serializer_class = gscg_serializer.ApiTipoMediosSituacion                                
    http_method_names = ['get']

#7 MSIS'7' SGSIS'7'
class TipoPoblacionPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.TipoPoblacion.objects.all()          
    serializer_class = gscg_serializer.ApiTipoPoblacion                                
    http_method_names = ['get']
    
#8 MSIS'8' SGSIS'8'
class PoblacionObjetoPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.PoblacionObjeto.objects.all()          
    serializer_class = gscg_serializer.ApiPoblacionObjeto                                
    http_method_names = ['get']
    
#9 MSIS'9' SGSIS'9'
class TipoCategoriaOrganizacionPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.TipoCategoriaOrganizacion.objects.all()          
    serializer_class = gscg_serializer.ApiTipoCategoriaOrganizacion                                
    http_method_names = ['get']
    
#10 MSIS'10' SGSIS'10'
class CategoriaPnisPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.CategoriaPnis.objects.all()          
    serializer_class = gscg_serializer.ApiCategoriaPnis                                
    http_method_names = ['get']
    
#11 MSIS'11' SGSIS'11'
class tipoEntidadAcreditadoraPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.tipoEntidadAcreditadora.objects.all()          
    serializer_class = gscg_serializer.ApitipoEntidadAcreditadora                                
    http_method_names = ['get']
    
#12 MSIS'12' SGSIS'12'
class PoblacionGeneralColectivoPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.PoblacionGeneralColectivo.objects.all()          
    serializer_class = gscg_serializer.ApiPoblacionGeneralColectivo                                
    http_method_names = ['get']
    
#13 MSIS'13' SGSIS'13'
class TipoPoblacionColectivoPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.TipoPoblacionColectivo.objects.all()          
    serializer_class = gscg_serializer.ApiTipoPoblacionColectivo                                
    http_method_names = ['get']
    
#14 MSIS'14' SGSIS'14'
class TipoPoblacionSespPermiso(viewsets.ModelViewSet):                                   
    queryset = gsc_models.TipoPoblacionSesp.objects.all()          
    serializer_class = gscg_serializer.ApiTipoPoblacionSesp                                
    http_method_names = ['get']
    
#15 MGSC'15' SPGSC'1'
class DireccionNotificacionPersonaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.DireccionNotificacionPersona.objects.all()
    serializer_class = gscp_serializer.apiDireccionNotificacionPersona
    http_method_names = ['post','put']
    
#16 MGSC'16' SPGSC'2'
class NombreIdentitarioPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.NombreIdentitario.objects.all()
    serializer_class = gscp_serializer.apiNombreIdentitario
    http_method_names = ['post','put']
    
#17 MGSC'17' SPGSC'3'
class PersonasCargoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.PersonasCargo.objects.all()
    serializer_class = gscp_serializer.apiPersonasCargo
    http_method_names = ['post','put']
    
#18 MGSC'18' SPGSC'4'
class DispacidadPersonaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.DispacidadPersona.objects.all()
    serializer_class = gscp_serializer.apiDispacidadPersona
    http_method_names = ['post','put']
    
#19 MGSC'19' SPGSC'5'
class GrupoEtnicoPersonaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.GrupoEtnicoPersona.objects.all()
    serializer_class = gscp_serializer.apiGrupoEtnicoPersona
    http_method_names = ['post','put']
        
#20 MGSC'20' SPGSC'6'
class GrupoIndigenaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.GrupoIndigena.objects.all()
    serializer_class = gscp_serializer.apiGrupoIndigena
    http_method_names = ['post','put']

#21 MGSC'21' SPGSC'7'
class EtnicoIndigenaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.EtnicoIndigena.objects.all()
    serializer_class = gscp_serializer.apiEtnicoIndigena
    http_method_names = ['post','put']
    
#22 MGSC'22' SPGSC'8'
class OtroGrupoPersonaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.OtroGrupoPersona.objects.all()
    serializer_class = gscp_serializer.apiOtroGrupoPersona
    http_method_names = ['post','put']

#23 MGSC'23' SPGSC'9'
class EtnicoConcejoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.EtnicoConcejo.objects.all()
    serializer_class = gscp_serializer.apiEtnicoConcejo
    http_method_names = ['post','put']

#24 MGSC'24' SPGSC'10'
class OrganizacionPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.Organizacion.objects.all()
    serializer_class = gscp_serializer.apiOrganizacion
    http_method_names = ['post','put']

#25 MGSC'25' SPGSC'11'
class OtraOrganizacionPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.OtraOrganizacion.objects.all()
    serializer_class = gscp_serializer.apiOtraOrganizacion
    http_method_names = ['post','put']
    
#26 MGSC'26' SPGSC'12'
class PersoneriaJuridicaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.PersoneriaJuridica.objects.all()
    serializer_class = gscp_serializer.apiPersoneriaJuridica
    http_method_names = ['post','put']

#27 MGSC'27' SPGSC'13'
class OrganizacionPersonaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.OrganizacionPersona.objects.all()
    serializer_class = gscp_serializer.apiOrganizacionPersona
    http_method_names = ['post','put']
    
#28 MGSC'28' SPGSC'14'
class MedidaCuatelarPersonaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.MedidaCuatelarPersona.objects.all()
    serializer_class = gscp_serializer.apiMedidaCuatelarPersona
    http_method_names = ['post','put']
    
#29 MGSC'29' SPGSC'15'
class ActividadAmbientalPersonaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.ActividadAmbientalPersona.objects.all()
    serializer_class = gscp_serializer.apiActividadAmbientalPersona
    http_method_names = ['post','put']
    
#30 MGSC'30' SPGSC'16'
class IdRiesgoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.IdRiesgo.objects.all()
    serializer_class = gscp_serializer.apiIdRiesgo
    http_method_names = ['post','put']
    
#31 MGSC'31' SPGSC'17'
class EvidenciasPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.Evidencias.objects.all()
    serializer_class = gscp_serializer.apiEvidencias
    http_method_names = ['post','put']
    
#32 MGSC'32' SPGSC'18'
class IdentificacionSituacionPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.IdentificacionSituacion.objects.all()
    serializer_class = gscp_serializer.apiIdentificacionSituacion
    http_method_names = ['post','put']
    
#33 MGSC'33' SPGSC'19'
class OtraSituacionRiesgoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.OtraSituacionRiesgo.objects.all()
    serializer_class = gscp_serializer.apiOtraSituacionRiesgo
    http_method_names = ['post','put']
    
#34 MGSC'34' SPGSC'20'
class IdentificacionMedioPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.IdentificacionMedio.objects.all()
    serializer_class = gscp_serializer.apiIdentificacionMedio
    http_method_names = ['post','put']
    
#35 MGSC'35' SPGSC'21'
class RelatosHechosPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.RelatosHechos.objects.all()
    serializer_class = gscp_serializer.apiRelatosHechos
    http_method_names = ['post','put']
    
#36 MGSC'36' SPGSC'22'
class IdPoblacionPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.IdPoblacion.objects.all()
    serializer_class = gscp_serializer.apiIdPoblacion
    http_method_names = ['post','put']
    
#37 MGSC'37' SPGSC'23'
class IdentificacionPoblacionObjetoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.IdentificacionPoblacionObjeto.objects.all()
    serializer_class = gscp_serializer.apiIdentificacionPoblacionObjeto
    http_method_names = ['post','put']
    
#38 MGSC'38' SPGSC'24'
class FilePoblacionPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.FilePoblacion.objects.all()
    serializer_class = gscp_serializer.apiFilePoblacion
    http_method_names = ['post','put']
    
#39 MGSC'39' SPGSC'25'
class OrganizacionPoliticaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.OrganizacionPolitica.objects.all()
    serializer_class = gscp_serializer.apiOrganizacionPolitica
    http_method_names = ['post','put']
    
#40 MGSC'40' SPGSC'26'
class CargoOrganizacionPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.CargoOrganizacion.objects.all()
    serializer_class = gscp_serializer.apiCargoOrganizacion
    http_method_names = ['post','put']
    
#41 MGSC'41' SPGSC'27'
class DatosPnisPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.DatosPnis.objects.all()
    serializer_class = gscp_serializer.apiDatosPnis
    http_method_names = ['post','put']

#42 MGSC'42' SPGSC'28'
class ConsentimientoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.Consentimiento.objects.all()
    serializer_class = gscp_serializer.apiConsentimiento
    http_method_names = ['post','put']
    
#43 MGSC'43' SPGSC'29'
class funcionColectivoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.funcionColectivo.objects.all()
    serializer_class = gscp_serializer.apifuncionColectivo
    http_method_names = ['post','put']
    
#44 MGSC'44' SPGSC'30'
class EntidadAcreditadoraPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.EntidadAcreditadora.objects.all()
    serializer_class = gscp_serializer.apiEntidadAcreditadora
    http_method_names = ['post','put']

#45 MGSC'45' SPGSC'31'
class CantidadPersonasDiscapacidadPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.CantidadPersonasDiscapacidad.objects.all()
    serializer_class = gscp_serializer.apiCantidadPersonasDiscapacidad
    http_method_names = ['post','put']
    
#46 MGSC'46' SPGSC'32'
class CantidadPersonasIndigenaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.CantidadPersonasIndigena.objects.all()
    serializer_class = gscp_serializer.apiCantidadPersonasIndigena
    http_method_names = ['post','put']
    
#47 MGSC'47' SPGSC'33'
class cantidadPersonasAfrocolombianosPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.cantidadPersonasAfrocolombianos.objects.all()
    serializer_class = gscp_serializer.apicantidadPersonasAfrocolombianos
    http_method_names = ['post','put']
    
#48 MGSC'48' SPGSC'34'
class cantidadPersonasNegroPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.cantidadPersonasNegro.objects.all()
    serializer_class = gscp_serializer.apicantidadPersonasNegro
    http_method_names = ['post','put']
     
#49 MGSC'49' SPGSC'35'
class cantidadPersonasRaizalPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.cantidadPersonasRaizal.objects.all()
    serializer_class = gscp_serializer.apicantidadPersonasRaizal
    http_method_names = ['post','put']
    
#50 MGSC'50' SPGSC'36'
class cantidadPersonasPalenqueroPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.cantidadPersonasPalenquero.objects.all()
    serializer_class = gscp_serializer.apicantidadPersonasPalenquero
    http_method_names = ['post','put']
    
#51 MGSC'51' SPGSC'37'
class cantidadPersonasRomGitanoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.cantidadPersonasRomGitano.objects.all()
    serializer_class = gscp_serializer.apicantidadPersonasRomGitano
    http_method_names = ['post','put']
    
#52 MGSC'52' SPGSC'38'
class CorrespondenciaColectivoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.CorrespondenciaColectivo.objects.all()
    serializer_class = gscp_serializer.apiCorrespondenciaColectivo
    http_method_names = ['post','put']
    
#53 MGSC'53' SPGSC'39'
class MedidaCautelarColectivoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.MedidaCautelarColectivo.objects.all()
    serializer_class = gscp_serializer.apiMedidaCautelarColectivo
    http_method_names = ['post','put']
    
#54 MGSC'54' SPGSC'40'
class mcComisionInternacionalPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.mcComisionInternacional.objects.all()
    serializer_class = gscp_serializer.apimcComisionInternacional
    http_method_names = ['post','put']
    
#55 MGSC'55' SPGSC'41'
class mcCorteInternacionalPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.mcCorteInternacional.objects.all()
    serializer_class = gscp_serializer.apimcCorteInternacional
    http_method_names = ['post','put']
    
#56 MGSC'56' SPGSC'42'
class mcJuezRepublicaPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.mcJuezRepublica.objects.all()
    serializer_class = gscp_serializer.apimcJuezRepublica
    http_method_names = ['post','put']

#57 MGSC'57' SPGSC'43'
class EntidadSolicitanteColectivoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.EntidadSolicitanteColectivo.objects.all()
    serializer_class = gscp_serializer.apiEntidadSolicitanteColectivo
    http_method_names = ['post','put']
    
#58 MGSC'58' SPGSC'44'
class ActividadPersonaColectivoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.ActividadPersonaColectivo.objects.all()
    serializer_class = gscp_serializer.apiActividadPersonaColectivo
    http_method_names = ['post','put']
    
#59 MGSC'59' SPGSC'45'
class IdPoblacionColectivoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.IdPoblacionColectivo.objects.all()
    serializer_class = gscp_serializer.apiIdPoblacionColectivo
    http_method_names = ['post','put']
    
#60 MGSC'60' SPGSC'46'
class PoblacionColectivoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.PoblacionColectivo.objects.all()
    serializer_class = gscp_serializer.apiPoblacionColectivo
    http_method_names = ['post','put']
    
#61 MGSC'61' SPGSC'47'
class PoblacionColectivoSespPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.PoblacionColectivoSesp.objects.all()
    serializer_class = gscp_serializer.apiPoblacionColectivoSesp
    http_method_names = ['post','put']
    
#62 MGSC'62' SPGSC'48'
class ActividadesColectivoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.ActividadesColectivo.objects.all()
    serializer_class = gscp_serializer.apiActividadesColectivo
    http_method_names = ['post','put']
    
#63 MGSC'63' SPGSC'49'
class HechoVictimizanteColectivoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.HechoVictimizanteColectivo.objects.all()
    serializer_class = gscp_serializer.apiHechoVictimizanteColectivo
    http_method_names = ['post','put']

#64 MGSC'64' SPGSC'50'
class ConsentimientoColectivoPermiso(viewsets.ModelViewSet):
    queryset = gsc_models.ConsentimientoColectivo.objects.all()
    serializer_class = gscp_serializer.apiConsentimientoColectivo
    http_method_names = ['post','put']