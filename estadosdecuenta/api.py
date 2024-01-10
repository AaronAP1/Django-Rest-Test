from .models import DataConsolidado, Cobros, Recaudaciones
from rest_framework import viewsets, permissions
from .serializers import ClvDataSerializer, ClvCobrosSerializer, ClvRecaudacionesSerializer


class DataClvviem(viewsets.ModelViewSet):
    queryset = DataConsolidado.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClvDataSerializer

class CobrosClvviem(viewsets.ModelViewSet):
    queryset = Cobros.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClvCobrosSerializer

class RecaudacionClvviem(viewsets.ModelViewSet):
    queryset = Recaudaciones.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClvRecaudacionesSerializer