
from rest_framework import viewsets
from sistema import models as sis_models
from sistema import serializer_get as sisg_serializer
from sistema import serializer_post as sisp_serializer


#  MSIS'numero' => (Modelos de la aplicación 'sistema')  + Número del modelo
#  SPSIS'numero' => (Serializador post de la aplicación 'sistema) + Número de la serialización
#  SGSIS'numero' => (Serializador get de la aplicación 'sistema) + Número de la serialización


#1 MSIS'1' SGSIS'1'
class PaisPermiso(viewsets.ModelViewSet):                                   
    queryset = sis_models.Pais.objects.all().order_by('id_pais')            
    serializer_class = sisg_serializer.ApiPais                                
    http_method_names = ['get']

#2 MSIS'2' SGSIS'2'
class DepartamentoPermiso(viewsets.ModelViewSet):
    serializer_class = sisg_serializer.ApiDepartamento
    http_method_names = ['get']

    def get_queryset(self):
        queryset = sis_models.Departamento.objects.all()
        pais = self.request.query_params.get('pais', None)

        if pais is not None:
            if pais == '1':
                pais = int(pais)
                queryset = queryset.filter(pais_id=pais)
            else:
                queryset = queryset.filter(pais=24)

        return queryset

#3 MSIS'3' SGSIS'3'    
class MunicipioPermiso(viewsets.ModelViewSet):
    serializer_class = sisg_serializer.ApiMunicipio
    http_method_names = ['get']

    def get_queryset(self):
        queryset = sis_models.Municipio.objects.all()
        departamento = self.request.query_params.get('departamento', None)
        if departamento is not None:
            queryset = queryset.filter(departamento=departamento)
        return queryset

#4 MSIS'4' SGSIS'4'   
class ZonaPermiso(viewsets.ModelViewSet):
    queryset = sis_models.ZonaUbicacion.objects.all()
    serializer_class = sisg_serializer.ApiZona
    http_method_names = ['get']

#5 MSIS'5' SGSIS'5'
class TipoIdentificacionPermiso(viewsets.ModelViewSet):
    queryset = sis_models.TipoIdentificacion.objects.all()
    serializer_class = sisg_serializer.ApiTipoIdentificacion
    http_method_names = ['get']

#6 MSIS'6' SGSIS'6'
class TipoGeneroPermiso(viewsets.ModelViewSet):
    queryset = sis_models.TipoGenero.objects.all()
    serializer_class = sisg_serializer.ApiTipoGenero
    http_method_names = ['get']

#7 MSIS'7' SGSIS'7'
class EstadoCivilPermiso(viewsets.ModelViewSet):
    queryset = sis_models.EstadoCivil.objects.all()
    serializer_class = sisg_serializer.ApiEstadoCivil
    http_method_names = ['get']

#8 MSIS'8' SGSIS'8'
class GpRhPermiso(viewsets.ModelViewSet):
    queryset = sis_models.GpRh.objects.all()
    serializer_class = sisg_serializer.ApiGpRh
    http_method_names = ['get']

#9 MSIS'9' SGSIS'9'
class FondoPensionesPermiso(viewsets.ModelViewSet):
    queryset = sis_models.FondoPensiones.objects.all()
    serializer_class = sisg_serializer.ApiFondoPensiones
    http_method_names = ['get']

#10 MSIS'10' SGSIS'10'
class EpsPermiso(viewsets.ModelViewSet):
    queryset = sis_models.Eps.objects.all()
    serializer_class = sisg_serializer.ApiEps
    http_method_names = ['get']

#11 MSIS'11' SGSIS'11'
class TipoSexoPermiso(viewsets.ModelViewSet):
    queryset = sis_models.TipoSexo.objects.all()
    serializer_class = sisg_serializer.apiTipoSexo
    http_method_names = ['get']

#12 MSIS'12' SGSIS'12'
class TipoOrientacionSexualPermiso(viewsets.ModelViewSet):
    queryset = sis_models.TipoOrientacionSexual.objects.all()
    serializer_class = sisg_serializer.apiTipoOrientacionSexual
    http_method_names = ['get']

#13 MSIS'13' SGSIS'13'
class TipoRangoEtarioPermiso(viewsets.ModelViewSet):
    queryset = sis_models.TipoRangoEtario.objects.all()
    serializer_class = sisg_serializer.apiTipoRangoEtario
    http_method_names = ['get']

