from rest_framework import serializers
from .models import Interaccion

class InteraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaccion
        fields = ['usuario', 'mensaje', 'emocion', 'fecha']
