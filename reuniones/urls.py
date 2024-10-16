from django.urls import path, include
from rest_framework import routers
from reuniones import api as reu_api

app_name = 'reuniones'
routers = routers.DefaultRouter()

routers.register('temareunion', reu_api.TemaReunionPermiso, 'temareunion'),
routers.register('fechareunion', reu_api.FechaReunionPermiso, 'fechareunion'),
routers.register('sede', reu_api.SedeUnpPermiso, 'sede'),
routers.register('lugarreunion', reu_api.LugarReunionPermiso, 'lugarreunion'),
routers.register('reunion', reu_api.ReunionesPermiso, 'reunion'),
routers.register('llavedesarrollo', reu_api.LlaveDesarrolloReunionPermiso, 'llavedesarrollo'),
routers.register('desarrolloreunion', reu_api.DesarrolloReunionPermiso, 'desarrolloreunion'),
routers.register('llaveconclusion', reu_api.LlaveConclusionReunionPermiso, 'llaveconclusion'),
routers.register('conclusionreunion', reu_api.ConclusionReunionPermiso, 'conclusionreunion'),
routers.register('llaveasistente', reu_api.LlaveAsistenteReunionPermiso, 'llaveasistente'),
routers.register('asistentereunion', reu_api.AsistenteReunionPermiso, 'asistentereunion'),
routers.register('llaveresponsable', reu_api.LlaveResponsableReunionPermiso, 'llaveresponsable'),
routers.register('responsablereunion', reu_api.ResponsableReunionPermiso, 'responsablereunion'),
routers.register('relatorreunion', reu_api.RelatorReunionPermiso, 'relatorreunion'),
routers.register('llavecompromiso', reu_api.LlaveCompromisoReunionPermiso, 'llavecompromiso'),
routers.register('compromisoreunion', reu_api.ConclusionReunionPermiso, 'compromisoreunion'),
routers.register('compromisoresponsable', reu_api.ResponsableCompromisoPermiso, 'compromisoresponsable'),
routers.register('compromisofecha', reu_api.FechaCompromisoPermiso, 'compromisofecha'),
routers.register('tipoestadocompromiso', reu_api.TipoEstadoCompromisoPermiso, 'tipoestadocompromiso'),
routers.register('estadocompromiso', reu_api.EstadoCompromisoPermiso, 'estadocompromiso'),

urlpatterns = [
    path('', include(routers.urls)),
]