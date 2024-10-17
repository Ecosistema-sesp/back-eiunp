from django.db import models
from django.db import models
from django.contrib.contenttypes.fields import  GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geo_models


# Create your models here.

# MODELOS PARA LAS TABLAS ESTÁTICAS 

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=170, null=False, blank=False)
    es_colombia = models.BooleanField(default=False)

    class Meta:
        db_table = 'eco_ext_pais'
        verbose_name_plural = 'Países'

    def __str__(self):
        return str(self.id_pais)
    
class Departamento(models.Model):
    id_departamento = models.IntegerField(primary_key=True)
    nombre_departamento = models.CharField(max_length=85, null=False, blank=False)
    pais = models.ForeignKey(Pais, to_field='id_pais', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_ext_departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return str(self.id_departamento)
    
class Municipio(models.Model):
    id_municipio = models.IntegerField(primary_key=True)
    nombre_municipio = models.CharField(max_length=85, null=False, blank=False)
    departamento = models.ForeignKey(Departamento, to_field='id_departamento', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_ext_municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return str(self.id_municipio)
    
class ZonaUbicacion(models.Model):
    id_zubicacion = models.SmallAutoField(primary_key=True)
    nombre_zubicacion = models.CharField(max_length=10)

    class Meta:
        db_table = 'eco_bas_zonaubicacion'
        verbose_name_plural = 'Zona de ubicación'

    def __str__(self):
        return str(self.nombre_zubicacion)

class TipoIdentificacion(models.Model):
    id_tidentificacion = models.SmallAutoField(primary_key=True)
    nombre_tidentificacion = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_tipoidentificacion'
        verbose_name_plural = 'Tipo de identificación'

    def __str__(self):
        return str(self.nombre_tidentificacion)
    
class TipoGenero(models.Model):
    id_tgenero = models.SmallAutoField(primary_key=True)
    nombre_tgenero = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_tipogenero'
        verbose_name_plural = 'Tipo de género'

    def __str__(self):
        return str(self.nombre_tgenero)
    
class EstadoCivil(models.Model):
    id_ecivil = models.SmallAutoField(primary_key=True)
    nombre_ecivil = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_estadocivil'
        verbose_name_plural = 'Estado civil'

    def __str__(self):
        return str(self.nombre_ecivil)
    
class GpRh(models.Model):
    id_grh = models.SmallAutoField(primary_key=True)
    nombre_grh = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_gruporh'
        verbose_name_plural = 'Grupo rh'

    def __str__(self):
        return str(self.nombre_grh)

class FondoPensiones(models.Model):
    id_fpensiones = models.SmallAutoField(primary_key=True)
    nombre_fpensiones = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_fpensiones'
        verbose_name_plural = 'Fondo de pensiones'

    def __str__(self):
        return str(self.nombre_fpensiones)
    
class Eps(models.Model):
    id_eps = models.SmallAutoField(primary_key=True)
    nombre_eps = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_eps'
        verbose_name_plural = 'Eps'

    def __str__(self):
        return str(self.nombre_eps)
    
class TipoSexo(models.Model):
    id_tsexo = models.SmallAutoField(primary_key=True)
    nombre_tsexo = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_tiposexo'
        verbose_name_plural = 'Tipo de sexo'

    def __str__(self):
        return str(self.nombre_tsexo)
   
class TipoOrientacionSexual(models.Model):
    id_torientacion = models.SmallAutoField(primary_key=True)
    nombre_torientacion = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_tipoorientacion'
        verbose_name_plural = 'Tipo de orientación sexual'

    def __str__(self):
        return str(self.nombre_torientacion)

class TipoRangoEtario(models.Model):
    id_tretario = models.SmallAutoField(primary_key=True)
    nombre_tretario = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_tiporetario'
        verbose_name_plural = 'Tipos de rangos etarios'

    def __str__(self):
        return str(self.nombre_tretario)
    
class TipoFactorDiferencial(models.Model):
    id_tfdiferencial = models.SmallAutoField(primary_key=True)
    nombre_tfdiferencial = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_tipofdiferencial'
        verbose_name_plural = 'Tipo de factor diferencial'

    def __str__(self):
        return str(self.nombre_tfdiferencial)

class TipoIdentificacionColectivo(models.Model):
    id_ticolectivo = models.SmallAutoField(primary_key=True)
    nombre_ticolectivo = models.CharField(max_length=100)

    class Meta:
        db_table = 'eco_bas_ticolectivo'
        verbose_name_plural = 'Tipo de identificacion de colectivos'

    def __str__(self):
        return str(self.id_ticolectivo)



# MODELOS PARA LAS TABLAS DINÁMICAS QUE SON TRASVERSALES A TODO EL SISTEMA

class DatosUbicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    pais = models.ForeignKey(Pais, to_field='id_pais', on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, to_field='id_departamento', on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, to_field='id_municipio', on_delete=models.CASCADE)
    zona = models.ForeignKey(ZonaUbicacion, to_field='id_zubicacion', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=160, blank=True, null=True)
    indicacion = models.CharField(max_length=160, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'eco_sis_ubicacion'
        verbose_name_plural = 'Datos de ubicación'

    def __str__(self):
        return str(self.id_ubicacion)

class UbicacionRural(DatosUbicacion):
    corregimiento = models.CharField(max_length=150, null=True, blank=True)
    centro_poblado = models.CharField(max_length=150, null=True, blank=True)
    vereda = models.CharField(max_length=150, null=True, blank=True)
    
    def __str__(self):
        return self.direccion
    
    class Meta:
        db_table = 'eco_sis_direccionrural'
        verbose_name_plural = 'Dirección rural'

class direccionUrbana(DatosUbicacion):
    nombre_barrio = models.CharField(max_length=100, null=True, blank=True)
    tipo_viaprincipal = models.CharField(max_length=20, null=True, blank=True)
    numero_viaprincipal = models.IntegerField(null=True, blank=True)
    letra_principal = models.CharField(max_length=10, null=True, blank=True)
    es_bis = models.BooleanField(null=True)
    cuadrante_principal = models.CharField(max_length=10, null=True, blank=True)
    numero_viasecundaria = models.IntegerField(null=True, blank=True)
    letra_secundaria = models.CharField(max_length=10, null=True, blank=True)
    cuadrante_secundario = models.CharField(max_length=10, null=True, blank=True)
    numero_placa = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        fields = [
            self.tipo_viaprincipal, self.numero_viaprincipal, self.letra_principal,
            self.cuadrante_principal, self.numero_viasecundaria, self.letra_secundaria, self.numero_placa,
            self.cuadrante_secundario, self.complemento]
        
        fields = [str(field) for field in fields if field]
        return " ".join(fields)
    
    class Meta:
        db_table = 'eco_sis_direccionurbana'
        verbose_name_plural = 'Dirección urbana'

# class GeoUrbana(geo_models.Model):
#     id_geourbana = geo_models.AutoField(primary_key=True)
#     ubicacion = geo_models.ForeignKey(DatosUbicacion, to_field='id_ubicacion', on_delete=geo_models.CASCADE, blank=True, null=True)
#     geom = geo_models.PointField(srid=4326, blank=True, null=True)

#     class Meta:
#         db_table = 'eco_geo_urbana'
#         verbose_name_plural = 'Geolocalización urbana'

#     def __str__(self):
#         return str(self.id_geourbana)
    
class TelefonoCelularContacto(models.Model):
    id_ctelefono = models.SmallAutoField(primary_key=True)
    celular_uno = models.CharField(max_length=15, blank=True, null=True)
    celular_dos = models.CharField(max_length=15, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'eco_sis_ctelefono'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_ctelefono)
    
class CorreoElectronicoContacto(models.Model):
    id_ccelectronico = models.SmallAutoField(primary_key=True)
    correo_electronico = models.EmailField(max_length=100)
    autoriza_envio = models.BooleanField(default=False)

    class Meta:
        db_table = 'eco_sis_ccelectronico'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_ccelectronico)
    
class DatosContacto(models.Model):
    id_contacto = models.SmallAutoField(primary_key=True)
    id_ctelefono = models.ForeignKey(TelefonoCelularContacto, to_field='id_ctelefono', on_delete=models.CASCADE)
    id_ccelectronico = models.ForeignKey(CorreoElectronicoContacto, to_field='id_ccelectronico', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'eco_sis_contacto'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_contacto)
    
class IdentificacionPersona(models.Model):
    id_ipersona = models.AutoField(primary_key=True)
    numero_identificacion = models.CharField(max_length=20, null=False, blank=True)
    fecha_expedicion = models.DateField()
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, to_field='id_tidentificacion', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sis_ipersona'
        verbose_name_plural = 'Datos de la identificación de la persona'

    def __str__(self):
        return str(self.numero_identificacion) + str(self.fecha_expedicion)

class FileDocumentoIdentidad(models.Model):
    id_fdocumento = models.AutoField(primary_key=True)
    file_documento = models.FileField(upload_to= 'documento_identidad/', null=True, blank=True)
    id_ipersona = models.ForeignKey(IdentificacionPersona, to_field='id_ipersona', on_delete=models.CASCADE)
    class Meta:
        db_table = 'eco_doc_fdidentidad'
        verbose_name_plural = 'Archivo del documento de identidad'
    def __str__(self):
        return str(self.id_fdocumento)

class NombrePersona(models.Model):
    id_npersona = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=20, null=False, blank=False)
    segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
    primer_apellido = models.CharField(max_length=50, null=False, blank=False)
    segundo_apellido = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'eco_sis_nombrepersona'
        verbose_name_plural = 'Nombres y apellidos de las personas'

    def __str__(self):
        return str(self.id_npersona) + str(self.primer_nombre)
    
class DatosBasicosPersona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre_persona = models.ForeignKey(NombrePersona, to_field='id_npersona', on_delete=models.CASCADE)
    identificacion_persona = models.ForeignKey(IdentificacionPersona, to_field='id_ipersona', on_delete=models.CASCADE)
    genero_persona = models.ForeignKey(TipoGenero, to_field='id_tgenero', on_delete=models.CASCADE, null=True)
    ubicacion_persona = GenericRelation(DatosUbicacion)
    contacto_persona = GenericRelation(DatosContacto)

    class Meta:
        db_table = 'eco_sis_basicospersona'
        verbose_name_plural = 'Datos básicos de la persona'

    def __str__(self):
        return str(self.id_persona)

class LugarNacimientoPersona(models.Model):
    id_lnacimiento = models.AutoField(primary_key=True);
    pais = models.ForeignKey(Pais, to_field='id_pais', on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, to_field='id_departamento', on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, to_field='id_municipio', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sis_lnpersona'
        verbose_name_plural = 'Lugar de nacimiento de la persona'

    def __str__(self):
        return str(self.id_lnacimiento)

class FechaNacimientoPersona(models.Model):
    id_fnacimiento = models.AutoField(primary_key=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = 'eco_sis_fnpersona'
        verbose_name_plural = 'Fecha de nacimiento de la persona'

    def __str__(self):
        return str(self.id_fnacimiento)

class DatosNacimientoPersona(models.Model):
    id_dnacimiento = models.AutoField(primary_key=True)
    Lugar_npersona = models.ForeignKey(LugarNacimientoPersona, to_field='id_lnacimiento', on_delete=models.CASCADE, null=True, blank=True)
    fecha_npersona = models.ForeignKey(FechaNacimientoPersona, to_field='id_fnacimiento', on_delete=models.CASCADE, null=True, blank=True)
    persona = models.ForeignKey(DatosBasicosPersona, to_field='id_persona', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'eco_sis_dnpersona'
        verbose_name_plural = 'Datos de nacimiento de la persona'

    def __str__(self):
        return str(self.id_dnacimiento)
    
class DatosComplemetariosPersona(models.Model):
    id_complementarios = models.SmallAutoField(primary_key=True)
    sexo = models.ForeignKey(TipoSexo, to_field='id_tsexo', on_delete=models.CASCADE)
    orientacion_sexual = models.ForeignKey(TipoOrientacionSexual, to_field='id_torientacion', on_delete=models.CASCADE)
    rango_etario = models.ForeignKey(TipoRangoEtario, to_field='id_tretario', on_delete=models.CASCADE)
    factor_diferencial = models.ForeignKey(TipoFactorDiferencial, to_field='id_tfdiferencial', on_delete=models.CASCADE)
    tiene_discapacidad = models.BooleanField(default=False)
    pertenece_getnico = models.BooleanField(default=False)
    pertenece_organizacion = models.BooleanField(default=False)
    tiene_mcautelar = models.BooleanField(default=False)
    registra_tercero = models.BooleanField(default=False)
    persona = models.ForeignKey(DatosBasicosPersona, to_field='id_persona', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sis_cpersona'
        verbose_name_plural = 'Datos complementarios de la persona'

    def __str__(self):
        return str(self.id_complementarios)
    
class NombreRepresentanteLegalMenor(models.Model):
    id_nrepresentante = models.AutoField(primary_key=True)
    primer_nrepresentante = models.CharField(max_length=50, null=False, blank=False)
    segundo_nrepresentante = models.CharField(max_length=50, null=True, blank=True)
    primer_arepresentante = models.CharField(max_length=50, null=False, blank=False)
    segundo_arepresentante = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'eco_sis_nrepresentante'
        verbose_name_plural = 'Nombres y apellidos del representante legal'

    def __str__(self):
        return str(self.id_nrepresentante)

class IdentificacionRepresentanteLegalMenor(models.Model):
    id_irepresentante = models.AutoField(primary_key=True)
    numero_irepresentante = models.CharField(max_length=20, null=False, blank=True)
    fecha_exrepresentante = models.DateField()
    tipo_irepresentante = models.ForeignKey(TipoIdentificacion, to_field='id_tidentificacion', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sis_rrepresentante'
        verbose_name_plural = 'Datos de la identificación del representante legal'

    def __str__(self):
        return str(self.id_irepresentante)
    
class DatosRepresentanteLegalMenor(models.Model):
    id_rrepresentante = models.AutoField(primary_key=True)
    nombre_rrepresentante = models.ForeignKey(NombreRepresentanteLegalMenor, to_field='id_nrepresentante', on_delete=models.CASCADE)
    identificacion_rrepresentante = models.ForeignKey(IdentificacionRepresentanteLegalMenor, to_field='id_irepresentante', on_delete=models.CASCADE)
    persona = models.ForeignKey(DatosBasicosPersona, to_field='id_persona', on_delete=models.CASCADE, null=True, blank=True)   
    contacto_rrepresentante = GenericRelation(DatosContacto)

    class Meta:
        db_table = 'eco_sis_representantelegal'
        verbose_name_plural = 'Datos del representante legal'

    def __str__(self):
        return str(self.id_rrepresentante)
    

class NombreColectivo(models.Model):
    id_ncolectivo = models.AutoField(primary_key=True)
    nombre_colectivo = models.CharField(max_length=200, blank=True, null=True)
    # registro = GenericRelation(Registro)

    class Meta:
        db_table = 'eco_sis_ncolectivo'
        verbose_name_plural = 'Tipos de colectivos'

    def __str__(self):
        return str(self.id_ncolectivo)
        
class DatosbasicosColectivos(models.Model):
    id_bcolectivos = models.AutoField(primary_key=True)
    nombre_colectivo = models.ForeignKey(NombreColectivo, to_field='id_ncolectivo', on_delete=models.CASCADE)
    ubicacion_colectivo = GenericRelation(DatosUbicacion)
    contacto_colectivo = GenericRelation(DatosContacto)

    class Meta:
        db_table = 'eco_sis_dbcolectivo'
        verbose_name_plural = 'Datos básicos del id_bcolectivos'

    def __str__(self):
        return str(self.id_bcolectivos)
    
class IdentificacionColectivo(models.Model):
    id_icolectivo = models.AutoField(primary_key=True)
    tipo_icolectivo = models.ForeignKey(TipoIdentificacionColectivo, to_field='id_ticolectivo', on_delete=models.CASCADE)
    numero_icolectivo = models.CharField(max_length=20, blank=True, null=True)
    colectivo = models.ForeignKey(DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sis_icolectivo'
        verbose_name_plural = 'Identificacion del colectivo'
        
    def __str__(self):
        return str(self.id_icolectivo)

class InformaciónColectivoFactorDiferencial(models.Model):
    id_icfdiferencial = models.AutoField(primary_key=True)
    tiene_pdiscapacidad = models.BooleanField(default=False, null=True, blank=True)
    tiene_pindigenas = models.BooleanField(default=False, null=True, blank=True)
    tiene_pafrocolombiano = models.BooleanField(default=False, null=True, blank=True)
    tiene_pnegro = models.BooleanField(default=False, null=True, blank=True)
    tiene_praizal = models.BooleanField(default=False, null=True, blank=True)
    tiene_ppalenquero = models.BooleanField(default=False, null=True, blank=True)
    tiene_prongitano = models.BooleanField(default=False, null=True, blank=True)
    colectivo = models.ForeignKey(DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sis_icfdiferencial'
        verbose_name_plural = 'Información del colectivo factor diferencial'

    def __str__(self):
        return str(self.id_icfdiferencial)
    
class cantidadGenero(models.Model):
    id_cgenero = models.AutoField(primary_key=True)
    cantidad_femenino = models.SmallIntegerField(default=0, null=True, blank=True)
    cantidad_masculino = models.SmallIntegerField(default=0, null=True, blank=True)
    cantidad_nobinario = models.SmallIntegerField(default=0, null=True, blank=True)
    colectivo = models.ForeignKey(DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sis_cgenero'
        verbose_name_plural = 'Cantidad de personas por generos del colectivo'
        
    def __str__(self):
        return str(self.id_cgenero)
    
class cantidadSexo(models.Model):
    id_csexo = models.AutoField(primary_key=True)
    cantidad_mujer = models.SmallIntegerField(default=0, null=True, blank=True)
    cantidad_hombre = models.SmallIntegerField(default=0, null=True, blank=True)
    cantidad_intersexual = models.SmallIntegerField(default=0, null=True, blank=True)
    colectivo = models.ForeignKey(DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sis_csexo'
        verbose_name_plural = 'Cantidad de personas por generos del colectivo'
        
    def __str__(self):
        return str(self.id_csexo)
    
class TotalIntegrantes(models.Model):
    id_tintegrantes = models.AutoField(primary_key=True)
    total_integrantes = models.SmallIntegerField(default=0, null=True, blank=True)
    colectivo = models.ForeignKey(DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_sis_tintegrantes'
        verbose_name_plural = 'Cantidad aproximada de integrantes del colectivo'
        
    def __str__(self):
        return str(self.id_tintegrantes)
    
class NombreApellidoPersonaColectivo(models.Model):
    id_napcolectivo = models.AutoField(primary_key=True)
    primer_npcolectivo = models.CharField(max_length=20, null=False, blank=False)
    segundo_npcolectivo = models.CharField(max_length=50, null=True, blank=True)
    primer_apcolectivo = models.CharField(max_length=50, null=False, blank=False)
    segundo_apcolectivo = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'eco_sis_napcolectivo'
        verbose_name_plural = 'Nombres y apellidos de las personas del colectivo'

    def __str__(self):
        return str(self.id_napcolectivo)
    
class IdentificacionPersonaColectivo(models.Model):
    id_ipcolectivo = models.AutoField(primary_key=True)
    numero_ipcolectivo = models.CharField(max_length=20, null=False, blank=True)
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, to_field='id_tidentificacion', on_delete=models.CASCADE)
    fecha_expedicion = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'eco_sis_ipcolectivo'
        verbose_name_plural = 'Datos de la identificación de la persona del colectivo'

    def __str__(self):
        return str(self.id_ipcolectivo) + str(self.numero_ipcolectivo)
    
class PersonaColectivo(models.Model):
    id_pcolectivo = models.AutoField(primary_key=True)
    nombre_pcolectivo = models.ForeignKey(NombreApellidoPersonaColectivo, to_field='id_napcolectivo', on_delete=models.CASCADE)
    es_representante = models.BooleanField(default=False)
    esta_activo = models.BooleanField(default=True)
    colectivo = models.ForeignKey(DatosbasicosColectivos, to_field='id_bcolectivos', on_delete=models.CASCADE)
    contacto_pcolectivo = GenericRelation(DatosContacto)

    class Meta:
        db_table = 'eco_sis_pcolectivo'
        verbose_name_plural = 'Datos personales de las personas del colectivo'

    def __str__(self):
        return str(self.id_pcolectivo)

class PersonaColectivoRepresentante(PersonaColectivo):
    sexo_pcolectivo = models.ForeignKey(TipoSexo, to_field='id_tsexo', on_delete=models.CASCADE, null=True)
    ubicacion_pcolectivo = GenericRelation(DatosUbicacion)
    identificacion_pcolectivo = models.ForeignKey(IdentificacionPersonaColectivo, to_field='id_ipcolectivo', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'eco_sis_prcolectivo'
        verbose_name_plural = 'Datos personales del representante del colectivo'

    def __str__(self):
        return str(self.id_pcolectivo)