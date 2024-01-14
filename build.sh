#!/usr/bin/env bash
# exit on error

set -o errexit

pip install -r requerements.txt

python manage.py collectstatic --no-input
python manage.py migrate

nombre_de_usuario="clv"
correo_electronico="tu_correo@gmail.com"
contrasena="vivaelbarcelona124"

# Verificar si el usuario ya existe
if python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(username='${nombre_de_usuario}').exists())" | grep "True" &> /dev/null; then
    echo "El usuario ya existe. No se creará uno nuevo."
else
    # Crear un usuario de ejemplo
    python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('${nombre_de_usuario}', '${correo_electronico}', '${contrasena}')"
    echo "Usuario creado con éxito."
fi

# Puedes agregar más comandos según sea necesario

# Otros comandos que puedas necesitar ejecutar después de la creación del usuario
# ...

# Finalizar con un mensaje
echo "¡Script de construcción completado con éxito!"