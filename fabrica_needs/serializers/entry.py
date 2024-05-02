from rest_framework.serializers import ModelSerializer

from fabrica_needs.models import Entry

class EntrySerializer(ModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"