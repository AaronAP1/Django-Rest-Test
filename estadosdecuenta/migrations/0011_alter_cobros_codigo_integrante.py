# Generated by Django 5.0 on 2024-01-13 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadosdecuenta', '0010_rename_couta_dataconsolidado_cuota_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobros',
            name='CODIGO_INTEGRANTE',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
