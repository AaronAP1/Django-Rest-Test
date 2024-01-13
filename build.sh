#!/usr/bin/env bash
# exit on error

set -o errexit

pip install -r requerements.txt

python manage.py collectstatic --no-input
python manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_user('clvadmin', 'aaalenort@gmail.com', 'vivaelbarcelona')" | python manage.py shell

# Puedes agregar más comandos según sea necesario

# Otros comandos que puedas necesitar ejecutar después de la creación del usuario
# ...

# Finalizar con un mensaje
echo "¡Script de construcción completado con éxito!"