#14 MSIS'14' SGSIS'14'
class TipoFactorDiferencialPermiso(viewsets.ModelViewSet):
    queryset = sis_models.TipoFactorDiferencial.objects.all()
    serializer_class = sisg_serializer.apiTipoFactorDiferencial
    http_method_names = ['get']

#15 MSIS'15' SGSIS'15'
class TipoIdentificacionColectivoPermiso(viewsets.ModelViewSet):
    queryset = sis_models.TipoIdentificacionColectivo.objects.all()
    serializer_class = sisg_serializer.apiTipoIdentificacionColectivo
    http_method_names = ['get']



#16 MSIS'16' SPSIS'1'
class DatosUbicacionPermiso(viewsets.ModelViewSet):
    queryset = sis_models.DatosUbicacion.objects.all()
    serializer_class = sisp_serializer.apiDatosUbicacion
    http_method_names = ['post','put']

#17 MSIS'17' SPSIS'2'
class UbicacionRuralPermiso(viewsets.ModelViewSet):
    queryset = sis_models.UbicacionRural.objects.all()
    serializer_class = sisp_serializer.apiUbicacionRural
    http_method_names = ['post','put']

#18 MSIS'18' SPSIS'3'
class UbicacionUrbanaPermiso(viewsets.ModelViewSet):
    queryset = sis_models.UbicacionUrbana.objects.all()
    serializer_class = sisp_serializer.apiUbicacionUrbana
    http_method_names = ['post','put']

#19 MSIS'20' SPSIS'4'
class TelefonoCelularContactoPermiso(viewsets.ModelViewSet):
    queryset = sis_models.TelefonoCelularContacto.objects.all()
    serializer_class = sisp_serializer.apiTelefonoCelularContacto
    http_method_names = ['post','put']

#20 MSIS'21' SPSIS'5'
class CorreoElectronicoContactoPermiso(viewsets.ModelViewSet):
    queryset = sis_models.CorreoElectronicoContacto.objects.all()
    serializer_class = sisp_serializer.apiCorreoElectronicoContacto
    http_method_names = ['post','put']

#21 MSIS'22' SPSIS'6'
class DatosContactoPermiso(viewsets.ModelViewSet):
    queryset = sis_models.DatosContacto.objects.all()
    serializer_class = sisp_serializer.apiDatosContacto
    http_method_names = ['post','put']

#22 MSIS'23' SPSIS'7'
class IdentificacionPersonaPermiso(viewsets.ModelViewSet):
    queryset = sis_models.IdentificacionPersona.objects.all()
    serializer_class = sisp_serializer.apiIdentificacionPersona
    http_method_names = ['post','put']

#23 MSIS'24' SPSIS'8'
class FileDocumentoIdentidadPermiso(viewsets.ModelViewSet):
    queryset = sis_models.FileDocumentoIdentidad.objects.all()
    serializer_class = sisp_serializer.apiFileDocumentoIdentidad
    http_method_names = ['post','put']

#24 MSIS'25' SPSIS'9'
class NombrePersonaPermiso(viewsets.ModelViewSet):
    queryset = sis_models.NombrePersona.objects.all()
    serializer_class = sisp_serializer.apiNombrePersona
    http_method_names = ['post','put']

#25 MSIS'26' SPSIS'10'
class DatosBasicosPersonaPermiso(viewsets.ModelViewSet):
    queryset = sis_models.DatosBasicosPersona.objects.all()
    serializer_class = sisp_serializer.apiDatosBasicosPersona
    http_method_names = ['post','put']

#26 MSIS'27' SPSIS'11'
class LugarNacimientoPersonaPermiso(viewsets.ModelViewSet):
    queryset = sis_models.LugarNacimientoPersona.objects.all()
    serializer_class = sisp_serializer.apiLugarNacimientoPersona
    http_method_names = ['post','put']

#27 MSIS'28' SPSIS'12'
class FechaNacimientoPersonaPermiso(viewsets.ModelViewSet):
    queryset = sis_models.FechaNacimientoPersona.objects.all()
    serializer_class = sisp_serializer.apiFechaNacimientoPersona
    http_method_names = ['post','put']

#28 MSIS'29' SPSIS'13'
class DatosNacimientoPersonaPermiso(viewsets.ModelViewSet):
    queryset = sis_models.DatosNacimientoPersona.objects.all()
    serializer_class = sisp_serializer.apiDatosNacimientoPersona
    http_method_names = ['post','put']

