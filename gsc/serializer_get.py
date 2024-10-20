from rest_framework import serializers
from gsc import models as gsc_models

# MGSC'numero' => (Modelos de la aplicación 'gsc')  + Número del modelo


# SERIALIZAORES DE LAS TABLAS ESTÁTICAS

#1 MGSC'1'
class ApiTipoDiscapacidad(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.TipoDiscapacidad                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)             

#2 MGSC'2'
class ApiTipoGrupoEtnico(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.TipoGrupoEtnico                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)   

#3 MGSC'3'
class ApiTipoOrganizacionPersona(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.TipoOrganizacionPersona                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)  
    
#4 MGSC'4'
class ApiTipoMedidaCautelar(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.TipoMedidaCautelar                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)  

#5 MGSC'5'
class ApiTipoSituacionesRiesgo(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.TipoSituacionesRiesgo                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)  
        

#6 MGSC'6'
class ApiTipoMediosSituacion(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.TipoMediosSituacion                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)  
        
#7 MGSC'7'
class ApiTipoPoblacion(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.TipoPoblacion                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)  
        
#8 MGSC'8'
class ApiPoblacionObjeto(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.PoblacionObjeto                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)  
        
#9 MGSC'9'
class ApiTipoCategoriaOrganizacion(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.TipoCategoriaOrganizacion                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)  
        
#10 MGSC'10'
class ApiCategoriaPnis(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.CategoriaPnis                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)  

#11 MGSC'11'
class ApitipoEntidadAcreditadora(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.tipoEntidadAcreditadora                      
        fields = '__all__'                         
        read_only_fields = ('__all__',) 
        
#12 MGSC'12'
class ApiPoblacionGeneralColectivo(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.PoblacionGeneralColectivo                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)  
        
#13 MGSC'13'
class ApiTipoPoblacionColectivo(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.TipoPoblacionColectivo                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)  
        
#14 MGSC'14'
class ApiTipoPoblacionSesp(serializers.ModelSerializer):         
    class Meta:
        model = gsc_models.TipoPoblacionSesp                      
        fields = '__all__'                         
        read_only_fields = ('__all__',)  