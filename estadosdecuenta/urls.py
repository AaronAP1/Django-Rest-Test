from rest_framework import routers
from .api import DataClvviem, CobrosClvviem, RecaudacionClvviem
from .views import mi_pagina, tu_vista, tu_vista2, tu_vista3info
from django.urls import path, include

router = routers.DefaultRouter()

router.register('api/clvdat', DataClvviem, 'DataConsolidada' )
router.register('api/clvco', CobrosClvviem, 'Cobros' )
router.register('api/clvrec', RecaudacionClvviem, 'Recaudaciones')

urlpatterns = [
    path('', mi_pagina, name='mi_pagina'),
    path('consultacobros/<str:codigo_pago>/', tu_vista, name='nombre_de_la_vista'),
    path('consultarecau/<str:codigo_pago>/', tu_vista, name='nombre_de_la_vista'),
    path('consultainfo/<str:codigo_pago>/', tu_vista, name='nombre_de_la_vista'),  # Agrega esta línea para tu página personalizada
    path('consumo/', include(router.urls)),
]