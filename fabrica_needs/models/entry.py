from django.db import models
from django.contrib.auth.models import User
from .wallet import Wallet
    
class Entry(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    donor = models.ForeignKey(User, on_delete=models.PROTECT, related_name="doação")

    def __str__(self):
        return self.donor

        
