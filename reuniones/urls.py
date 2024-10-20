from django.urls import path, include
from rest_framework import routers
from reuniones import api as reu_api

app_name = 'reuniones'
routers = routers.DefaultRouter()

routers.register('sede', reu_api.SedeUnpPermiso, 'sede'),                                                       #AREU'1'
routers.register('tipoestadocompromiso', reu_api.TipoEstadoCompromisoPermiso, 'tipoestadocompromiso'),          #AREU'2'
routers.register('temareunion', reu_api.TemaReunionPermiso, 'temareunion'),                                     #AREU'3'
routers.register('fechareunion', reu_api.FechaReunionPermiso, 'fechareunion'),                                  #AREU'4'
routers.register('lugarreunion', reu_api.LugarReunionPermiso, 'lugarreunion'),                                  #AREU'5'
routers.register('reunion', reu_api.ReunionesPermiso, 'reunion'),                                               #AREU'6'
routers.register('llavedesarrollo', reu_api.LlaveDesarrolloReunionPermiso, 'llavedesarrollo'),                  #AREU'7'
routers.register('desarrolloreunion', reu_api.DesarrolloReunionPermiso, 'desarrolloreunion'),                   #AREU'8'
routers.register('llaveconclusion', reu_api.LlaveConclusionReunionPermiso, 'llaveconclusion'),                  #AREU'9'
routers.register('conclusionreunion', reu_api.ConclusionReunionPermiso, 'conclusionreunion'),                   #AREU'10'
routers.register('llaveasistente', reu_api.LlaveAsistenteReunionPermiso, 'llaveasistente'),                     #AREU'11'
routers.register('asistentereunion', reu_api.AsistenteReunionPermiso, 'asistentereunion'),                      #AREU'12'
routers.register('llaveresponsable', reu_api.LlaveResponsableReunionPermiso, 'llaveresponsable'),               #AREU'13'
routers.register('responsablereunion', reu_api.ResponsableReunionPermiso, 'responsablereunion'),                #AREU'14'
routers.register('relatorreunion', reu_api.RelatorReunionPermiso, 'relatorreunion'),                            #AREU'15'
routers.register('llavecompromiso', reu_api.LlaveCompromisoReunionPermiso, 'llavecompromiso'),                  #AREU'16'
routers.register('compromisoreunion', reu_api.ConclusionReunionPermiso, 'compromisoreunion'),                   #AREU'17'
routers.register('compromisoresponsable', reu_api.ResponsableCompromisoPermiso, 'compromisoresponsable'),       #AREU'18'
routers.register('compromisofecha', reu_api.FechaCompromisoPermiso, 'compromisofecha'),                         #AREU'19'
routers.register('estadocompromiso', reu_api.EstadoCompromisoPermiso, 'estadocompromiso'),                      #AREU'20'

urlpatterns = [
    path('', include(routers.urls)),
]