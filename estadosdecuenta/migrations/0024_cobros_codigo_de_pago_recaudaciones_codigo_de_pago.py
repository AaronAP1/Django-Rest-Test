# Generated by Django 5.0 on 2024-01-16 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadosdecuenta', '0023_alter_cobros_codigo_integrante_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cobros',
            name='CODIGO_DE_PAGO',
            field=models.ForeignKey(blank=True, db_column='CÓDIGO DE PAGO', null=True, on_delete=django.db.models.deletion.SET_NULL, to='estadosdecuenta.dataconsolidado'),
        ),
        migrations.AddField(
            model_name='recaudaciones',
            name='CODIGO_DE_PAGO',
            field=models.ForeignKey(blank=True, db_column='CÓDIGO DE PAGO', null=True, on_delete=django.db.models.deletion.SET_NULL, to='estadosdecuenta.dataconsolidado'),
        ),
    ]
