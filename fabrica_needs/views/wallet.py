from rest_framework.viewsets import ModelViewSet

from fabrica_needs.models import Wallet
from fabrica_needs.serializers import WalletSerializer

class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer