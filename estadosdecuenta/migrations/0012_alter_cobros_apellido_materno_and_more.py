# Generated by Django 5.0 on 2024-01-13 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadosdecuenta', '0011_alter_cobros_codigo_integrante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobros',
            name='APELLIDO_MATERNO',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='APELLIDO_PATERNO',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='CODIGO_CONCEPTO_1',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='CODIGO_DE_GRUPO_INTEGRANTES',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='CODIGO_INTEGRANTE',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='CODIGO_REFERENCIA_CLIENTE',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='DESCRIPCION_COBRO_REALIZAR',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='IMPORTE_COBRO_CONCEPTO_1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='INDICADOR_COBRO_MORA',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='MONEDA_A_PAGAR',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='NOMBRES',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cobros',
            name='OBSERVACIONES_RECIBO',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
