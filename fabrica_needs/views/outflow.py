from rest_framework.viewsets import ModelViewSet
from fabrica_needs.models import Outflow
from fabrica_needs.serializers import OutflowSerializer
from rest_framework.permissions import IsAuthenticated

class OutflowViewSet(ModelViewSet):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer
    permission_classes = [IsAuthenticated]