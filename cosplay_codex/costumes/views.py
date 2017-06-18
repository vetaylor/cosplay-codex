from rest_framework import viewsets

from .models import Costume
from .serializers import CostumeSerializer


class CostumeViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing Costume objects."""
    queryset = Costume.objects.all()
    serializer_class = CostumeSerializer
