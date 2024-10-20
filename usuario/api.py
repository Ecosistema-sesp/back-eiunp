from rest_framework import viewsets
from usuario import models as usr_models
from usuario import serializer_get as usrg_serializer
from usuario import serializer_post as usrp_serializer


#  MUSR'numero' => (Modelos de la aplicación 'usuario')  + Número del modelo
#  SPUSR'numero' => (Serializador post de la aplicación 'usuario) + Número de la serialización
#  SGUSR'numero' => (Serializador get de la aplicación 'usuario) + Número de la serialización


#1 MUSR'1' SGUSR'1'
class TipoVinculacionPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.TipoVinculacion.objects.all()            
    serializer_class = usrg_serializer.ApiTipoVinculacion                                
    http_method_names = ['get']

#2 MUSR'2' SGUSR'2'
class DependenciaPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.Dependencia.objects.all()            
    serializer_class = usrg_serializer.ApiDependencia                            
    http_method_names = ['get']

#3 MUSR'3' SGUSR'3'
class GrupoPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.Grupo.objects.all()            
    serializer_class = usrg_serializer.ApiGrupo                                
    http_method_names = ['get']

#4 MUSR'4' SGUSR'4'
class RolPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.Rol.objects.all()            
    serializer_class = usrg_serializer.ApiRol                            
    http_method_names = ['get']

#5 MUSR'5' SPUSR'1'
class TelefonoCelularContactoUsuarioPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.TelefonoCelularContactoUsuario.objects.all()            
    serializer_class = usrp_serializer.apiTelefonoCelularContactoUsuario                           
    http_method_names = ['post','put']

#6 MUSR'6' SPUSR'2'
class CorreoElectronicoContactoUsuarioPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.CorreoElectronicoContactoUsuario.objects.all()            
    serializer_class = usrp_serializer.apiCorreoElectronicoContactoUsuario                            
    http_method_names = ['post','put']

#7 MUSR'7' SPUSR'3'
class DatosContactoUsuarioPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.DatosContactoUsuario.objects.all()            
    serializer_class = usrp_serializer.apiDatosContactoUsuario                            
    http_method_names = ['post','put']

#8 MUSR'8' SPUSR'4'
class DatosUbicacionUsuarioPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.DatosUbicacionUsuario.objects.all()            
    serializer_class = usrp_serializer.apiDatosUbicacionUsuario                            
    http_method_names = ['post','put']

#9 MUSR'9' SPUSR'5'
class UbicacionRuralPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.UbicacionRural.objects.all()            
    serializer_class = usrp_serializer.apiUbicacionRural                            
    http_method_names = ['post','put']

#10 MUSR'10' SPUSR'6'
class UbicacionUrbanaPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.UbicacionUrbana.objects.all()            
    serializer_class = usrp_serializer.apiUbicacionUrbana                         
    http_method_names = ['post','put']

#11 MUSR'11' SPUSR'7'
class IdentificacionUsuarioPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.IdentificacionUsuario.objects.all()            
    serializer_class = usrp_serializer.apiIdentificacionUsuario                         
    http_method_names = ['post','put']

#12 MUSR'12' SPUSR'8'
class NombrePersonaUsuarioPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.NombrePersonaUsuario.objects.all()            
    serializer_class = usrp_serializer.apiNombrePersonaUsuario                         
    http_method_names = ['post','put']

#13 MUSR'13' SPUSR'9'
class DatosBasicosUsuarioPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.DatosBasicosUsuario.objects.all()            
    serializer_class = usrp_serializer.apiDatosBasicosUsuario                         
    http_method_names = ['post','put']

#14 MUSR'14' SPUSR'10'
class DatosComplementariosUsuarioPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.DatosComplementariosUsuario.objects.all()            
    serializer_class = usrp_serializer.apiDatosComplementariosUsuario                         
    http_method_names = ['post','put']

#15 MUSR'15' SPUSR'11'
class ContratoContratistaPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.ContratoContratista.objects.all()            
    serializer_class = usrp_serializer.apiContratoContratista                         
    http_method_names = ['post','put']

#16 MUSR'16' SPUSR'12'
class ResolucionFuncionarioPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.ResolucionFuncionario.objects.all()            
    serializer_class = usrp_serializer.apiResolucionFuncionario                         
    http_method_names = ['post','put']

#17 MUSR'17' SPUSR'13'
class PerfilUsuarioPermiso(viewsets.ModelViewSet):                                   
    queryset = usr_models.PerfilUsuario.objects.all()            
    serializer_class = usrp_serializer.apiPerfilUsuario                         
    http_method_names = ['post','put']