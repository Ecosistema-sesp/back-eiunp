from django.urls import path, include
from rest_framework import routers
from registro import api as reg_api

app_name = 'registro'
routers = routers.DefaultRouter()

# AREG<numero> => (Api de la aplicación 'registro')  + Número de la api

routers.register('estadogeneralregistro', reg_api.EstadoGeneralPermiso, 'estadogeneralregistro'),                #AREG'1'
routers.register('estadoespecificoregistro', reg_api.EstadoEspecificoPermiso, 'estadoespecificoregistro'),       #AREG'2'
routers.register('tiporuta', reg_api.TipoRutaPermiso, 'tiporuta'),                                               #AREG'3'
routers.register('canalsolicitud', reg_api.CanalSolicitudPermiso, 'canalsolicitud'),                             #AREG'4'
routers.register('tiporesultadollamada', reg_api.TipoResultadoLlamadaPermiso, 'tiporesultadollamada'),           #AREG'5'
routers.register('registro', reg_api.RegistroPermiso, 'registro'),                                               #AREG'6'
routers.register('fechaterminos', reg_api.FechaTerminosPermiso, 'fechaterminos'),                                #AREG'7'
routers.register('trazabilidadgeneral', reg_api.TrazabilidadGeneralPermiso, 'trazabilidadgeneral'),              #AREG'8'
routers.register('trazabilidad', reg_api.TrazabilidadPermiso, 'trazabilidad'),                                   #AREG'9'
routers.register('fdformulario', reg_api.fechaDiligenciamientoFormularioPermiso, 'fdformulario'),                #AREG'10'
routers.register('ldformulario', reg_api.lugarDiligenciamientoFormularioPermiso, 'ldformulario'),                #AREG'11'
routers.register('diligenciaformulario', reg_api.DiligenciaFormularioPermiso, 'diligenciaformulario'),           #AREG'12'
routers.register('formulario', reg_api.FormularioPermiso, 'formulario'),                                         #AREG'13'
routers.register('formularioindividual', reg_api.FormularioIndividualPermiso, 'formularioindividual'),           #AREG'14'
routers.register('formulariocolectivo', reg_api.FormularioColectivoPermiso, 'formulariocolectivo'),              #AREG'15'
routers.register('registrollamadas', reg_api.RegistroLlamadasPermiso, 'registrollamadas'),                       #AREG'16'
routers.register('fechahorallamada', reg_api.FechaHoraLlamadaPermiso, 'fechahorallamada'),                       #AREG'17'
routers.register('mcontactollamada', reg_api.InformacionLlamadaPermiso, 'mcontactollamada'),                     #AREG'18'
routers.register('informacionllamadas', reg_api.InformacionLlamadaPermiso, 'informacionllamadas'),               #AREG'19'
routers.register('trespondellamada', reg_api.TerceroRespondeLlamadaPermiso, 'trespondellamada'),                 #AREG'20'
routers.register('erespondellamada', reg_api.EntidadrespondeLlamadaPermiso, 'erespondellamada'),                 #AREG'21'
routers.register('urespondellamada', reg_api.UbicacionrespondeLlamadaPermiso, 'urespondellamada'),               #AREG'22'
routers.register('uurespondellamada', reg_api.RespondeUrbanaLlamadaPermiso, 'uurespondellamada'),                #AREG'23'
routers.register('urrespondellamada', reg_api.RespondeRuralLlamadaPermiso, 'urrespondellamada'),                 #AREG'23'




urlpatterns = [
    path('', include(routers.urls)),
]