from rest_framework import serializers
from reuniones import models as reu_models


#1 MREU'3'
class apiTemaReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.TemaReunion
        fields = '__all__'

#2 MREU'4'
class apiFechaReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.FechaReunion
        fields = '__all__'

#3 MREU'5'
class apiLugarReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LugarReunion
        fields = '__all__'

#4 MREU'6'
class apiReuniones(serializers.ModelSerializer):
    class Meta:
        model = reu_models.Reuniones
        fields = '__all__'

#5 MREU'7'
class apiLlaveDesarrolloReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LlaveDesarrolloReunion
        fields = '__all__'

#6 MREU'8'
class apiDesarrolloReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.DesarrolloReunion
        fields = '__all__'

#7 MREU'9'
class apiLlaveConclusionReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LlaveConclusionReunion
        fields = '__all__'

#8 MREU'10'
class apiConclusionReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.ConclusionReunion
        fields = '__all__'

#9 MREU'11'
class apiLlaveAsistenteReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LlaveAsistenteReunion
        fields = '__all__'

#10 MREU'12'
class apiAsistenteReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.AsistenteReunion
        fields = '__all__'

#11 MREU'13'
class apiLlaveResponsableReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LlaveResponsableReunion
        fields = '__all__'

#12 MREU'14'
class apiResponsableReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.ResponsableReunion
        fields = '__all__'

#13 MREU'15'
class apiRelatorReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.RelatorReunion
        fields = '__all__'
        
#14 MREU'16'        
class apiLlaveCompromisoReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.LlaveCompromisoReunion
        fields = '__all__'

#15 MREU'17'        
class apiCompromisoReunion(serializers.ModelSerializer):
    class Meta:
        model = reu_models.CompromisoReunion
        fields = '__all__'

#16 MREU'18'        
class apiResponsableCompromiso(serializers.ModelSerializer):
    class Meta:
        model = reu_models.ResponsableCompromiso
        fields = '__all__'

#17 MREU'19'        
class apiFechaCompromiso(serializers.ModelSerializer):
    class Meta:
        model = reu_models.FechaCompromiso
        fields = '__all__'

#18 MREU'20'        
class apiEstadoCompromiso(serializers.ModelSerializer):
    class Meta:
        model = reu_models.EstadoCompromiso
        fields = '__all__'