# Generated by Django 5.1.2 on 2024-10-17 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('gsc', '0002_initial'),
        ('registro', '0001_initial'),
        ('sistema', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='lugardiligenciamientoformulario',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.departamento'),
        ),
        migrations.AddField(
            model_name='lugardiligenciamientoformulario',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.municipio'),
        ),
        migrations.AddField(
            model_name='lugardiligenciamientoformulario',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.pais'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='lugar_diligenciamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.lugardiligenciamientoformulario'),
        ),
        migrations.AddField(
            model_name='registro',
            name='canal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.canalsolicitud'),
        ),
        migrations.AddField(
            model_name='registro',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.estadoespecifico'),
        ),
        migrations.AddField(
            model_name='registro',
            name='objects_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='registrollamadas',
            name='registro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.registro'),
        ),
        migrations.AddField(
            model_name='registrollamadas',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mediocontactollamada',
            name='registro_llamada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.registrollamadas'),
        ),
        migrations.AddField(
            model_name='informacionllamada',
            name='registro_llamada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.registrollamadas'),
        ),
        migrations.AddField(
            model_name='fechahorallamada',
            name='registro_llamada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.registrollamadas'),
        ),
        migrations.AddField(
            model_name='entidadrespondellamada',
            name='registro_llamada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.registrollamadas'),
        ),
        migrations.AddField(
            model_name='tercerorespondellamada',
            name='registro_llamada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.registrollamadas'),
        ),
        migrations.AddField(
            model_name='informacionllamada',
            name='tipo_rllamada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.tiporesultadollamada'),
        ),
        migrations.AddField(
            model_name='registro',
            name='ruta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.tiporura'),
        ),
        migrations.AddField(
            model_name='trazabilidad',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trazabilidadgeneral',
            name='registro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.registro'),
        ),
        migrations.AddField(
            model_name='trazabilidad',
            name='Trazabilidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.trazabilidadgeneral'),
        ),
        migrations.AddField(
            model_name='ubicacionrespondellamada',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.departamento'),
        ),
        migrations.AddField(
            model_name='ubicacionrespondellamada',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.municipio'),
        ),
        migrations.AddField(
            model_name='ubicacionrespondellamada',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.pais'),
        ),
        migrations.AddField(
            model_name='ubicacionrespondellamada',
            name='registro_llamada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.registrollamadas'),
        ),
        migrations.AddField(
            model_name='respondeurbanallamada',
            name='ubicacion_responde',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.ubicacionrespondellamada'),
        ),
        migrations.AddField(
            model_name='responderuralllamada',
            name='ubicacion_responde',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.ubicacionrespondellamada'),
        ),
        migrations.AddField(
            model_name='formulariocolectivo',
            name='colectivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.datosbasicoscolectivos'),
        ),
        migrations.AddField(
            model_name='formulariocolectivo',
            name='consentimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsc.consentimientocolectivo'),
        ),
        migrations.AddField(
            model_name='formulariocolectivo',
            name='factor_diferencial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.informacióncolectivofactordiferencial'),
        ),
        migrations.AddField(
            model_name='formulariocolectivo',
            name='hecho_victimizante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsc.hechovictimizantecolectivo'),
        ),
        migrations.AddField(
            model_name='formulariocolectivo',
            name='id_representante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.personacolectivo'),
        ),
        migrations.AddField(
            model_name='formulariocolectivo',
            name='medida_cautelar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsc.medidacautelarcolectivo'),
        ),
        migrations.AddField(
            model_name='formulariocolectivo',
            name='poblacion_colectivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsc.idpoblacioncolectivo'),
        ),
        migrations.AddField(
            model_name='formularioindividual',
            name='consentimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsc.consentimiento'),
        ),
        migrations.AddField(
            model_name='formularioindividual',
            name='cpersona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.datoscomplemetariospersona'),
        ),
        migrations.AddField(
            model_name='formularioindividual',
            name='ipoblacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsc.idpoblacion'),
        ),
        migrations.AddField(
            model_name='formularioindividual',
            name='iriesgo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsc.idriesgo'),
        ),
        migrations.AddField(
            model_name='formularioindividual',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.datosbasicospersona'),
        ),
    ]
