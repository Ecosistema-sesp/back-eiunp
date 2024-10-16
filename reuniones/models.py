from django.db import models
from sistema import models as sis_models
from usuario import models as usr_modesl
from django.contrib.auth.models import User


# Create your models here.

class TemaReunion(models.Model):
    id_temareunion = models.AutoField(primary_key=True)
    nombre_temareunion = models.CharField(max_length=100)

    class Meta:
        db_table = 'eco_reu_temareunion'
        verbose_name_plural = 'Tema principal de la reunión'

    def __str__(self):
        return str(self.id_tema)
    
class FechaReunion(models.Model):
    id_fechareunion = models.AutoField(primary_key=True)
    fecha_reunion = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'eco_reu_horareunion'
        verbose_name_plural = 'fecha y hora  de la reunión'

    def __str__(self):
        return str(self.id_fechareunion)
    

class SedeUnp(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre_sede = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.ForeignKey(sis_models.Departamento, to_field='id_departamento', on_delete=models.CASCADE, blank=True, null=True)
    Municipio = models.ForeignKey(sis_models.Municipio, to_field='id_municipio', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        db_table = 'eco_reu_sede'
        verbose_name_plural = 'Sedes de la UNP'

    def __str__(self):
        return str(self.id_sede)
    
class LugarReunion(models.Model):
    id_lugarreunion = models.AutoField(primary_key=True)
    sede = models.ForeignKey(SedeUnp, to_field='id_sede', on_delete=models.CASCADE, blank=True, null=True)
    lugar = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_lugarreunion'
        verbose_name_plural = 'lugar de la UNP'

    def __str__(self):
        return str(self.id_sede)
    
class Reuniones(models.Model):
    id_reunion = models.AutoField(primary_key=True)
    fecha = models.ForeignKey(FechaReunion, to_field='id_fechareunion', on_delete=models.CASCADE, blank=True, null=True)
    lugar = models.ForeignKey(LugarReunion, to_field='id_lugarreunion', on_delete=models.CASCADE, blank=True, null=True)
    tema = models.ForeignKey(TemaReunion, to_field='id_temareunion', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_reunion'
        verbose_name_plural = 'reuniones'

    def __str__(self):
        return str(self.id_reunion)
    
class LlaveDesarrolloReunion(models.Model):
    id_tdreunion = models.AutoField(primary_key=True)
    reunion = models.ForeignKey(Reuniones, to_field='id_reunion', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_lldreunion'
        verbose_name_plural = 'llave de desarrollo del los temas de la reunion'

    def __str__(self):
        return str(self.id_tdreunion)
    
class DesarrolloReunion(models.Model):
    id_dreunion = models.AutoField(primary_key=True)
    descripcion_tema = models.CharField(max_length=200, blank=True, null=True)
    llave_dreunion = models.ForeignKey(LlaveDesarrolloReunion, to_field='id_tdreunion', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_desarrolloreunion'
        verbose_name_plural = 'desarrollo del los temas de la reunion'

    def __str__(self):
        return str(self.id_dreunion)
    
class LlaveConclusionReunion(models.Model):
    id_tcreunion = models.AutoField(primary_key=True)
    reunion = models.ForeignKey(Reuniones, to_field='id_reunion', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_llcreunion'
        verbose_name_plural = 'llave de conclusiones del los temas de la reunion'

    def __str__(self):
        return str(self.id_tcreunion)
    
class ConclusionReunion(models.Model):
    id_creunion = models.AutoField(primary_key=True)
    descripcion_conclucion = models.CharField(max_length=200, blank=True, null=True)
    llave_creunion = models.ForeignKey(LlaveConclusionReunion, to_field='id_tcreunion', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_conclusionreunion'
        verbose_name_plural = 'conclusiones del los temas de la reunion'

    def __str__(self):
        return str(self.id_creunion)
    
class LlaveAsistenteReunion(models.Model):
    id_lareunion = models.AutoField(primary_key=True)
    reunion = models.ForeignKey(Reuniones, to_field='id_reunion', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_llareunion'
        verbose_name_plural = 'llave de asistentes de la reunion'

    def __str__(self):
        return str(self.id_lareunion)

class AsistenteReunion(models.Model):
    id_areunion = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, blank=True, null=True)
    llave_areunion = models.ForeignKey(LlaveAsistenteReunion, to_field='id_lareunion', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_asistentereunion'
        verbose_name_plural = 'Asistentes a las reunion'

    def __str__(self):
        return str(self.id_areunion)
    
class LlaveResponsableReunion(models.Model):
    id_lrreunion = models.AutoField(primary_key=True)
    reunion = models.ForeignKey(Reuniones, to_field='id_reunion', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_llrreunion'
        verbose_name_plural = 'llave de responsables de la reunion'

    def __str__(self):
        return str(self.id_lrreunion)

class ResponsableReunion(models.Model):
    id_responsablereunion = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, blank=True, null=True)
    llave_areunion = models.ForeignKey(LlaveResponsableReunion, to_field='id_lrreunion', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_responsablereunion'
        verbose_name_plural = 'Asistentes a las reunion'

    def __str__(self):
        return str(self.id_responsablereunion)

class RelatorReunion(models.Model):
    id_relatorreunion = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, blank=True, null=True)
    llave_areunion = models.ForeignKey(LlaveResponsableReunion, to_field='id_lrreunion', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_relatorreunion'
        verbose_name_plural = 'Asistentes a las reunion'

    def __str__(self):
        return str(self.id_relatorreunion)

class LlaveCompromisoReunion(models.Model):
    id_lrcompromiso = models.AutoField(primary_key=True)
    reunion = models.ForeignKey(Reuniones, to_field='id_reunion', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_lrcompromisos'
        verbose_name_plural = 'llave de compromisos de la reunion'

    def __str__(self):
        return str(self.id_lrcompromiso)

class CompromisoReunion(models.Model):
    id_compromiso = models.AutoField(primary_key=True)
    descripcion_compromiso = models.CharField(max_length=500, blank=True, null=True)
    compromiso_cumplido = models.BooleanField(default=False, blank=True, null=True)
    llave_compromiso = models.ForeignKey(LlaveCompromisoReunion, to_field='id_lrcompromiso', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_rcompromisos'
        verbose_name_plural = 'Compromisos de la reunion'

    def __str__(self):
        return str(self.id_compromiso)
    
class ResponsableCompromiso(models.Model):
    id_responsablecompromiso = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, blank=True, null=True)
    id_compromiso = models.ForeignKey(CompromisoReunion, to_field='id_compromiso', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_responsablecompromiso'
        verbose_name_plural = 'responsable de los compromisos de la reunión'

    def __str__(self):
        return str(self.id_responsablecompromiso)
    
class FechaCompromiso(models.Model):
    id_fechacompromiso = models.AutoField(primary_key=True)
    fecha_iniciocompromiso = models.DateField(blank=True, null=True)
    fecha_fincompromiso = models.DateField(blank=True, null=True)
    id_compromiso = models.ForeignKey(CompromisoReunion, to_field='id_compromiso', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_fechacompromiso'
        verbose_name_plural = 'fecha de los compromisos de la reunión'

    def __str__(self):
        return str(self.id_fechacompromiso)
    
class TipoEstadoCompromiso(models.Model):
    id_tecompromiso = models.AutoField(primary_key=True)
    nombre_tecompromiso = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_tecompromiso'
        verbose_name_plural = 'tipo de estados de los compromisos de la reunión'

    def __str__(self):
        return str(self.id_tecompromiso)
    
class EstadoCompromiso(models.Model):
    id_estadocompromiso = models.AutoField(primary_key=True)
    estado_compromiso = models.ForeignKey(TipoEstadoCompromiso, to_field='id_tecompromiso', on_delete=models.CASCADE, blank=True, null=True)
    id_compromiso = models.ForeignKey(CompromisoReunion, to_field='id_compromiso', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_reu_estadocompromiso'
        verbose_name_plural = 'Estado de los compromisos de la reunión'

    def __str__(self):
        return str(self.id_estadocompromiso)