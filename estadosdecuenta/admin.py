from django.contrib import admin
from .models import DataConsolidado, Cobros, Recaudaciones
from import_export.admin import ImportExportActionModelAdmin
from .resources import DataConsolidadoResource 



@admin.register(DataConsolidado)
class DataConsolidadoAdmin(ImportExportActionModelAdmin):
    resource_class = DataConsolidadoResource  # Especifica la clase de recurso
    list_display = ( 'ITEM', 'CODIGO_DE_PAGO', 'MZLTS', 'CAPTACION', 'ASESOR', 'APELLIDO_PATERNO', 'APELLIDO_MATERNO', 'NOMBRES', 'DOC', 'NUMERO', 'DIRECCION', 'DISTRITO', 'PROVINCIA', 'DEPARTAMENTO', 'CELULAR', 'EMAIL', 'M2', 'UBICACION', 'PRECIOVENTA', 'INICIAL', 'SALDO', 'CUOTAS', 'CUOTA', 'INICIOPAGO', 'CVENCIDAS', 'CPAGADAS', 'SVENCIDOS', 'SPAGADOS', 'COMENTARIO')
    search_fields = ('CODIGO_DE_PAGO',)
admin.site.register(Cobros)
admin.site.register(Recaudaciones)

# Register your models here.
