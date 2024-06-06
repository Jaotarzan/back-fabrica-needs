from rest_framework.viewsets import ModelViewSet
from fabrica_needs.models import Entry
from fabrica_needs.serializers import EntrySerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class EntryViewSet(ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["donor__username"]