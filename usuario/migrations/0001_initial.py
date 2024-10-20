# Generated by Django 5.1.2 on 2024-10-17 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorreoElectronicoContactoUsuario',
            fields=[
                ('id_ccelectronico', models.SmallAutoField(primary_key=True, serialize=False)),
                ('correo_electronico', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Datos de contacto',
                'db_table': 'eco_usr_ccelectronico',
            },
        ),
        migrations.CreateModel(
            name='DatosUbicacionUsuario',
            fields=[
                ('id_ubicacion', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(blank=True, max_length=160, null=True)),
                ('indicacion', models.CharField(blank=True, max_length=160, null=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.departamento')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.municipio')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.pais')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.zonaubicacion')),
            ],
            options={
                'verbose_name_plural': 'Datos de ubicación',
                'db_table': 'eco_usr_ubicacion',
            },
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id_dependencia', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_dependencia', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Dependencia',
                'db_table': 'eco_bas_dependencia',
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id_grupo', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_grupo', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Grupo',
                'db_table': 'eco_bas_grupo',
            },
        ),
        migrations.CreateModel(
            name='NombrePersonaUsuario',
            fields=[
                ('id_npersona', models.AutoField(primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=20)),
                ('segundo_nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Nombres y apellidos de las personas',
                'db_table': 'eco_usr_nombrepersona',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Rol',
                'db_table': 'eco_bas_rol',
            },
        ),
        migrations.CreateModel(
            name='TelefonoCelularContactoUsuario',
            fields=[
                ('id_ctelefono', models.SmallAutoField(primary_key=True, serialize=False)),
                ('celular_uno', models.CharField(blank=True, max_length=15, null=True)),
                ('celular_dos', models.CharField(blank=True, max_length=15, null=True)),
                ('celular_emergencia', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name_plural': 'Datos de contacto',
                'db_table': 'eco_usr_ctelefono',
            },
        ),
        migrations.CreateModel(
            name='TipoVinculacion',
            fields=[
                ('id_tvinculacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tvinculacion', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tipo de vinculación a la UNP',
                'db_table': 'eco_bas_tipovinculacion',
            },
        ),
        migrations.CreateModel(
            name='DatosComplementariosUsuario',
            fields=[
                ('id_cusuario', models.AutoField(primary_key=True, serialize=False)),
                ('acepto_politicas', models.BooleanField(default=False)),
                ('eps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.eps')),
                ('estado_civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.estadocivil')),
                ('fondo_pensiones', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.fondopensiones')),
                ('tipo_vinculacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.tipovinculacion')),
            ],
            options={
                'verbose_name_plural': 'Datos básicos del usuario',
                'db_table': 'eco_usr_complementariosusuario',
            },
        ),
        migrations.CreateModel(
            name='ContratoContratista',
            fields=[
                ('id_contrato', models.AutoField(primary_key=True, serialize=False)),
                ('numero_contrato', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha_iniciocontrato', models.DateField(blank=True, null=True)),
                ('fecha_fincontrato', models.DateField(blank=True, null=True)),
                ('complementario_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.datoscomplementariosusuario')),
            ],
            options={
                'verbose_name_plural': 'Datos básicos del contrato',
                'db_table': 'eco_usr_datoscontrato',
            },
        ),
        migrations.CreateModel(
            name='direccionUrbana',
            fields=[
                ('datosubicacionusuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.datosubicacionusuario')),
                ('nombre_barrio', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_viaprincipal', models.CharField(blank=True, max_length=20, null=True)),
                ('numero_viaprincipal', models.IntegerField(blank=True, null=True)),
                ('letra_principal', models.CharField(blank=True, max_length=10, null=True)),
                ('es_bis', models.BooleanField(null=True)),
                ('cuadrante_principal', models.CharField(blank=True, max_length=10, null=True)),
                ('numero_viasecundaria', models.IntegerField(blank=True, null=True)),
                ('letra_secundaria', models.CharField(blank=True, max_length=10, null=True)),
                ('cuadrante_secundario', models.CharField(blank=True, max_length=10, null=True)),
                ('numero_placa', models.IntegerField(blank=True, null=True)),
                ('complemento', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name_plural': 'Dirección urbana',
                'db_table': 'eco_usr_direccionurbana',
            },
            bases=('usuario.datosubicacionusuario',),
        ),
        migrations.CreateModel(
            name='UbicacionRural',
            fields=[
                ('datosubicacionusuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.datosubicacionusuario')),
                ('corregimiento', models.CharField(blank=True, max_length=150, null=True)),
                ('centro_poblado', models.CharField(blank=True, max_length=150, null=True)),
                ('vereda', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'Dirección rural',
                'db_table': 'eco_usr_direccionrural',
            },
            bases=('usuario.datosubicacionusuario',),
        ),
        migrations.CreateModel(
            name='IdentificacionUsuario',
            fields=[
                ('id_iusuario', models.AutoField(primary_key=True, serialize=False)),
                ('numero_identificacion', models.CharField(blank=True, max_length=20)),
                ('fecha_expedicion', models.DateField()),
                ('tipo_identificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.tipoidentificacion')),
            ],
            options={
                'verbose_name_plural': 'Datos de la identificación del usuario',
                'db_table': 'eco_usr_iusuario',
            },
        ),
        migrations.CreateModel(
            name='DatosBasicosUsuario',
            fields=[
                ('id_busuario', models.AutoField(primary_key=True, serialize=False)),
                ('genero_persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.tipogenero')),
                ('gp_rh', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.gprh')),
                ('identificacion_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.identificacionusuario')),
                ('nombre_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.nombrepersonausuario')),
            ],
            options={
                'verbose_name_plural': 'Datos básicos del usuario',
                'db_table': 'eco_usr_basicosusuario',
            },
        ),
        migrations.CreateModel(
            name='ResolucionFuncionario',
            fields=[
                ('id_resolucion', models.AutoField(primary_key=True, serialize=False)),
                ('numero_resolucion', models.CharField(blank=True, max_length=30, null=True)),
                ('complementario_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.datoscomplementariosusuario')),
            ],
            options={
                'verbose_name_plural': 'Datos básicos de la resolucion del contratista',
                'db_table': 'eco_usr_datosresolucion',
            },
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id_pusuario', models.AutoField(primary_key=True, serialize=False)),
                ('basicos_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.datosbasicosusuario')),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.dependencia')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.grupo')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.rol')),
            ],
            options={
                'verbose_name_plural': 'perfil del usuario',
                'db_table': 'eco_usr_perfilusuario',
            },
        ),
        migrations.CreateModel(
            name='DatosContactoUsuario',
            fields=[
                ('id_contacto', models.SmallAutoField(primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('id_ccelectronico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.correoelectronicocontactousuario')),
                ('id_ctelefono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.telefonocelularcontactousuario')),
            ],
            options={
                'verbose_name_plural': 'Datos de contacto',
                'db_table': 'eco_usr_contacto',
            },
        ),
    ]
