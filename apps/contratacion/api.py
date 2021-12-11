from rest_framework import viewsets, permissions

from . import serializers
from . import models

class ProcesoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Proceso class"""
    queryset = models.Proceso.objects.all()
    serializer_class = serializers.ProcesoSerializer
    permission_classes = [permissions.IsAuthenticated]