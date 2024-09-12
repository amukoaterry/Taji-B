from rest_framework import serializers
from scanevent.models import ScanEvent

class ScanEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanEvent
        fields = '__all__'
