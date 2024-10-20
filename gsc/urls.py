from django.urls import path, include
from gsc import api as gsc_api
from rest_framework import routers

app_name = 'gsc'
routers = routers.DefaultRouter()

routers.register('tipodiscapacidad', gsc_api.TipoDiscapacidadPermiso, 'tipodiscapacidad'),                      #AGSC'1'
routers.register('tipogrupoetnico', gsc_api.TipoGrupoEtnicoPermiso, 'tipogrupoetnico'),                         #AGSC'2'
routers.register('tipoorganizacionpersona', gsc_api.TipoOrganizacionPersonaPermiso, 'tipoorganizacionpersona'), #AGSC'3'
routers.register('tipomedidacautelar', gsc_api.TipoMedidaCautelarPermiso, 'tipomedidacautelar'),                #AGSC'4'
routers.register('tiposituacionriesgo', gsc_api.TipoSituacionesRiesgoPermiso, 'tiposituacionriesgo'),           #AGSC'5'
routers.register('tipomediosituacion', gsc_api.TipoMediosSituacionPermiso, 'tipomediosituacion'),               #AGSC'6'
routers.register('tipopoblacion', gsc_api.TipoPoblacionPermiso, 'tipopoblacion'),                               #AGSC'7'
routers.register('tipopoblacionobjeto', gsc_api.PoblacionObjetoPermiso, 'tipopoblacionobjeto'),                 #AGSC'8'
routers.register('tcorganizacionpersona', gsc_api.TipoCategoriaOrganizacionPermiso, 'tcorganizacionpersona'),   #AGSC'9'
routers.register('tipocategoriapenis', gsc_api.CategoriaPnisPermiso, 'tipocategoriapenis'),                     #AGSC'10'
routers.register('tipoentidadacreditadora', gsc_api.tipoEntidadAcreditadoraPermiso, 'tipoentidadacreditadora'), #AGSC'11'
routers.register('tpgeneralcolectivo', gsc_api.PoblacionGeneralColectivoPermiso, 'tpgeneralcolectivo'),         #AGSC'12'
routers.register('tipopoblacioncolectivo', gsc_api.TipoPoblacionColectivoPermiso, 'tipopoblacioncolectivo'),    #AGSC'13'
routers.register('tipopoblacionsesp', gsc_api.TipoPoblacionSespPermiso, 'tipopoblacionsesp'),                   #AGSC'14'

