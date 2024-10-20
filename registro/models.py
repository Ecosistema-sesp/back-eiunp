from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from sistema import models as sis_models
from gsc import models as gsc_models


# Create your models here.

# MODELOS PARA LAS TABLAS ESTÁTICAS DE REGISTRO

#1
class EstadoGeneral(models.Model):
    id_egeneral = models.AutoField(primary_key=True)
    nombre_egeneral = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_egeneral'
        verbose_name_plural = 'Estados generales'

    def __str__(self):
        return str(self.id_egeneral)

#2
class EstadoEspecifico(models.Model):
    id_eespecifico = models.AutoField(primary_key=True)
    nombre_eespecifico = models.CharField(max_length=100, null=True, blank=True)
    estado_general = models.ForeignKey(EstadoGeneral, to_field='id_egeneral', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_bas_especifico'
        verbose_name_plural = 'Estados específicos'

    def __str__(self):
        return str(self.id_eespecifico)

#3
class TipoRuta(models.Model):
    id_truta = models.AutoField(primary_key=True)
    nombre_truta = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_ruta'
        verbose_name_plural = 'Tipo de ruta'

    def __str__(self):
        return str(self.id_truta)

#4
class CanalSolicitud(models.Model):
    id_csolicitud = models.AutoField(primary_key=True)
    nombre_csolicitud = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_canalsolicitud'
        verbose_name_plural = 'Tipo de medio o canal donde se realiza la solicitud'

    def __str__(self):
        return str(self.id_csolicitud)

#5
class TipoResultadoLlamada(models.Model):
    id_trllamada = models.AutoField(primary_key=True)
    nombre_trllamada = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_trllamadas'
        verbose_name_plural = 'Tipos de resultados de la llamadas'

    def __str__(self):  
        return str(self.id_trllamada)


# MODELOS PARA LAS TABLAS DINÁMICAS DE REGISTRO

#6
class Registro(models.Model):
    registro = models.AutoField(primary_key=True)
    estado =  models.ForeignKey(EstadoEspecifico, to_field='id_eespecifico', on_delete=models.CASCADE, null=True, blank=True)
    objects_id = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    content_type = models.PositiveIntegerField(blank=True, null=True)
    ruta =  models.ForeignKey(TipoRuta, to_field='id_truta', on_delete=models.CASCADE, null=True, blank=True)
    canal =  models.ForeignKey(CanalSolicitud, to_field='id_csolicitud', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'eco_reg_registro'
        verbose_name_plural = 'Registro'

    def __str__(self):
        return str(self.registro)

#7
class FechaTerminos(models.Model):
    id_fterminos = models.AutoField(primary_key=True)
    fecha_actualizacion = models.DateField(null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'eco_reg_fterminos'
        verbose_name_plural = 'Fecha terminos'

    def __str__(self):
        return str(self.id_fterminos)

#8
class TrazabilidadGeneral(models.Model):
    id_trazabilidad = models.AutoField(primary_key=True)
    registro = models.ForeignKey(Registro, to_field='registro', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_reg_tgeneral'
        verbose_name_plural = 'trazabilidad general'

    def __str__(self):
        return str(self.id_trazabilidad)
    
#9
class Trazabilidad(models.Model):
    id_traza = models.AutoField(primary_key=True)
    fecha_recibido = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE,null=True,blank=True)
    Trazabilidad = models.ForeignKey(TrazabilidadGeneral, to_field='id_trazabilidad', on_delete=models.CASCADE,null=True,blank=True)
    

    class Meta:
        db_table = 'eco_reg_trazabilidad'
        verbose_name_plural = 'trazabilidad'

    def __str__(self):
        return str(self.id_traza)


# registro con los formularios de solicitud individual

#10
class fechaDiligenciamientoFormulario(models.Model):
    id_fdformulario = models.AutoField(primary_key=True)
    fecha_dformulario = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'eco_reg_fdiligenciamiento'
        verbose_name_plural = 'fecha de diligenciamiento del formualario'

    def __str__(self):
        return str(self.id_fdformulario)

#11   
class lugarDiligenciamientoFormulario(models.Model):
    id_ldiligenciamiento = models.AutoField(primary_key=True)
    pais = models.ForeignKey(sis_models.Pais, to_field='id_pais', on_delete=models.CASCADE)
    departamento = models.ForeignKey(sis_models.Departamento, to_field='id_departamento', on_delete=models.CASCADE)
    municipio = models.ForeignKey(sis_models.Municipio, to_field='id_municipio', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_reg_ldiligenciamiento'
        verbose_name_plural = 'lugar de diligenciamiento del formualario'

    def __str__(self):
        return str(self.id_ldiligenciamiento)


#12
class DiligenciaFormulario(models.Model):
    id_dformulario = models.AutoField(primary_key=True)
    primer_ndiligencia = models.CharField(max_length=30, null=True, blank=True)
    segundo_ndiligencia = models.CharField(max_length=30, null=True, blank=True)
    primer_adiligencia = models.CharField(max_length=30, null=True, blank=True)
    segundo_adiligencia = models.CharField(max_length=30, null=True, blank=True)
    contacto_tdiligencia = models.CharField(max_length=20, null=True, blank=True)
    correo_ediligencia = models.EmailField(max_length=60, null=True, blank=True)
    entidad_solicitante = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = 'eco_reg_dformulario'
        verbose_name_plural = 'Datos de quien diligencia el formulario'

    def __str__(self):
        return str(self.id_dformulario)
    
#13
class Formulario(models.Model):
    id_formulario = models.AutoField(primary_key=True)
    fecha_diligenciamiento = models.ForeignKey(fechaDiligenciamientoFormulario, to_field='id_fdformulario', on_delete=models.CASCADE)
    lugar_diligenciamiento = models.ForeignKey(lugarDiligenciamientoFormulario, to_field='id_ldiligenciamiento', on_delete=models.CASCADE)
    diligencia = models.ForeignKey(DiligenciaFormulario, to_field='id_dformulario', on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        db_table = 'eco_reg_formulario'
        verbose_name_plural = 'Datos del formulario'

    def __str__(self):
        return str(self.id_formulario)

#14
class FormularioIndividual(Formulario):
    persona = models.ForeignKey(sis_models.DatosBasicosPersona, to_field='id_persona', on_delete=models.CASCADE)
    cpersona = models.ForeignKey(sis_models.DatosComplemetariosPersona, to_field='id_complementarios', on_delete=models.CASCADE)
    ipoblacion = models.ForeignKey(gsc_models.IdPoblacion, to_field='id_ipoblacion', on_delete=models.CASCADE)
    iriesgo = models.ForeignKey(gsc_models.IdRiesgo, to_field='id_iriesgo', on_delete=models.CASCADE)
    consentimiento = models.ForeignKey(gsc_models.Consentimiento, to_field='id_consentimiento', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_reg_formularioindividual'
        verbose_name_plural = 'Datos del formulario individual'

    def __str__(self):
        return str(self.id_formulario)
    
#15
class FormularioColectivo(Formulario):
    colectivo = models.ForeignKey(sis_models.DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)
    factor_diferencial = models.ForeignKey(sis_models.ColectivoFDiferencial, to_field='id_icfdiferencial', on_delete=models.CASCADE)
    medida_cautelar = models.ForeignKey(gsc_models.MedidaCautelarColectivo, to_field='id_mccolectivo', on_delete=models.CASCADE)
    id_representante = models.ForeignKey(sis_models.PersonaColectivo, to_field='id_pcolectivo', on_delete=models.CASCADE)
    poblacion_colectivo = models.ForeignKey(gsc_models.IdPoblacionColectivo, to_field='id_ipcolectivo', on_delete=models.CASCADE)
    hecho_victimizante = models.ForeignKey(gsc_models.HechoVictimizanteColectivo, to_field='id_hvcolectivo', on_delete=models.CASCADE)
    consentimiento =  models.ForeignKey(gsc_models.ConsentimientoColectivo, to_field='id_cocolectivo', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_gsc_formulariocolectivo'
        verbose_name_plural = 'Datos del formulario colectivo'

    def __str__(self):
        return str(self.id_formulario)
    



# registro con los datos de llamadas


#16
class RegistroLlamadas(models.Model):
    id_rllamadas = models.AutoField(primary_key=True)
    registro = models.ForeignKey(Registro, to_field='registro', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE,null=True,blank=True)
    responde_solicitante = models.BooleanField(default=False)
    responde_tercero = models.BooleanField(default=False)
    responde_entidad = models.BooleanField(default=False)
    tiene_dubicacion = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'eco_reg_rllamadas'
        verbose_name_plural = 'regisros de llamadas'

    def __str__(self):
        return str(self.id_rllamadas)
    
#17
class FechaHoraLlamada(models.Model):
    id_fechahora = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    registro_llamada = models.ForeignKey(RegistroLlamadas, to_field='id_rllamadas', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'eco_reg_fhllamada'
        verbose_name_plural = 'fecha y hora de la llamada'

    def __str__(self):  
        return str(self.id_fechahora)
    
#18
class MedioContactoLlamada(models.Model):
    id_mcllamada = models.AutoField(primary_key=True)
    celular_torigen = models.CharField(max_length=12, null=True, blank=True)    
    celular_tdestino = models.CharField(max_length=12, null=True, blank=True)
    registro_llamada = models.ForeignKey(RegistroLlamadas, to_field='id_rllamadas', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'eco_reg_mcllamada'
        verbose_name_plural = 'número de celular o teléfono donde se realiza la llamada y número de quién recibe'

    def __str__(self):  
        return str(self.id_mcllamada)

#19
class InformacionLlamada(models.Model):
    id_infollamada = models.AutoField(primary_key=True)
    numero_intentos = models.SmallIntegerField(blank=True, null=True)
    tipo_rllamada = models.ForeignKey(TipoResultadoLlamada, to_field='id_trllamada', on_delete=models.CASCADE, blank=True, null=True)
    observacion_llamada = models.CharField(max_length=200, null=True, blank=True)
    registro_llamada = models.ForeignKey(RegistroLlamadas, to_field='id_rllamadas', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'eco_reg_infollamada'
        verbose_name_plural = 'Información importante de la llamada'

    def __str__(self):  
        return str(self.id_infollamada)
    
#20
class TerceroRespondeLlamada(models.Model):
    id_terceroresponde = models.AutoField(primary_key=True)
    nombre_terceroresponde = models.CharField(max_length=60, null=True, blank=True)
    apellido_respondetercero = models.CharField(max_length=60, null=True, blank=True)
    registro_llamada = models.ForeignKey(RegistroLlamadas, to_field='id_rllamadas', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'eco_reg_tllamada'
        verbose_name_plural = 'Datos del tercero que responde'

    def __str__(self):  
        return str(self.id_terceroresponde)

#21
class EntidadrespondeLlamada(models.Model):
    id_entidadresponde = models.AutoField(primary_key=True)
    nombre_entidadresponde = models.CharField(max_length=60, null=True, blank=True)
    nombre_personaresponde = models.CharField(max_length=100, null=True, blank=True)
    registro_llamada = models.ForeignKey(RegistroLlamadas, to_field='id_rllamadas', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'eco_reg_ellamada'
        verbose_name_plural = 'Datos de la entidad que responde'

    def __str__(self):  
        return str(self.id_entidadresponde)
    
#22
class UbicacionrespondeLlamada(models.Model):
    id_ubicacionresponde = models.AutoField(primary_key=True)
    pais = models.ForeignKey(sis_models.Pais, to_field='id_pais', on_delete=models.CASCADE, blank=True, null=True)
    departamento = models.ForeignKey(sis_models.Departamento, to_field='id_departamento', on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.ForeignKey(sis_models.Municipio, to_field='id_municipio', on_delete=models.CASCADE, blank=True, null=True)
    responde_urbana = models.BooleanField(default=False)
    responde_rural = models.BooleanField(default=False)
    registro_llamada = models.ForeignKey(RegistroLlamadas, to_field='id_rllamadas', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'eco_reg_ullamada'
        verbose_name_plural = 'Datos de ubicación donde se encuentra el contactado'

    def __str__(self):  
        return str(self.id_ubicacionresponde)
    
#23
class RespondeUrbanaLlamada(models.Model):
    id_respondeurbana = models.CharField(primary_key=True)
    nombre_barrio = models.CharField(max_length=30,  blank=True, null=True)
    ubicacion_responde = models.ForeignKey(UbicacionrespondeLlamada, to_field='id_ubicacionresponde', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        db_table = 'eco_reg_uullamada'
        verbose_name_plural = 'Datos de ubicación urbana donde se encuentra el contactado'

    def __str__(self):  
        return str(self.id_respondeurbana)
    
#24
class RespondeRuralLlamada(models.Model):
    id_responderural = models.CharField(primary_key=True)
    vereda = models.CharField(max_length=30,  blank=True, null=True)
    corregimiento = models.CharField(max_length=30,  blank=True, null=True)
    centro_poblado = models.CharField(max_length=30,  blank=True, null=True)
    ubicacion_responde = models.ForeignKey(UbicacionrespondeLlamada, to_field='id_ubicacionresponde', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        db_table = 'eco_reg_urllamada'
        verbose_name_plural = 'Datos de ubicación rural donde se encuentra el contactado'

    def __str__(self):  
        return str(self.id_responderural)