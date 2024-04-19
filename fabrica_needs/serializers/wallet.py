from rest_framework.serializers import ModelSerializer

from fabrica_needs.models import Wallet

class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"