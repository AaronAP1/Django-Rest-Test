from rest_framework import routers
from .api import DataClvviem, CobrosClvviem, RecaudacionClvviem
from .views import mi_pagina
from django.urls import path, include

router = routers.DefaultRouter()

router.register('api/clvdat', DataClvviem, 'DataConsolidada' )
router.register('api/clvco', CobrosClvviem, 'Cobros' )
router.register('api/clvrec', RecaudacionClvviem, 'Recaudaciones')

urlpatterns = [
    path('', mi_pagina, name='mi_pagina'),  # Agrega esta línea para tu página personalizada
    path('consumo/', include(router.urls)),
]