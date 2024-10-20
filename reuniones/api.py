from rest_framework import viewsets
from reuniones import models as reu_models
from reuniones import serializer_post as reup_serializer
from reuniones import serializer_get as reug_serializer


#1 MREU'1' SGREU'1'
class SedeUnpPermiso(viewsets.ModelViewSet):
    queryset = reu_models.SedeUnp.objects.all()
    serializer_class = reug_serializer.apiSedeUnp
    http_method_names = ['get'] 
    
#2 MREU'2' SGREU'2'
class TipoEstadoCompromisoPermiso(viewsets.ModelViewSet):
    queryset = reu_models.TipoEstadoCompromiso.objects.all()
    serializer_class = reug_serializer.apiTipoEstadoCompromiso   
    http_method_names = ['get']
    
#3 MREU'3' SPREU'1'
class TemaReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.TemaReunion.objects.all()
    serializer_class = reup_serializer.apiTemaReunion
    http_method_names = ['post', 'put']

#4 MREU'4' SPREU'2'
class FechaReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.FechaReunion.objects.all()
    serializer_class = reup_serializer.apiFechaReunion   
    http_method_names = ['post', 'put']

#5 MREU'5' SPREU'3'
class LugarReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LugarReunion.objects.all()
    serializer_class = reup_serializer.apiLugarReunion   
    http_method_names = ['post', 'put']

#6 MREU'6' SPREU'4'
class ReunionesPermiso(viewsets.ModelViewSet):
    queryset = reu_models.Reuniones.objects.all()
    serializer_class = reup_serializer.apiReuniones   
    http_method_names = ['post', 'put']

#7 MREU'7' SPREU'5'
class LlaveDesarrolloReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LlaveDesarrolloReunion.objects.all()
    serializer_class = reup_serializer.apiLlaveDesarrolloReunion   
    http_method_names = ['post', 'put']

#8 MREU'8' SPREU'6'
class DesarrolloReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.DesarrolloReunion.objects.all()
    serializer_class = reup_serializer.apiDesarrolloReunion   
    http_method_names = ['post', 'put']

#9 MREU'9' SPREU'7'
class LlaveConclusionReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LlaveConclusionReunion.objects.all()
    serializer_class = reup_serializer.apiLlaveConclusionReunion   
    http_method_names = ['post', 'put']

#10 MREU'10' SPREU'8'
class ConclusionReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.ConclusionReunion.objects.all()
    serializer_class = reup_serializer.apiConclusionReunion   
    http_method_names = ['post', 'put']

#11 MREU'11' SPREU'9'
class LlaveAsistenteReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LlaveAsistenteReunion.objects.all()
    serializer_class = reup_serializer.apiLlaveAsistenteReunion   
    http_method_names = ['post', 'put']

#12 MREU'12' SPREU'10'
class AsistenteReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.AsistenteReunion.objects.all()
    serializer_class = reup_serializer.apiAsistenteReunion   
    http_method_names = ['post', 'put']

#13 MREU'13' SPREU'11'
class LlaveResponsableReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LlaveResponsableReunion.objects.all()
    serializer_class = reup_serializer.apiLlaveResponsableReunion   
    http_method_names = ['post', 'put']

#14 MREU'14' SPREU'12'
class ResponsableReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.ResponsableReunion.objects.all()
    serializer_class = reup_serializer.apiResponsableReunion   
    http_method_names = ['post', 'put']

#15 MREU'15' SPREU'13'
class RelatorReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.RelatorReunion.objects.all()
    serializer_class = reup_serializer.apiRelatorReunion   
    http_method_names = ['post', 'put']

#16 MREU'16' SPREU'14'
class LlaveCompromisoReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LlaveCompromisoReunion.objects.all()
    serializer_class = reup_serializer.apiLlaveCompromisoReunion   
    http_method_names = ['post', 'put']

#17 MREU'17' SPREU'15'
class CompromisoReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.CompromisoReunion.objects.all()
    serializer_class = reup_serializer.apiCompromisoReunion   
    http_method_names = ['post', 'put']

#18 MREU'18' SPREU'16'
class ResponsableCompromisoPermiso(viewsets.ModelViewSet):
    queryset = reu_models.ResponsableCompromiso.objects.all()
    serializer_class = reup_serializer.apiResponsableCompromiso   
    http_method_names = ['post', 'put']

#19 MREU'19' SPREU'17'
class FechaCompromisoPermiso(viewsets.ModelViewSet):
    queryset = reu_models.FechaCompromiso.objects.all()
    serializer_class = reup_serializer.apiFechaCompromiso   
    http_method_names = ['post', 'put']
   
#20 MREU'20' SPREU'18'    
class EstadoCompromisoPermiso(viewsets.ModelViewSet):
    queryset = reu_models.EstadoCompromiso.objects.all()
    serializer_class = reup_serializer.apiEstadoCompromiso
    http_method_names = ['post', 'put']