# Generated by Django 5.0 on 2024-01-13 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estadosdecuenta', '0019_remove_cobros_codigo_integrante_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cobros',
            old_name='CODIGO_INTEGRANTE_ID',
            new_name='CODIGO_INTEGRANTE',
        ),
    ]