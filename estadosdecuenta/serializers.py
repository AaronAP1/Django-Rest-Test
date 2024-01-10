from rest_framework import serializers
from .models import DataConsolidado, Cobros, Recaudaciones

class ClvDataSerializer (serializers.ModelSerializer):
    class Meta: 
        model = DataConsolidado
        fields = '__all__'

class ClvCobrosSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Cobros
        fields = '__all__'


class ClvRecaudacionesSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Recaudaciones
        fields = '__all__'

