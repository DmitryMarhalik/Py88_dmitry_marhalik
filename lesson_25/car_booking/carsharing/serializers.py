from .models import Auto
from rest_framework.serializers import ModelSerializer


class AutoSerializer(ModelSerializer):
    class Meta:
        model = Auto
        fields = '__all__'
