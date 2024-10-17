from django.db import models
from django.contrib.contenttypes.fields import  GenericRelation
from django.contrib.contenttypes.models import ContentType
from sistema import models as sis_models

# Create your models here.

# MODELOS DE SERVICIO AL CIUDADAO ESTÁTICOS

class TipoDiscapacidad(models.Model):
    id_tdiscapacidad = models.SmallAutoField(primary_key=True)
    nombre_tdiscapacidad = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_tipodiscapacidad'
        verbose_name_plural = 'Tipo de discapacidad'

    def __str__(self):
        return str(self.nombre_tdiscapacidad)

class TipoGrupoEtnico(models.Model):
    id_tetnico = models.SmallAutoField(primary_key=True)
    nombre_tetnico = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_tipoetnico'
        verbose_name_plural = 'Tipo de grupo étnico'

    def __str__(self):
        return str(self.nombre_tetnico)

class TipoOrganizacionPersona(models.Model):
    id_torganizacion = models.SmallAutoField(primary_key=True)
    nombre_torganizacion = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_tipoorganizacion'
        verbose_name_plural = 'Tipo de organizaciones'

    def __str__(self):
        return str(self.nombre_torganizacion)

class TipoMedidaCautelar(models.Model):
    id_tmcautelar = models.SmallAutoField(primary_key=True)
    nombre_tmcautelar = models.CharField(max_length=150)

    class Meta:
        db_table = 'eco_bas_tipomcautelar'
        verbose_name_plural = 'Tipo de medida cautelar de la persona'

    def __str__(self):
        return str(self.nombre_tmcautelar)

class TipoSituacionesRiesgo(models.Model):
    id_tiporiesgo = models.AutoField(primary_key=True)
    nombre_sriesgo = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_tiporiesgo'
        verbose_name_plural = 'Tipos de situaciones de riesgo'
    def __str__(self):
        return str(self.nombre_sriesgo)

class TipoMediosSituacion(models.Model):
    id_msituacion = models.AutoField(primary_key=True)
    nombre_msituacion = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_mediosituacion'
        verbose_name_plural = 'Tipos de medios por el que se presento la situación'

    def __str__(self):
        return str(self.nombre_msituacion)
    
