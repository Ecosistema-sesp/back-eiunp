from rest_framework import serializers
from reuniones import models as reu_models

#1 MREU'1'        
class apiSedeUnp(serializers.ModelSerializer):
    class Meta:
        model = reu_models.SedeUnp
        fields = '__all__'
        
#2 MREU'2'        
class apiTipoEstadoCompromiso(serializers.ModelSerializer):
    class Meta:
        model = reu_models.TipoEstadoCompromiso
        fields = '__all__'
