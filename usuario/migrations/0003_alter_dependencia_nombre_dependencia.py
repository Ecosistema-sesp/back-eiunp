# Generated by Django 5.1.2 on 2024-10-21 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_rename_direccionurbana_ubicacionurbana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependencia',
            name='nombre_dependencia',
            field=models.CharField(max_length=50),
        ),
    ]
