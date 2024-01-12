from import_export import resources
from .models import DataConsolidado

class DataConsolidadoResource(resources.ModelResource):
    class Meta:
        model = DataConsolidado
        import_id_fields = ['ID_DATOS']
        skip_unchanged = True  # Evitar importar filas que no han cambiado
        report_skipped = False  # No generar informes para filas saltadas
        exclude = ('id',)  # Excluir el campo 'id' de la importación