#29 MSIS'30' SPSIS'14'
class DatosComplemetariosPersonaPermiso(viewsets.ModelViewSet):
    queryset = sis_models.DatosComplemetariosPersona.objects.all()
    serializer_class = sisp_serializer.apiDatosComplemetariosPersona
    http_method_names = ['post','put']

#30 MSIS'31' SPSIS'15'
class NombreRepresentanteLegalMenorPermiso(viewsets.ModelViewSet):
    queryset = sis_models.NombreRepresentanteLegalMenor.objects.all()
    serializer_class = sisp_serializer.apiNombreRepresentanteLegalMenor
    http_method_names = ['post','put']

#31 MSIS'32' SPSIS'16'
class IdentificacionRepresentantePermiso(viewsets.ModelViewSet):
    queryset = sis_models.IdentificacionRepresentante.objects.all()
    serializer_class = sisp_serializer.apiIdentificacionRepresentante
    http_method_names = ['post','put']

#32 MSIS'33' SPSIS'17'
class DatosRepresentanteLegalPermiso(viewsets.ModelViewSet):
    queryset = sis_models.DatosRepresentanteLegal.objects.all()
    serializer_class = sisp_serializer.apiDatosRepresentanteLegal
    http_method_names = ['post','put']

#33 MSIS'34' SPSIS'18'
class NombreColectivoPermiso(viewsets.ModelViewSet):
    queryset = sis_models.NombreColectivo.objects.all()
    serializer_class = sisp_serializer.apiNombreColectivo
    http_method_names = ['post','put']

#34 MSIS'35' SPSIS'19'
class DatosbasicosColectivosPermiso(viewsets.ModelViewSet):
    queryset = sis_models.DatosbasicosColectivos.objects.all()
    serializer_class = sisp_serializer.apiDatosbasicosColectivos
    http_method_names = ['post','put']

#35 MSIS'36' SPSIS'20'
class IdentificacionColectivoPermiso(viewsets.ModelViewSet):
    queryset = sis_models.IdentificacionColectivo.objects.all()
    serializer_class = sisp_serializer.apiIdentificacionColectivo
    http_method_names = ['post','put']

#36 MSIS'37' SPSIS'21'
class ColectivoFDiferencialPermiso(viewsets.ModelViewSet):
    queryset = sis_models.ColectivoFDiferencial.objects.all()
    serializer_class = sisp_serializer.apiColectivoFDiferencial
    http_method_names = ['post','put']

#37 MSIS'38' SPSIS'22'
class cantidadGeneroPermiso(viewsets.ModelViewSet):
    queryset = sis_models.cantidadGenero.objects.all()
    serializer_class = sisp_serializer.apicantidadGenero
    http_method_names = ['post','put']

#38 MSIS'39' SPSIS'23'
class cantidadSexoPermiso(viewsets.ModelViewSet):
    queryset = sis_models.cantidadSexo.objects.all()
    serializer_class = sisp_serializer.apicantidadSexo
    http_method_names = ['post','put']

#39 MSIS'40' SPSIS'24'
class TotalIntegrantesPermiso(viewsets.ModelViewSet):
    queryset = sis_models.TotalIntegrantes.objects.all()
    serializer_class = sisp_serializer.apiTotalIntegrantes
    http_method_names = ['post','put']

#40 MSIS'41' SPSIS'25'
class NombrePersonaColectivoPermiso(viewsets.ModelViewSet):
    queryset = sis_models.NombrePersonaColectivo.objects.all()
    serializer_class = sisp_serializer.apiNombrePersonaColectivo
    http_method_names = ['post','put']

#41 MSIS'42' SPSIS'26'
class IdentificacionPersonaColectivoPermiso(viewsets.ModelViewSet):
    queryset = sis_models.IdentificacionPersonaColectivo.objects.all()
    serializer_class = sisp_serializer.apiIdentificacionPersonaColectivo
    http_method_names = ['post','put']

#42 MSIS'43' SPSIS'27'
class PersonaColectivoPermiso(viewsets.ModelViewSet):
    queryset = sis_models.PersonaColectivo.objects.all()
    serializer_class = sisp_serializer.apiPersonaColectivo
    http_method_names = ['post','put']

#43 MSIS'44' SPSIS'28
class PersonaColectivoRepresentantePermiso(viewsets.ModelViewSet):
    queryset = sis_models.PersonaColectivoRepresentante.objects.all()
    serializer_class = sisp_serializer.apiPersonaColectivoRepresentante
    http_method_names = ['post','put']