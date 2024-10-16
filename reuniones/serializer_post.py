from rest_framework import serializers
from reuniones import models as reu_models

class apiTemaReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.TemaReunion
        fields = '__all__'

class apiFechaReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.FechaReunion
        fields = '__all__'

class apiSedeUnp(serializers.ModelSerializer):
    class Meta:
        model = reu_models.SedeUnp
        fields = '__all__'

class apiLugarReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LugarReunion
        fields = '__all__'

class apiReuniones(serializers.ModelSerializer):
    class Meta:
        model = reu_models.Reuniones
        fields = '__all__'

class apiLlaveDesarrolloReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LlaveDesarrolloReunion
        fields = '__all__'

class apiDesarrolloReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.DesarrolloReunion
        fields = '__all__'

class apiLlaveConclusionReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LlaveConclusionReunion
        fields = '__all__'

class apiConclusionReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.ConclusionReunion
        fields = '__all__'

class apiLlaveAsistenteReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LlaveAsistenteReunion
        fields = '__all__'

class apiAsistenteReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.AsistenteReunion
        fields = '__all__'

class apiLlaveResponsableReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LlaveResponsableReunion
        fields = '__all__'

class apiResponsableReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.ResponsableReunion
        fields = '__all__'

class apiRelatorReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.RelatorReunion
        fields = '__all__'

class apiLlaveCompromisoReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LlaveCompromisoReunion
        fields = '__all__'

class apiCompromisoReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.CompromisoReunion
        fields = '__all__'

class apiResponsableCompromiso(serializers.ModelSerializer):
    class Meta:
        model = reu_models.ResponsableCompromiso
        fields = '__all__'

class apiFechaCompromiso(serializers.ModelSerializer):
    class Meta:
        model = reu_models.FechaCompromiso
        fields = '__all__'

class apiTipoEstadoCompromiso(serializers.ModelSerializer):
    class Meta:
        model = reu_models.TipoEstadoCompromiso
        fields = '__all__'

class apiEstadoCompromiso(serializers.ModelSerializer):
    class Meta:
        model = reu_models.EstadoCompromiso
        fields = '__all__'