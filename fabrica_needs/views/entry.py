from rest_framework.viewsets import ModelViewSet

from fabrica_needs.models import Entry
from fabrica_needs.serializers import EntrySerializer

class EntryViewSet(ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer