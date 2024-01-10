from django.db import models

# Create your models here.
class DataConsolidado(models.Model):
    ID_DATOS = models.CharField(primary_key=True, max_length=10)
    ITEM = models.IntegerField(unique=True)
    CODIGO_DE_PAGO = models.IntegerField(unique=True)
    MZLTS = models.CharField(max_length=5)
    CAPTACION = models.DateField()
    ASESOR = models.TextField(max_length=200)
    APELLIDO_PATERNO = models.TextField(max_length=200)
    APELLIDO_MATERNO = models.TextField(max_length=200)
    NOMBRES = models.TextField(max_length=20)
    DOC = models.CharField(unique=True, max_length=4)
    NUMERO = models.CharField(unique=True, max_length=8)
    DIRECCION = models.CharField(max_length=100) 
    DISTRITO = models.TextField(max_length=100)
    PROVINCIA = models.TextField(max_length=100)
    DEPARTAMENTO = models.TextField(max_length=100)
    CELULAR= models.CharField(unique=True, max_length=12)
    EMAIL = models.CharField(unique=True, max_length=30)
    M2 = models.CharField(max_length=8)
    UBICACION = models.TextField()
    PRECIOVENTA = models.CharField()
    INICIAL = models.CharField()
    SALDO = models.CharField()
    COUTAS = models.IntegerField(max_length=2)
    COUTA = models.CharField()
    INICIO_PAGO = models.DateField()
    CVENCIDAS = models.IntegerField()
    CPAGADAS = models.IntegerField()
    SVENCIDOS = models.CharField()
    SPAGADOS = models.CharField()
    COMENTARIO = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.ID_DATOS} - {self.ITEM} - {self.CODIGO_DE_PAGO} - {self.MZLTS}"
    
    def __str__(self):
        return self.CODIGO_DE_PAGO

class Cobros(models.Model):
    ID_COBROS = models.CharField(primary_key=True, max_length=10)
    NUMERO_DE_RECIBO = models.CharField(max_length=5)
    CODIGO_INTEGRANTE = models.ForeignKey(DataConsolidado, on_delete=models.CASCADE)
    APELLIDO_PATERNO = models.TextField(max_length=20)
    APELLIDO_MATERNO = models.TextField(max_length=20)
    NOMBRES = models.TextField(max_length=20)
    CODIGO_DE_GRUPO_INTEGRANTES = models.CharField(max_length=5)
    FECHA_EMICION_RECIBO = models.DateTimeField(auto_now_add=True)
    FECHA_VENCIMIENTO_RECIBO = models.DateField()
    MONEDA_A_PAGAR = models.CharField(max_length=6)
    CODIGO_REFERENCIA_CLIENTE = models.CharField(max_length=5)
    DESCRIPCION_COBRO_REALIZAR = models.TextField(max_length=200)
    OBSERVACIONES_RECIBO = models.TextField(max_length=200)
    INDICADOR_COBRO_MORA = models.CharField(max_length=1)
    CODIGO_CONCEPTO_1 = models.CharField(max_length=1)
    IMPORTE_COBRO_CONCEPTO_1 = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.ID_COBROS} - {self.NUMERO_DE_RECIBO} - {self.CODIGO_INTEGRANTE} - {self.APELLIDO_PATERNO} - {self.APELLIDO_MATERNO}"

class Recaudaciones(models.Model):
    ID_RECAUDACIONES = models.CharField(primary_key=True, max_length=10)
    NUMERO_DE_RECIBO = models.CharField(max_length=100000)
    CODIGO_INTEGRANTE = models.ForeignKey(DataConsolidado, on_delete=models.CASCADE)
    APELLIDOS_NOMBRES = models.TextField(max_length=40)
    GRUPO = models.CharField(max_length=10)
    DESCRIPCION_RECIBO = models.CharField(max_length=40)
    IMP_RECIBO = models.CharField()
    FECHA_VENCIMIENTO = models.DateField()
    DIA_MORA = models.IntegerField(max_length=1)
    IMP_MORA = models.CharField()
    IMP_TOTAL = models.CharField()
    FECHA_PAGO = models.DateField()
    MZLTE = models.CharField(max_length=5)
    FORMA_PAGO = models.TextField()
    CALC_MORA = models.CharField(2)
    FECHA_ACTUALIZADA = models.DateField()

    def __str__(self):
        return f"{self.ID_RECAUDACIONES} - {self.NUMERO_DE_RECIBO} - {self.CODIGO_INTEGRANTE} - {self.APELLIDOS_NOMBRES} - {self.GRUPO}"

class Resumen(models.Model):
    ID_RESUMEN = models.CharField(primary_key=True, max_length=10) 
    ID_INTEGRANTE = models.CharField()
    FECHA_RESUMEN = models.DateField()
    CVENCIDAS = models.IntegerField()
    CPAGADAS = models.IntegerField()
    SVENCIDOS = models.CharField()
    SPAGADOS = models.CharField()
