from django.urls import path, include
from rest_framework import routers
from sistema import api as sis_api

app_name = 'sistema'
routers = routers.DefaultRouter()


# ASIS<numero> => (Api de la aplicación 'sistema')  + Número de la api


# RUTAS DE LAS TABLAS ESTÁTICAS
routers.register('pais', sis_api.PaisPermiso, 'pais'),                                                          #ASIS'1'
routers.register('departamento', sis_api.DepartamentoPermiso, 'departamento'),                                  #ASIS'2'
routers.register('municipio', sis_api.MunicipioPermiso, 'municipio'),                                           #ASIS'3'
routers.register('zona', sis_api.ZonaPermiso, 'zona'),                                                          #ASIS'4'
routers.register('tipoidentificacion', sis_api.TipoIdentificacionPermiso, 'tipoidentificacion'),                #ASIS'5'
routers.register('tipogenero', sis_api.TipoGeneroPermiso, 'tipogenero'),                                        #ASIS'6'
routers.register('tipoestadocivil', sis_api.EstadoCivilPermiso, 'tipoestadocivil'),                             #ASIS'7'
routers.register('tipogprh', sis_api.GpRhPermiso, 'gprhl'),                                                     #ASIS'8'
routers.register('tipofondopensiones', sis_api.FondoPensionesPermiso, 'fondopensiones'),                        #ASIS'9'
routers.register('tipoeps', sis_api.EpsPermiso, 'eps'),                                                         #ASIS'10'
routers.register('tiposexo', sis_api.TipoSexoPermiso, 'tiposexo'),                                              #ASIS'11'
routers.register('tiposexual', sis_api.TipoOrientacionSexualPermiso, 'tiposexual'),                             #ASIS'12'
routers.register('tiporangoetario', sis_api.TipoRangoEtarioPermiso, 'rangoetario'),                             #ASIS'13'
routers.register('tipodiferencial', sis_api.TipoFactorDiferencialPermiso, 'tipodiferencial'),                   #ASIS'14'
routers.register('tipoicolectivo', sis_api.TipoIdentificacionColectivoPermiso, 'tipoicolectivo'),               #ASIS'15'


# RUTAS DE LAS TABLAS DINÁMICAS
routers.register('ubicacion', sis_api.DatosUbicacionPermiso, 'ubicacion'),                                      #ASIS'16'
routers.register('direccionrural', sis_api.UbicacionRuralPermiso, 'direccionrural'),                            #ASIS'17'
routers.register('direccionurbana', sis_api.UbicacionUrbanaPermiso, 'direccionurbana'),                         #ASIS'18'
routers.register('telefonocontacto', sis_api.TelefonoCelularContactoPermiso, 'telefonocontacto'),               #ASIS'19'
routers.register('correocontacto', sis_api.CorreoElectronicoContactoPermiso, 'correocontacto'),                 #ASIS'20'
routers.register('contacto', sis_api.DatosContactoPermiso, 'contacto'),                                         #ASIS'21'
routers.register('identificacionpersona', sis_api.IdentificacionPersonaPermiso, 'identificacionpersona'),       #ASIS'22'
routers.register('filedocumentoidentidad', sis_api.FileDocumentoIdentidadPermiso, 'filedocumentoidentidad'),    #ASIS'23'
routers.register('nombrepersona', sis_api.NombrePersonaPermiso, 'nombrepersona'),                               #ASIS'24'
routers.register('datosbasicospersona', sis_api.DatosBasicosPersonaPermiso, 'datosbasicospersona'),             #ASIS'25'
routers.register('lugarnacimiento', sis_api.LugarNacimientoPersonaPermiso, 'lugarnacimiento'),                  #ASIS'26'
routers.register('fechanacimiento', sis_api.FechaNacimientoPersonaPermiso, 'fechanacimiento'),                  #ASIS'27'
routers.register('nacimiento', sis_api.DatosNacimientoPersonaPermiso, 'nacimiento'),                            #ASIS'28'
routers.register('datoscomplementarios', sis_api.DatosComplemetariosPersonaPermiso, 'datoscomplementarios'),    #ASIS'29'
routers.register('nrepresentantelegal', sis_api.NombreRepresentanteLegalMenorPermiso, 'nrepresentantelegal'),   #ASIS'30'
routers.register('irepresentantelegal', sis_api.IdentificacionRepresentantePermiso, 'irepresentantelegal'),     #ASIS'31'
routers.register('datorepresentantelegal', sis_api.DatosRepresentanteLegalPermiso, 'datorepresentantelegal'),   #ASIS'32'
routers.register('nombrecolectivo', sis_api.NombreColectivoPermiso, 'nombrecolectivo'),                         #ASIS'34'
routers.register('datosbasicoscolectivo', sis_api.DatosbasicosColectivosPermiso, 'datosbasicoscolectivo'),      #ASIS'35'
routers.register('identificacioncolectivo', sis_api.IdentificacionColectivoPermiso, 'identificacioncolectivo'), #ASIS'36'
routers.register('fdcolectivo', sis_api.ColectivoFDiferencialPermiso, 'fdcolectivo'),                           #ASIS'37'
routers.register('cantidadgenero', sis_api.cantidadGeneroPermiso, 'cantidadgenero'),                            #ASIS'38'
routers.register('cantidadsexo', sis_api.cantidadSexoPermiso, 'cantidadsexo'),                                  #ASIS'39'
routers.register('totalintegrantes', sis_api.TotalIntegrantesPermiso, 'totalintegrantes'),                      #ASIS'40'
routers.register('napcolectivo', sis_api.NombrePersonaColectivoPermiso, 'napcolectivo'),                        #ASIS'41'
routers.register('ipcolectivo', sis_api.IdentificacionPersonaColectivoPermiso, 'ipcolectivo'),                  #ASIS'42'
routers.register('personacolectivo', sis_api.PersonaColectivoPermiso, 'personacolectivo'),                      #ASIS'43'
routers.register('pcrepresentante', sis_api.PersonaColectivoRepresentantePermiso, 'pcrepresentante'),           #ASIS'44'

urlpatterns = [
    path('', include(routers.urls)),
]