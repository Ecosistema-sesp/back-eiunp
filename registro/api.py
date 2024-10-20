from rest_framework import viewsets
from registro import models as reg_models
from registro import serializer_get as regg_serializer
from registro import serializer_post as regp_serializer


#  MREG'numero' => (Modelos de la aplicación 'sistema')  + Número del modelo
#  SPREG'numero' => (Serializador post de la aplicación 'sistema) + Número de la serialización
#  SGREG'numero' => (Serializador get de la aplicación 'sistema) + Número de la serialización


#1 MREG'1' SGREG'1'
class EstadoGeneralPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.EstadoGeneral.objects.all()        
    serializer_class = regg_serializer.apiEstadoGeneral                                
    http_method_names = ['get']

#2 MREG'2' SGREG'2'
class EstadoEspecificoPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.EstadoEspecifico.objects.all()        
    serializer_class = regg_serializer.apiEstadoEspecifico                                
    http_method_names = ['get']

#3 MREG'3' SGREG'3'
class TipoRutaPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.TipoRuta.objects.all()        
    serializer_class = regg_serializer.apiTipoRuta                                
    http_method_names = ['get']

#4 MREG'4' SGREG'4'
class CanalSolicitudPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.CanalSolicitud.objects.all()        
    serializer_class = regg_serializer.apiCanalSolicitud                                
    http_method_names = ['get']

#5 MREG'5' SGREG'5'
class TipoResultadoLlamadaPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.TipoResultadoLlamada.objects.all()        
    serializer_class = regg_serializer.apiTipoResultadoLlamada                                
    http_method_names = ['get']


#6 MREG'6' SPREG'1'
class RegistroPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.Registro.objects.all()        
    serializer_class = regp_serializer.apiRegistro                                
    http_method_names = ['post', 'put']

#7 MREG'7' SPREG'2'
class FechaTerminosPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.FechaTerminos.objects.all()        
    serializer_class = regp_serializer.apiFechaTerminos                                
    http_method_names = ['post', 'put']

#8 MREG'8' SPREG'3'
class TrazabilidadGeneralPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.TrazabilidadGeneral.objects.all()        
    serializer_class = regp_serializer.apiTrazabilidadGeneral                                
    http_method_names = ['post', 'put']


#9 MREG'9' SPREG'4'
class TrazabilidadPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.Trazabilidad.objects.all()        
    serializer_class = regp_serializer.apiTrazabilidad                                
    http_method_names = ['post', 'put']

#10 MREG'10' SPREG'5'
class fechaDiligenciamientoFormularioPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.fechaDiligenciamientoFormulario.objects.all()        
    serializer_class = regp_serializer.apifechaDiligenciamientoFormulario                                
    http_method_names = ['post', 'put']

#11 MREG'11' SPREG'6'
class lugarDiligenciamientoFormularioPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.lugarDiligenciamientoFormulario.objects.all()        
    serializer_class = regp_serializer.apilugarDiligenciamientoFormulario                                
    http_method_names = ['post', 'put']

#12 MREG'12' SPREG'7'
class DiligenciaFormularioPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.DiligenciaFormulario.objects.all()        
    serializer_class = regp_serializer.apiDiligenciaFormulario                                
    http_method_names = ['post', 'put']

#13 MREG'13' SPREG'8'
class FormularioPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.Formulario.objects.all()        
    serializer_class = regp_serializer.apiFormulario                                
    http_method_names = ['post', 'put']

#14 MREG'14' SPREG'9'
class FormularioIndividualPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.FormularioIndividual.objects.all()        
    serializer_class = regp_serializer.apiFormularioIndividual                                
    http_method_names = ['post', 'put']

#15 MREG'15' SPREG'10'
class FormularioColectivoPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.FormularioColectivo.objects.all()        
    serializer_class = regp_serializer.apiFormularioColectivo                                
    http_method_names = ['post', 'put']

#16 MREG'16' SPREG'11'
class RegistroLlamadasPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.RegistroLlamadas.objects.all()        
    serializer_class = regp_serializer.apiRegistroLlamadas                                
    http_method_names = ['post', 'put']

#17 MREG'17' SPREG'12'
class FechaHoraLlamadaPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.FechaHoraLlamada.objects.all()        
    serializer_class = regp_serializer.apiFechaHoraLlamada                                
    http_method_names = ['post', 'put']

#18 MREG'18' SPREG'13'
class MedioContactoLlamadaPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.MedioContactoLlamada.objects.all()        
    serializer_class = regp_serializer.apiMedioContactoLlamada                                
    http_method_names = ['post', 'put']

#19 MREG'19' SPREG'14'
class InformacionLlamadaPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.InformacionLlamada.objects.all()        
    serializer_class = regp_serializer.apiInformacionLlamada                               
    http_method_names = ['post', 'put']

#20 MREG'20' SPREG'15'
class TerceroRespondeLlamadaPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.TerceroRespondeLlamada.objects.all()        
    serializer_class = regp_serializer.apiTerceroRespondeLlamada                               
    http_method_names = ['post', 'put']

#21 MREG'21' SPREG'16'
class EntidadrespondeLlamadaPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.EntidadrespondeLlamada.objects.all()        
    serializer_class = regp_serializer.apiEntidadrespondeLlamada                                
    http_method_names = ['post', 'put']

#22 MREG'22' SPREG'17'
class UbicacionrespondeLlamadaPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.UbicacionrespondeLlamada.objects.all()        
    serializer_class = regp_serializer.apiUbicacionrespondeLlamada                   
    http_method_names = ['post', 'put']

#23 MREG'23' SPREG'18'
class RespondeUrbanaLlamadaPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.RespondeUrbanaLlamada.objects.all()        
    serializer_class = regp_serializer.apiRespondeUrbanaLlamada          
    http_method_names = ['post', 'put']

#24 MREG'24' SPREG'19'
class RespondeRuralLlamadaPermiso(viewsets.ModelViewSet):                                   
    queryset = reg_models.RespondeRuralLlamada.objects.all()        
    serializer_class = regp_serializer.apiRespondeRuralLlamada          
    http_method_names = ['post', 'put']