class TipoPoblacion(models.Model):
    id_tipopoblacion = models.AutoField(primary_key=True)
    nombre_tpoblacion = models.CharField(max_length=170, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_tipopoblacion'
        verbose_name_plural = 'Tipo de población objeto'

    def __str__(self):
        return str(self.id_tipopoblacion)
    
class PoblacionObjeto(models.Model):
    id_poblacionobjeto = models.AutoField(primary_key=True)
    nombre_pobjeto = models.CharField(max_length=700, null=True, blank=True)
    tipo_poblacion = models.ForeignKey(TipoPoblacion, to_field='id_tipopoblacion', on_delete=models.CASCADE)
    identificador = models.CharField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'eco_bas_poblacionobjeto'
        verbose_name_plural = 'Listado de las poblaciones objeto'

    def __str__(self):
        return str(self.id_poblacionobjeto)

class TipoCategoriaOrganizacion(models.Model):
    id_catorganizacion = models.AutoField(primary_key=True)
    nombre_catorganizacion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_catorganizacion'
        verbose_name_plural = 'Categorias de organizaciones'

    def __str__(self):
        return str(self.id_catorganizacion)

class CategoriaPnis(models.Model):
    id_categoriapnis = models.AutoField(primary_key=True)
    nombre_categoriapnis = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        db_table = 'eco_bas_categoriapnis'
        verbose_name_plural = 'Categorias para el pnis'
    def __str__(self):
        return str(self.id_categoriapnis)

class tipoEntidadAcreditadora(models.Model):
    id_teacreditadora = models.AutoField(primary_key=True)
    nombre_teacreditadora = models.CharField(max_length=40, null=True,blank=True)
    
    class Meta:
        db_table = 'eco_bas_teacolectivo'
        verbose_name_plural = 'Entidades acreditadoras del colectivo'

    def __str__(self):
        return str(self.id_teacreditadora)
    
class PoblacionGeneralColectivo(models.Model):
    id_tpgcolectivo = models.SmallAutoField(primary_key=True)
    nombre_tpgcolectivo = models.CharField(max_length=700, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_tpgcolectivo'
        verbose_name_plural = 'Tipo de poblacion general colectivo'

    def __str__(self):
        return str(self.id_tpgcolectivo)

class TipoPoblacionColectivo(models.Model):
    id_tpcolectivo = models.SmallAutoField(primary_key=True)
    nombre_tpcolectivo = models.CharField(max_length=700, null=True, blank=True)
    poblacion_gcolectivo = models.ForeignKey(PoblacionGeneralColectivo, to_field='id_tpgcolectivo', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_tpoblacioncolectivo'
        verbose_name_plural = 'Tipo de poblacion colectivo'

    def __str__(self):
        return str(self.id_tpcolectivo)
    
class TipoPoblacionSesp(models.Model):
    id_poblacionsesp = models.SmallAutoField(primary_key=True)
    nombre_poblacionsesp = models.CharField(max_length=150, null=True, blank=True)
    tipo_poblacion = models.ForeignKey(TipoPoblacionColectivo, to_field='id_tpcolectivo', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_tpcsesp'
        verbose_name_plural = 'Tipo de poblacion colectivo de la sesp'

    def __str__(self):
        return str(self.id_poblacionsesp)
    


# MODELOS PARA SERVICIO AL CIUDADANO DINÁMICOS

class DireccionNotificacionPersona(models.Model):
    id_notificacion = models.IntegerField(primary_key=True)
    ubicacion_notificacion = GenericRelation(sis_models.DatosUbicacion)
    persona = models.ForeignKey(sis_models.DatosBasicosPersona, to_field='id_persona', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_npersona'
        verbose_name_plural = 'Datos de nacimiento de la persona'

    def __str__(self):
        return str(self.ubicacion_notificacion)
    
class NombreIdentitario(models.Model):
    id_identitario = models.AutoField(primary_key=True)
    nombre_identitario = models.CharField(max_length=60, null=True, blank=True)
    cpersona = models.ForeignKey(sis_models.DatosComplemetariosPersona, to_field='id_complementarios', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_nidentitario'
        verbose_name_plural = 'Nombre identitario'

    def __str__(self):
        return str(self.id_identitario)
    
class PersonasCargo(models.Model):
    id_pcargo = models.SmallAutoField(primary_key=True)
    numero_pcargo= models.SmallIntegerField(null=True, blank=True)
    factor_diferencial = models.ForeignKey(sis_models.DatosComplemetariosPersona, to_field='id_complementarios', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_personascargo'
        verbose_name_plural = 'Número de personas a cargo'

    def __str__(self):
        return str(self.id_pcargo)
    
class DispacidadPersona(models.Model):
    id_dpersona = models.SmallAutoField(primary_key=True)
    tipo_discapacidad = models.ForeignKey(TipoDiscapacidad, to_field='id_tdiscapacidad',on_delete=models.CASCADE)
    cpersona = models.ForeignKey(sis_models.DatosComplemetariosPersona, to_field='id_complementarios', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sac_discapacidadpersona'
        verbose_name_plural = 'Discapacidad de la persona'

    def __str__(self):
        return str(self.id_dpersona)
    
class GrupoEtnicoPersona(models.Model):
    id_getnico = models.AutoField(primary_key=True)
    tipo_getnico = models.ForeignKey(TipoGrupoEtnico, to_field='id_tetnico', on_delete=models.CASCADE)
    cpersona = models.ForeignKey(sis_models.DatosComplemetariosPersona, to_field='id_complementarios', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_grupoetnico'
        verbose_name_plural = 'Grupo étnico de la persona'

    def __str__(self):
        return str(self.id_getnico)
    
class GrupoIndigena(models.Model):
    id_gindigena = models.AutoField(primary_key=True)
    etnia = models.CharField(max_length=100, null=True, blank=True)
    resguardo = models.CharField(max_length=100, null=True, blank=True)
    comunidad = models.CharField(max_length=100, null=True, blank=True)
    parcialidad = models.CharField(max_length=100, null=True, blank=True)
    comunidad_sregistro = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'eco_gsc_grupoindigena'
        verbose_name_plural = 'Grupo indígena de la persona'

    def __str__(self):
        return str(self.id_gindigena)
    
class EtnicoIndigena(models.Model):
    id_etnicoindigena = models.AutoField(primary_key=True)
    grupo_etnico = models.ForeignKey(GrupoEtnicoPersona, to_field='id_getnico', on_delete=models.CASCADE)
    grupo_indigena = models.ForeignKey(GrupoIndigena, to_field='id_gindigena', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_etnicoindigena'
        verbose_name_plural = 'Grupo étnico indígena de la persona'

    def __str__(self):
        return str(self.id_etnicoindigena)

class OtroGrupoPersona(models.Model):
    id_ogetnico = models.AutoField(primary_key=True)
    nombre_ccomunitario = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'eco_gsc_ogetnico'
        verbose_name_plural = 'Otro grupo de la persona'

    def __str__(self):
        return str(self.id_ogetnico)
    
class EtnicoConcejo(models.Model):
    id_etnicoconcejo = models.AutoField(primary_key=True)
    grupo_etnico = models.ForeignKey(GrupoEtnicoPersona, to_field='id_getnico', on_delete=models.CASCADE)
    otro_grupo = models.ForeignKey(OtroGrupoPersona, to_field='id_ogetnico', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_etnicoconcejo'
        verbose_name_plural = 'Otro grupo étnico de la persona'

    def __str__(self):
        return str(self.id_etnicoconcejo)
    
class Organizacion(models.Model):
    id_organizacion = models.SmallAutoField(primary_key=True)
    nombre_organizacion = models.CharField(max_length=100, null=True, blank=True)
    tipo_organizacion = models.ForeignKey(TipoOrganizacionPersona, to_field='id_torganizacion', on_delete=models.CASCADE)
    tiene_pjuridica = models.BooleanField(default=False)

    class Meta:
        db_table = 'eco_gsc_organizacion'
        verbose_name_plural = 'Organizaciones'

    def __str__(self):
        return str(self.id_organizacion)

class OtraOrganizacion(models.Model):
    id_oorganizacion = models.SmallAutoField(primary_key=True)
    nombre_oorganizacion = models.CharField(max_length=100, null=True, blank=True)
    organizacion = models.ForeignKey(Organizacion, to_field='id_organizacion', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_oorganizacion'
        verbose_name_plural = 'Otro tipo de organización'

    def __str__(self):
        return str(self.id_oorganizacion)

class PersoneriaJuridica(models.Model):
    id_pjuridica = models.SmallAutoField(primary_key=True)
    numero_pjuridica= models.CharField(max_length=20, blank=True, null=True)
    organizacion = models.ForeignKey(Organizacion, to_field='id_organizacion', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_pjorganizacion'
        verbose_name_plural = 'Personería jurídica de la organización'

    def __str__(self):
        return str(self.id_pjuridica)
    
class OrganizacionPersona(models.Model):
    id_orgpersona = models.SmallAutoField(primary_key=True)
    cpersona = models.ForeignKey(sis_models.DatosComplemetariosPersona, to_field='id_complementarios', on_delete=models.CASCADE)
    organizacion = models.ForeignKey(Organizacion, to_field='id_organizacion', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_organizacionpersona'
        verbose_name_plural = 'Organización a la que pertenece la persona'

    def __str__(self):
        return str(self.id_orgpersona)
        
class MedidaCuatelarPersona(models.Model):
    id_mcautelar = models.AutoField(primary_key=True)
    tipo_mcautelar = models.ForeignKey(TipoMedidaCautelar, to_field='id_tmcautelar', on_delete=models.CASCADE)
    cpersona = models.ForeignKey(sis_models.DatosComplemetariosPersona, to_field='id_complementarios', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_mcautelar'
        verbose_name_plural = 'Medida cautelar de la persona'

    def __str__(self):
        return str(self.id_mcautelar)
    
class ActividadAmbientalPersona(models.Model):
    id_actividadambiental = models.AutoField(primary_key=True)
    desarrolla_aambiental = models.BooleanField(default=False)
    cpersona = models.ForeignKey(sis_models.DatosComplemetariosPersona, to_field='id_complementarios', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_aambiental'
        verbose_name_plural = 'Dasarrolla actividad ambiental'

    def __str__(self):
        return str(self.id_actividadambiental)
    
class IdRiesgo(models.Model):
    id_iriesgo = models.AutoField(primary_key=True)
    persona = models.ForeignKey(sis_models.DatosBasicosPersona, to_field='id_persona', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_identificacionriesgo'
        verbose_name_plural = 'Identificación del Riesgo'

    def __str__(self):
        return str(self.id_iriesgo)
    
class Evidencias(models.Model):
    id_evidencias = models.AutoField(primary_key=True)
    ruta_evidencias = models.FileField(upload_to='evidencias/', null=False, blank=False)
    id_iriesgo = models.ForeignKey(IdRiesgo, to_field='id_iriesgo', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_doc_evidenciasRiesgo'
        verbose_name_plural = 'tabla para mantener las evidencias cargadas por el usuario.'
        
    def __str__(self):
        return str(self.id_evidencias)
    
class IdentificacionSituacion(models.Model):
    id_identificacionSituacion = models.AutoField(primary_key=True)
    identificacion_riesgo = models.ForeignKey(IdRiesgo, to_field='id_iriesgo', on_delete=models.CASCADE)
    tipo_sriesgo = models.ForeignKey(TipoSituacionesRiesgo, to_field='id_tiporiesgo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_identificacionsituacion'
        verbose_name_plural = 'Identificación de las situaciones de riesgo'

    def __str__(self):
        return str(self.id_identificacionSituacion)
    
class OtraSituacionRiesgo(models.Model):
    id_osriesgo = models.AutoField(primary_key=True)
    nombre_osituacion = models.CharField(max_length=50, null=True, blank=True)
    identificacion_situacion = models.ForeignKey(IdRiesgo, to_field='id_iriesgo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_osriesgo'
        verbose_name_plural = 'Otra situación de riesgo'
    def __str__(self):
        return str(self.id_osriesgo)
    
class IdentificacionMedio(models.Model):
    id_identificacionmedio = models.AutoField(primary_key=True)
    identificacion_riesgo = models.ForeignKey(IdRiesgo, to_field='id_iriesgo', on_delete=models.CASCADE)
    medio_situacion = models.ForeignKey(TipoMediosSituacion, to_field='id_msituacion', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_identificacionmedio'
        verbose_name_plural = 'Identificacion de los medios de la situación de riesgo'

    def __str__(self):
        return str(self.id_identificacionmedio)
    
class RelatosHechos(models.Model):
    id_rhechos = models.AutoField(primary_key=True)
    relato_hechos = models.CharField(max_length=5000, null=False, blank=False)
    identificacion_riesgo = models.ForeignKey(IdRiesgo, to_field='id_iriesgo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_relatohechos'
        verbose_name_plural = 'Relato de los hechos victimizantes'

    def __str__(self):
        return str(self.id_rhechos)
    
class IdPoblacion(models.Model):
    id_ipoblacion = models.AutoField(primary_key=True)
    persona = models.ForeignKey(sis_models.DatosBasicosPersona, to_field='id_persona', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_gsc_idpoblacion'
        verbose_name_plural = 'Identificación de la población objeto'

    def __str__(self):
        return str(self.id_ipoblacion)
    
class IdentificacionPoblacionObjeto(models.Model):
    id_ipobjeto = models.AutoField(primary_key=True)
    identificacion_poblacion = models.ForeignKey(IdPoblacion, to_field='id_ipoblacion', on_delete=models.CASCADE)
    poblacion_objeto = models.ForeignKey(PoblacionObjeto, to_field='id_poblacionobjeto', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_ipobjeto'
        verbose_name_plural = 'Poblaciones objeto identificadas por la persona'

    def __str__(self):
        return str(self.id_ipobjeto)
    
class FilePoblacion(models.Model):
    id_fpoblacion = models.AutoField(primary_key=True)
    ruta_fpoblacion = models.FileField(upload_to='poblacion_objeto/', null=False, blank=False)
    id_ipoblacion = models.ForeignKey(IdPoblacion, to_field= 'id_ipoblacion', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_doc_filepoblacion'
        verbose_name_plural = 'Documento de acreditacion poblacional.'
    
    def __str__(self):
        return str(self.id_fpoblacion)
    
class OrganizacionPolitica(models.Model):
    id_porganizacion = models.AutoField(primary_key=True)
    pertene_poprganizacion = models.BooleanField(default=False)
    poblacion_objeto = models.ForeignKey(IdPoblacion, to_field='id_ipoblacion', on_delete=models.CASCADE)
    tipo_catorganizacion = models.ForeignKey(TipoCategoriaOrganizacion, to_field='id_catorganizacion', on_delete=models.CASCADE)
    class Meta:
        db_table = 'eco_gsc_porganizacion'
        verbose_name_plural = 'Organizaciones Politicas poblacion 1'
    def __str__(self):
        return str(self.id_porganizacion)
    
class CargoOrganizacion(models.Model):
    id_corganizacion = models.AutoField(primary_key=True)
    nombre_corganizacion = models.CharField(max_length=200, null=True, blank=True)
    Poblacion_objeto = models.ForeignKey(IdPoblacion, to_field='id_ipoblacion', on_delete=models.CASCADE)
    class Meta:
        db_table = 'eco_gsc_corganizacion'
        verbose_name_plural = 'Cargos de las organizaciones poblacion 2'

    def __str__(self):
        return str(self.id_corganizacion)

class DatosPnis(models.Model):
    id_pnis = models.AutoField(primary_key=True)
    pertenece_pnis = models.BooleanField(default=False)
    categoria_pnis = models.ForeignKey(CategoriaPnis, to_field='id_categoriapnis', on_delete=models.CASCADE)
    poblacion_objeto = models.ForeignKey(IdPoblacion, to_field='id_ipoblacion', on_delete=models.CASCADE)
    class Meta:
        db_table = 'eco_gsc_datospnis'
        verbose_name_plural = 'Datos del PNIS'
    def __str__(self):
        return str(self.id_pnis)
    
class Consentimiento(models.Model):
    id_consentimiento = models.AutoField(primary_key=True)
    acepta_tdpersonales = models.BooleanField(null=False)
    autoriza_pnacional = models.BooleanField(null=False)
    autoriza_cmujeres = models.BooleanField(null=False)
    persona = models.ForeignKey(sis_models.DatosComplemetariosPersona, to_field='id_complementarios', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_consentimiento'
        verbose_name_plural = 'Consentimiento de la persona'

    def __str__(self):
        return str(self.id_consentimiento)
    
class funcionColectivo(models.Model):
    id_fcolectivo = models.AutoField(primary_key=True)
    organizacion_stnivel = models.CharField(max_length=300, blank=True, null=True)
    descripcion_funcion = models.CharField(max_length=300, blank=True, null=True)
    colectivo = models.ForeignKey(sis_models.DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_fcolectivo'
        verbose_name_plural = 'Función del colectivo'

    def __str__(self):
        return str(self.id_fcolectivo)

class EntidadAcreditadora(models.Model):
    id_eacreditadora = models.AutoField(primary_key=True)
    Tipo_eacreditadora = models.ForeignKey(tipoEntidadAcreditadora, to_field='id_teacreditadora', on_delete=models.CASCADE, blank=True, null=True)
    colectivo = models.ForeignKey(sis_models.DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'eco_gsc_eacreditadora'
        verbose_name_plural = 'Entidad acreditadora'

    def __str__(self):
        return str(self.id_eacreditadora)
    
class CantidadPersonasDiscapacidad(models.Model):
    id_cpdiscapacidad = models.AutoField(primary_key=True)
    cantidad_pdiscapacidad = models.SmallIntegerField(default=0, null=True, blank=True)
    informacion_cfdiferencial = models.ForeignKey(sis_models.InformaciónColectivoFactorDiferencial, to_field='id_icfdiferencial', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_cpdiscapacidad'
        verbose_name_plural = 'Cantidad de personas con discapacidad del colectivo'
        
    def __str__(self):
        return str(self.id_cpdiscapacidad)
    
class CantidadPersonasIndigena(models.Model):
    id_cpindigena = models.AutoField(primary_key=True)
    cantidad_pindigena = models.SmallIntegerField(default=0, null=True, blank=True)
    informacion_cfdiferencial = models.ForeignKey(sis_models.InformaciónColectivoFactorDiferencial, to_field='id_icfdiferencial', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_cpindigena'
        verbose_name_plural = 'Cantidad de personas indígenas del colectivo'
        
    def __str__(self):
        return str(self.id_cpindigena)
    
class cantidadPersonasAfrocolombianos(models.Model):
    id_cpafrocolombiano = models.AutoField(primary_key=True)
    cantidad_pafrocolombiano = models.SmallIntegerField(default=0, null=True, blank=True)
    informacion_cfdiferencial = models.ForeignKey(sis_models.InformaciónColectivoFactorDiferencial, to_field='id_icfdiferencial', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_cpafrocolombiano'
        verbose_name_plural = 'Cantidad de personas afrocolombianos del colectivo'
        
    def __str__(self):
        return str(self.id_cpafrocolombiano)
    
class cantidadPersonasNegro(models.Model):
    id_cpnegro = models.AutoField(primary_key=True)
    cantidad_pnegro = models.SmallIntegerField(default=0, null=True, blank=True)
    informacion_cfdiferencial = models.ForeignKey(sis_models.InformaciónColectivoFactorDiferencial, to_field='id_icfdiferencial', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_cpnegro'
        verbose_name_plural = 'Cantidad de personas negras del colectivo'
        
    def __str__(self):
        return str(self.id_cpnegro)
    
class cantidadPersonasRaizal(models.Model):
    id_cpraizal = models.AutoField(primary_key=True)
    cantidad_praizal = models.SmallIntegerField(default=0, null=True, blank=True)
    informacion_cfdiferencial = models.ForeignKey(sis_models.InformaciónColectivoFactorDiferencial, to_field='id_icfdiferencial', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_cpraizal'
        verbose_name_plural = 'Cantidad de personas raizales del colectivo'
        
    def __str__(self):
        return str(self.id_cpraizal)

class cantidadPersonasPalenquero(models.Model):
    id_cppalenquero = models.AutoField(primary_key=True)
    cantidad_ppalenquero = models.SmallIntegerField(default=0, null=True, blank=True)
    informacion_cfdiferencial = models.ForeignKey(sis_models.InformaciónColectivoFactorDiferencial, to_field='id_icfdiferencial', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_cppalenquero'
        verbose_name_plural = 'Cantidad de personas palenqueros del colectivo'
        
    def __str__(self):
        return str(self.id_cppalenquero)
    
class cantidadPersonasRomGitano(models.Model):
    id_cpromgitano = models.AutoField(primary_key=True)
    cantidad_promgitano = models.SmallIntegerField(default=0, null=True, blank=True)
    informacion_cfdiferencial = models.ForeignKey(sis_models.InformaciónColectivoFactorDiferencial, to_field='id_icfdiferencial', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_cpromgitano'
        verbose_name_plural = 'Cantidad de personas rom o gitanos del colectivo'
        
    def __str__(self):
        return str(self.id_cpromgitano)
    
class CorrespondenciaColectivo(models.Model):
    id_ccolectivo = models.AutoField(primary_key=True)
    ubicacion_ccolectivo = GenericRelation(sis_models.DatosUbicacion)

    class Meta:
        db_table = 'eco_gsc_ccolectivo'
        verbose_name_plural = 'Dirección de correspondencia del colectivo'
        
    def __str__(self):
        return str(self.id_ccolectivo)
    
class MedidaCautelarColectivo(models.Model):
    id_mccolectivo = models.AutoField(primary_key=True)
    es_bmcocomisionidhumanos = models.BooleanField(default=False, null=True, blank=True)
    es_bmcocorteidhumanos = models.BooleanField(default=False, null=True, blank=True)
    es_bmcojrepublica = models.BooleanField(default=False, null=True, blank=True)
    es_bmpsesp = models.BooleanField(default=False, blank=True, null=True)
    colectivo = models.ForeignKey(sis_models.DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_bmccolectivo'
        verbose_name_plural = 'Beneficiario de alguna medida cautelar'
        
    def __str__(self):
        return str(self.id_mccolectivo)
    
class mcComisionInternacional(models.Model):
    id_mccomision = models.AutoField(primary_key=True)
    numero_medida = models.CharField(max_length=20, blank=True, null=True)
    id_mccolectivo = models.ForeignKey(MedidaCautelarColectivo, to_field='id_mccolectivo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_mccomision'
        verbose_name_plural = 'número medida cautelar comisión interamericana de derechos humanos'
        
    def __str__(self):
        return str(self.id_mccomision)
    
class mcCorteInternacional(models.Model):
    id_mccorte = models.AutoField(primary_key=True)
    numero_medida = models.CharField(max_length=20, blank=True, null=True)
    id_mccolectivo = models.ForeignKey(MedidaCautelarColectivo, to_field='id_mccolectivo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_mccorte'
        verbose_name_plural = 'número medida cautelar corte interamericana de derechos humanos'
        
    def __str__(self):
        return str(self.id_mccorte)
    
class mcJuezRepublica(models.Model):
    id_mcjrepublica = models.AutoField(primary_key=True)
    numero_medida = models.CharField(max_length=20, blank=True, null=True)
    id_mccolectivo = models.ForeignKey(MedidaCautelarColectivo, to_field='id_mccolectivo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_mcjrepublica'
        verbose_name_plural = 'número medida cautelar otorgado por un juez de la república'
        
    def __str__(self):
        return str(self.id_mcjrepublica)
    
class EntidadSolicitanteColectivo(models.Model):
    id_esolicitante = models.AutoField(primary_key=True)
    nombre_esolicitante = models.CharField(max_length=100, blank=True, null=True)
    colectivo = models.ForeignKey(sis_models.DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_esolicitante'
        verbose_name_plural = 'Entidad solicitante'

    def __str__(self):
        return str(self.id_esolicitante)
    
class ActividadPersonaColectivo(models.Model):
    id_apcolectivo = models.AutoField(primary_key=True)
    descripcion_actividad = models.CharField(max_length=300, null=True, blank=True)
    persona_colectivo = models.ForeignKey(sis_models.PersonaColectivo, to_field='id_pcolectivo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_apcolectivo'
        verbose_name_plural = 'Actividades de las personas dentro del colectivo'

    def __str__(self):
        return str(self.id_apcolectivo)

class IdPoblacionColectivo(models.Model):
    id_ipcolectivo = models.AutoField(primary_key=True)
    colectivo = models.ForeignKey(sis_models.DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_gsc_idpcolectivo'
        verbose_name_plural = 'Identificación de la población objeto para colectivo'

    def __str__(self):
        return str(self.id_ipcolectivo)
    
class PoblacionColectivo(models.Model):
    id_pcoelctivo = models.AutoField(primary_key=True)
    tipo_pcolectivo = models.ForeignKey(TipoPoblacionColectivo, to_field='id_tpcolectivo', on_delete=models.CASCADE)
    poblacion_colectivo = models.ForeignKey(IdPoblacionColectivo, to_field='id_ipcolectivo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_poblacioncolectivo'
        verbose_name_plural = 'Poblacion al que pertenece el colectivo'

    def __str__(self):
        return str(self.id_pcoelctivo)

class PoblacionColectivoSesp(models.Model):
    id_pcsesp = models.AutoField(primary_key=True)
    poblacion_sesp = models.ForeignKey(TipoPoblacionSesp, to_field='id_poblacionsesp', on_delete=models.CASCADE)
    poblacion_colectivo = models.ForeignKey(IdPoblacionColectivo, to_field='id_ipcolectivo', on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        db_table = 'eco_gsc_psesp'
        verbose_name_plural = 'Poblacion al que pertenece el colectivo si es de la sesp'

    def __str__(self):
        return str(self.id_pcsesp)
    
class ActividadesColectivo(models.Model):
    id_acolectivo = models.AutoField(primary_key=True)
    descripcion_actividad = models.CharField(max_length=2000, blank=True, null=True)
    poblacion_colectivo = models.ForeignKey(IdPoblacionColectivo, to_field='id_ipcolectivo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_gsc_acolectivo'
        verbose_name_plural = 'actividadeds del colectivo'

    def __str__(self):
        return str(self.id_acolectivo)
    
class HechoVictimizanteColectivo(models.Model):
    id_hvcolectivo = models.AutoField(primary_key=True)
    descripcion_hvcolectivo = models.CharField(max_length=5000, null=True, blank=True)
    colectivo = models.ForeignKey(sis_models.DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sis_hvcolectivo'
        verbose_name_plural = 'Hechos victimizantes del colectivo'

    def __str__(self):
        return str(self.id_hvcolectivo)

class ConsentimientoColectivo(models.Model):
    id_cocolectivo = models.AutoField(primary_key=True)
    acepta_tdpersonales = models.BooleanField(null=False)
    autoriza_mpfpublica = models.BooleanField(null=False)
    colectivo = models.ForeignKey(sis_models.DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sis_consentimientoColectivo'
        verbose_name_plural = 'Consentimiento del colectivo'

    def __str__(self):
        return str(self.id_cocolectivo)