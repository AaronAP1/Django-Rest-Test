# Generated by Django 5.0 on 2024-01-13 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadosdecuenta', '0015_alter_recaudaciones_apellidos_nombres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recaudaciones',
            name='CODIGO_INTEGRANTE',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estadosdecuenta.dataconsolidado'),
        ),
    ]
