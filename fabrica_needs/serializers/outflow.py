from rest_framework.serializers import ModelSerializer

from fabrica_needs.models import Outflow

class OutflowSerializer(ModelSerializer):
    class Meta:
        model = Outflow
        fields = "__all__"