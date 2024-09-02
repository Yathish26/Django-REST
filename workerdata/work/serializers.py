from rest_framework import serializers
from .models import Workers

class WorkerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = '__all__'