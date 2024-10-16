from rest_framework import viewsets
from reuniones import models as reu_models
from reuniones import serializer_post as reu_serializer


class TemaReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.TemaReunion.objects.all()
    serializer_class = reu_serializer.apiTemaReunion
    http_method_names = ['post', 'put']

class FechaReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.FechaReunion.objects.all()
    serializer_class = reu_serializer.apiFechaReunion   
    http_method_names = ['post', 'put']

class SedeUnpPermiso(viewsets.ModelViewSet):
    queryset = reu_models.SedeUnp.objects.all()
    serializer_class = reu_serializer.apiSedeUnp   
    http_method_names = ['get']

class LugarReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LugarReunion.objects.all()
    serializer_class = reu_serializer.apiLugarReunion   
    http_method_names = ['post', 'put']

class ReunionesPermiso(viewsets.ModelViewSet):
    queryset = reu_models.Reuniones.objects.all()
    serializer_class = reu_serializer.apiReuniones   
    http_method_names = ['post', 'put']

class LlaveDesarrolloReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LlaveDesarrolloReunion.objects.all()
    serializer_class = reu_serializer.apiLlaveDesarrolloReunion   
    http_method_names = ['post', 'put']

class DesarrolloReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.DesarrolloReunion.objects.all()
    serializer_class = reu_serializer.apiDesarrolloReunion   
    http_method_names = ['post', 'put']

class LlaveConclusionReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LlaveConclusionReunion.objects.all()
    serializer_class = reu_serializer.apiLlaveConclusionReunion   
    http_method_names = ['post', 'put']

class ConclusionReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.ConclusionReunion.objects.all()
    serializer_class = reu_serializer.apiConclusionReunion   
    http_method_names = ['post', 'put']

class LlaveAsistenteReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LlaveAsistenteReunion.objects.all()
    serializer_class = reu_serializer.apiLlaveAsistenteReunion   
    http_method_names = ['post', 'put']

class AsistenteReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.AsistenteReunion.objects.all()
    serializer_class = reu_serializer.apiAsistenteReunion   
    http_method_names = ['post', 'put']

class LlaveResponsableReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LlaveResponsableReunion.objects.all()
    serializer_class = reu_serializer.apiLlaveResponsableReunion   
    http_method_names = ['post', 'put']

class ResponsableReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.ResponsableReunion.objects.all()
    serializer_class = reu_serializer.apiResponsableReunion   
    http_method_names = ['post', 'put']

class RelatorReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.RelatorReunion.objects.all()
    serializer_class = reu_serializer.apiRelatorReunion   
    http_method_names = ['post', 'put']

class LlaveCompromisoReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.LlaveCompromisoReunion.objects.all()
    serializer_class = reu_serializer.apiLlaveCompromisoReunion   
    http_method_names = ['post', 'put']

class CompromisoReunionPermiso(viewsets.ModelViewSet):
    queryset = reu_models.CompromisoReunion.objects.all()
    serializer_class = reu_serializer.apiCompromisoReunion   
    http_method_names = ['post', 'put']

class ResponsableCompromisoPermiso(viewsets.ModelViewSet):
    queryset = reu_models.ResponsableCompromiso.objects.all()
    serializer_class = reu_serializer.apiResponsableCompromiso   
    http_method_names = ['post', 'put']

class FechaCompromisoPermiso(viewsets.ModelViewSet):
    queryset = reu_models.FechaCompromiso.objects.all()
    serializer_class = reu_serializer.apiFechaCompromiso   
    http_method_names = ['post', 'put']

class TipoEstadoCompromisoPermiso(viewsets.ModelViewSet):
    queryset = reu_models.TipoEstadoCompromiso.objects.all()
    serializer_class = reu_serializer.apiTipoEstadoCompromiso   
    http_method_names = ['post', 'put']

class EstadoCompromisoPermiso(viewsets.ModelViewSet):
    queryset = reu_models.EstadoCompromiso.objects.all()
    serializer_class = reu_serializer.apiEstadoCompromiso
    http_method_names = ['post', 'put']