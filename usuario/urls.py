from django.urls import path, include
from usuario import views
from usuario import api as usr_api
from rest_framework import routers

app_name = 'usuario'
routers = routers.DefaultRouter()

routers.register('tipovinculacion', usr_api.TipoVinculacionPermiso, 'tipovinculacion'),                         #AUSR'1'
routers.register('dependencia', usr_api.DependenciaPermiso, 'dependencia'),                                     #AUSR'2'
routers.register('grupo', usr_api.GrupoPermiso, 'grupo'),                                                       #AUSR'3'
routers.register('rol', usr_api.RolPermiso, 'rol'),                                                             #AUSR'4'
routers.register('tccusuario', usr_api.TelefonoCelularContactoUsuarioPermiso, 'tccusuario'),                    #AUSR'5'
routers.register('cceusuario', usr_api.CorreoElectronicoContactoUsuarioPermiso, 'cceusuario'),                  #AUSR'6'
routers.register('datoscontacto', usr_api.DatosContactoUsuarioPermiso, 'datoscontacto'),                        #AUSR'7'
routers.register('datosubicacion', usr_api.DatosUbicacionUsuarioPermiso, 'datosubicacion'),                     #AUSR'8'
routers.register('ubicacionrural', usr_api.UbicacionRuralPermiso, 'ubicacionrural'),                            #AUSR'9'
routers.register('ubicacionurbana', usr_api.UbicacionUrbanaPermiso, 'ubicacionurbana'),                         #AUSR'10'
routers.register('identificacionusuario', usr_api.IdentificacionUsuarioPermiso, 'identificacionusuario'),       #AUSR'11'
routers.register('nombreusuario', usr_api.NombrePersonaUsuarioPermiso, 'nombreusuario'),                        #AUSR'12'
routers.register('datosbasicosusuario', usr_api.DatosBasicosUsuarioPermiso, 'datosbasicosusuario'),             #AUSR'13'
routers.register('dcusuario', usr_api.DatosComplementariosUsuarioPermiso, 'dcusuario'),                         #AUSR'14'
routers.register('datoscontrato', usr_api.ContratoContratistaPermiso, 'datoscontrato'),                         #AUSR'15'
routers.register('datosresolucion', usr_api.ResolucionFuncionarioPermiso, 'datosresolucion'),                   #AUSR'16'
routers.register('perfilusuario', usr_api.PerfilUsuarioPermiso, 'perfilusuario'),                               #AUSR'17'


urlpatterns = [
    path('', views.Inicio, name='inicio' ),
    path('usuario/', include(routers.urls)),
]