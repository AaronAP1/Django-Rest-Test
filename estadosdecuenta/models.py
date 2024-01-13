from django.db import models

# Create your models here.
class DataConsolidado(models.Model):
    ID_DATOS = models.CharField(primary_key=True, db_column='IDDATOS')
    ITEM = models.IntegerField()
    CODIGO_DE_PAGO = models.CharField(unique=True, null=True, db_column='CÓDIGO DE PAGO')
    MZLTS = models.CharField(null=True)
    CAPTACION = models.DateField(null=True)
    ASESOR = models.TextField(null=True)
    APELLIDO_PATERNO = models.TextField(null=True, db_column='APELLIDO PATERNO')
    APELLIDO_MATERNO = models.TextField(null=True, db_column='APELLIDO MATERNO')
    NOMBRES = models.TextField(null=True)
    DOC = models.CharField( null=True)
    NUMERO = models.CharField( null=True,db_column='NÚMERO')
    DIRECCION = models.CharField(null=True,db_column='DIRECCIÓN') 
    DISTRITO = models.TextField(null=True)
    PROVINCIA = models.TextField(null=True)
    DEPARTAMENTO = models.TextField(null=True)
    CELULAR = models.CharField( null=True)
    EMAIL = models.CharField(null=True)
    M2 = models.CharField(null=True)
    UBICACION = models.TextField(null=True, db_column='UBICACIÓN')
    PRECIOVENTA = models.CharField(null=True)
    INICIAL = models.CharField(null=True)
    SALDO = models.CharField(null=True)
    CUOTAS = models.IntegerField(null=True)
    CUOTA = models.CharField(null=True)
    INICIOPAGO = models.DateField(null=True)
    CVENCIDAS = models.IntegerField(null=True)
    CPAGADAS = models.IntegerField(null=True)
    SVENCIDOS = models.CharField(null=True)
    SPAGADOS = models.CharField(null=True)
    COMENTARIO = models.TextField(null=True)

  
    

class Cobros(models.Model):
    ID_COBROS = models.CharField(primary_key=True)
    CODIGO_INTEGRANTE = models.CharField(null=True)
    NUMERO_DE_RECIBO = models.CharField()
    APELLIDO_PATERNO = models.TextField( null=True)
    APELLIDO_MATERNO = models.TextField( null=True)
    NOMBRES = models.TextField( null=True)
    CODIGO_DE_GRUPO_INTEGRANTES = models.CharField( null=True)
    FECHA_EMICION_RECIBO = models.DateTimeField(auto_now_add=True)
    FECHA_VENCIMIENTO_RECIBO = models.DateField()
    MONEDA_A_PAGAR = models.CharField( null=True)
    CODIGO_REFERENCIA_CLIENTE = models.CharField(null=True)
    DESCRIPCION_COBRO_REALIZAR = models.TextField(null=True)
    OBSERVACIONES_RECIBO = models.TextField( null=True)
    INDICADOR_COBRO_MORA = models.CharField( null=True)
    CODIGO_CONCEPTO_1 = models.CharField(null=True)
    IMPORTE_COBRO_CONCEPTO_1 = models.CharField(null=True)


    

class Recaudaciones(models.Model):
    ID_RECAUDACIONES = models.CharField(primary_key=True)
    CODIGO_INTEGRANTE = models.CharField(null=True)
    NUMERO_DE_RECIBO = models.CharField(null=True)
    APELLIDOS_NOMBRES = models.TextField(null=True)
    GRUPO = models.CharField(null=True)
    DESCRIPCION_RECIBO = models.CharField(null=True)
    IMP_RECIBO = models.CharField(null=True)
    FECHA_VENCIMIENTO = models.DateField(null=True)
    DIA_MORA = models.IntegerField(null=True)
    IMP_MORA = models.CharField(null=True)
    IMP_TOTAL = models.CharField(null=True)
    FECHA_PAGO = models.DateField(null=True)
    MZLTE = models.CharField(null=True)
    FORMA_PAGO = models.TextField(null=True)
    CALC_MORA = models.CharField(null=True)
    FECHA_ACTUALIZADA = models.DateField(null=True)



class Resumen(models.Model):
    ID_RESUMEN = models.CharField(primary_key=True, max_length=10) 
    ID_INTEGRANTE = models.CharField()
    FECHA_RESUMEN = models.DateField()
    CVENCIDAS = models.IntegerField()
    CPAGADAS = models.IntegerField()
    SVENCIDOS = models.CharField()
    SPAGADOS = models.CharField()
