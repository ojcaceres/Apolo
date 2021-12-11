from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PlanAnualViewSet(viewsets.ModelViewSet):
    """ViewSet for the PlanAnual class"""

    queryset = models.PlanAnual.objects.all()
    serializer_class = serializers.PlanAnualSerializer
    permission_classes = [permissions.IsAuthenticated]


class BaseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Base class"""

    queryset = models.Base.objects.all()
    serializer_class = serializers.BaseSerializer
    permission_classes = [permissions.IsAuthenticated]
