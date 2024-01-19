from rest_framework import routers
from .api import DataClvviem, CobrosClvviem, RecaudacionClvviem
from .views import mi_pagina, recaudaciones, tu_vista, busqueda, recaudacionesbusqueda
from django.urls import path, include

router = routers.DefaultRouter()

router.register('api/clvdat/(?P<codigo_de_pago>\w+)', DataClvviem, 'DataConsolidada')
router.register('api/clvco', CobrosClvviem, 'Cobros')
router.register('api/clvrec', RecaudacionClvviem, 'Recaudaciones')

urlpatterns = [
    path('', mi_pagina, name='mi_pagina'),
    path('listarb/', busqueda, name='listar'),
    path('recaudaciones/', recaudaciones, name='recaudaciones'),
    path('consultacobros/<str:codigo_pago>/', tu_vista, name='nombre_de_la_vista'),
    path('consultarecau/<str:codigo_pago>/', recaudacionesbusqueda, name='nombre_de_la_vista'),
    # Agrega esta línea para tu página personalizada
    path('consumo/', include(router.urls)),
]