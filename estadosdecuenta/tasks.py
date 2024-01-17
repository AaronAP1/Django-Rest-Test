from celery import shared_task
from import_export.formats import base_formats
from tablib import Dataset
from .resources import CobrosResource  # Asegúrate de importar tu recurso específico

@shared_task
def import_cobros_async(file_data):
    resource = CobrosResource()
    dataset = Dataset()
    
    dataset.load(file_data, format='xlsx')  # Asegúrate de ajustar el formato según el tipo de archivo que estás manejando
    
    # Lógica de importación
    result = resource.import_data(dataset, dry_run=False, raise_errors=True)

    # Manejar errores y hacer cualquier otra cosa necesaria
    if result.has_errors():
        # Manejar los errores según sea necesario
        errors = result.rows_with_errors()
        # Podrías almacenar los errores en la base de datos, enviar correos electrónicos, etc.
        # ...

    # Puedes realizar cualquier otra lógica que necesites aquí
    # ...

    return result.has_errors()