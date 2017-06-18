from rest_framework import serializers

from .models import Costume


class CostumeSerializer(serializers.ModelSerializer):
    """Serializer for Costume."""
    class Meta:
        model = Costume
        fields = ('name', 'series', 'date_added', 'owner',)
