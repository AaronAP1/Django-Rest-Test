# Generated by Django 5.0 on 2024-01-11 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadosdecuenta', '0003_alter_dataconsolidado_celular_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataconsolidado',
            name='APELLIDO_MATERNO',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='APELLIDO_PATERNO',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='ASESOR',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='CELULAR',
            field=models.CharField(unique=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='COMENTARIO',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='COUTAS',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='DEPARTAMENTO',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='DIRECCION',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='DISTRITO',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='DOC',
            field=models.CharField(unique=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='EMAIL',
            field=models.CharField(unique=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='ID_DATOS',
            field=models.CharField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='M2',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='MZLTS',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='NOMBRES',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='NUMERO',
            field=models.CharField(unique=True),
        ),
        migrations.AlterField(
            model_name='dataconsolidado',
            name='PROVINCIA',
            field=models.TextField(),
        ),
    ]