routers.register('dnotificacionpersona', gsc_api.DireccionNotificacionPersonaPermiso, 'dnotificacionpersona'),  #AGSC'15'
routers.register('nombreidentitario', gsc_api.NombreIdentitarioPermiso, 'nombreidentitario'),                   #AGSC'16'
routers.register('personascargo', gsc_api.PersonasCargoPermiso, 'personascargo'),                               #AGSC'17'
routers.register('discapacidadpersona', gsc_api.DispacidadPersonaPermiso, 'discapacidadpersona'),               #AGSC'18'
routers.register('grupoetnicopersona', gsc_api.GrupoEtnicoPersonaPermiso, 'grupoetnicopersona'),                #AGSC'19'
routers.register('grupoindigena', gsc_api.GrupoIndigenaPermiso, 'grupoindigena'),                               #AGSC'20'
routers.register('etnicoindigena', gsc_api.EtnicoIndigenaPermiso, 'etnicoindigena'),                            #AGSC'21'
routers.register('otrogrupopersona', gsc_api.OtroGrupoPersonaPermiso, 'otrogrupopersona'),                      #AGSC'22'
routers.register('etnicoconsejo', gsc_api.EtnicoConcejoPermiso, 'etnicoconsejo'),                               #AGSC'23'
routers.register('organizacion', gsc_api.OrganizacionPermiso, 'organizacion'),                                  #AGSC'24'
routers.register('otraorganizacion', gsc_api.OtraOrganizacionPermiso, 'otraorganizacion'),                      #AGSC'25'
routers.register('personeriajuridica', gsc_api.PersoneriaJuridicaPermiso, 'personeriajuridica'),                #AGSC'26'
routers.register('organizacionpersona', gsc_api.OrganizacionPersonaPermiso, 'organizacionpersona'),             #AGSC'27'
routers.register('medidacautelarpersona', gsc_api.MedidaCuatelarPersonaPermiso, 'medidacautelarpersona'),       #AGSC'28'
routers.register('aambientalpersona', gsc_api.ActividadAmbientalPersonaPermiso, 'aambientalpersona'),           #AGSC'29'
routers.register('llaveriesgo', gsc_api.IdRiesgoPermiso, 'llaveriesgo'),                                        #AGSC'30'
routers.register('documentoevidencia', gsc_api.EvidenciasPermiso, 'documentoevidencia'),                        #AGSC'31'
routers.register('identificacionsituacion', gsc_api.IdentificacionSituacionPermiso, 'identificacionsituacion'), #AGSC'32'
routers.register('otrasituacionriesgo', gsc_api.OtraSituacionRiesgoPermiso, 'otrasituacionriesgo'),             #AGSC'33'
routers.register('identificacionmedio', gsc_api.IdentificacionMedioPermiso, 'identificacionmedio'),             #AGSC'34'
routers.register('relatoshechos', gsc_api.RelatosHechosPermiso, 'relatoshechos'),                               #AGSC'35'
routers.register('llavepoblacion', gsc_api.IdPoblacionPermiso, 'llavepoblacion'),                               #AGSC'36'
routers.register('ipoblacionobjeto', gsc_api.IdentificacionPoblacionObjetoPermiso, 'ipoblacionobjeto'),         #AGSC'37'
routers.register('documentopoblacion', gsc_api.FilePoblacionPermiso, 'documentopoblacion'),                     #AGSC'38'
routers.register('organizacionpolitica', gsc_api.OrganizacionPoliticaPermiso, 'organizacionpolitica'),          #AGSC'39'
routers.register('cargoorganizacion', gsc_api.CargoOrganizacionPermiso, 'cargoorganizacion'),                   #AGSC'40'
routers.register('datospenis', gsc_api.DatosPnisPermiso, 'datospenis'),                                         #AGSC'41'
routers.register('consentimientoindividual', gsc_api.ConsentimientoPermiso, 'consentimientoindividual'),        #AGSC'42'
routers.register('funcioncolectivo', gsc_api.funcionColectivoPermiso, 'funcioncolectivo'),                      #AGSC'43'
routers.register('entidadacreditadora', gsc_api.EntidadAcreditadoraPermiso, 'entidadacreditadora'),             #AGSC'44'
routers.register('cpdiscapacidad', gsc_api.CantidadPersonasDiscapacidadPermiso, 'cpdiscapacidad'),              #AGSC'45'
routers.register('cpindigena', gsc_api.CantidadPersonasIndigenaPermiso, 'cpindigena'),                          #AGSC'46'
routers.register('cpafrocolombiano', gsc_api.cantidadPersonasAfrocolombianosPermiso, 'cpafrocolombiano'),       #AGSC'47'
routers.register('cpnegros', gsc_api.cantidadPersonasNegroPermiso, 'cpnegros'),                                 #AGSC'48'
routers.register('cpraizal', gsc_api.cantidadPersonasRaizalPermiso, 'cpraizal'),                                #AGSC'49'
routers.register('cppalenquero', gsc_api.cantidadPersonasPalenqueroPermiso, 'cppalenquero'),                    #AGSC'50'
routers.register('cpromgitano', gsc_api.cantidadPersonasRomGitanoPermiso, 'cpromgitano'),                       #AGSC'51'
routers.register('ccolectivo', gsc_api.CorrespondenciaColectivoPermiso, 'ccolectivo'),                          #AGSC'52'
routers.register('medidacautelarcolectivo', gsc_api.MedidaCautelarColectivoPermiso, 'medidacautelarcolectivo'), #AGSC'53'
routers.register('mccinternacional', gsc_api.mcComisionInternacionalPermiso, 'mccinternacional'),               #AGSC'54'
routers.register('mccorteinternacional', gsc_api.mcCorteInternacionalPermiso, 'mccorteinternacional'),          #AGSC'55'
routers.register('mcjuezrepublica', gsc_api.mcJuezRepublicaPermiso, 'mcjuezrepublica'),                         #AGSC'56'
routers.register('escolectivo', gsc_api.EntidadSolicitanteColectivoPermiso, 'escolectivo'),                     #AGSC'57'
routers.register('apcolectivo', gsc_api.ActividadPersonaColectivoPermiso, 'apcolectivo'),                       #AGSC'58'
routers.register('llavecolectivo', gsc_api.IdPoblacionColectivoPermiso, 'llavecolectivo'),                      #AGSC'59'
routers.register('poblacioncolectivo', gsc_api.PoblacionColectivoPermiso, 'poblacioncolectivo'),                #AGSC'60'
routers.register('poblacioncolectivosesp', gsc_api.PoblacionColectivoSespPermiso, 'poblacioncolectivosesp'),    #AGSC'61'
routers.register('actidadescolectivo', gsc_api.ActividadesColectivoPermiso, 'actidadescolectivo'),              #AGSC'62'
routers.register('hvcolectivo', gsc_api.HechoVictimizanteColectivoPermiso, 'hvcolectivo'),                      #AGSC'63'
routers.register('consentimientocolectivo', gsc_api.ConsentimientoColectivoPermiso, 'consentimientocolectivo'), #AGSC'64'


urlpatterns = [
    path('', include(routers.urls)),
]