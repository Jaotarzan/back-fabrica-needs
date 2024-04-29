from django.db import models

class Wallet(models.Model):
   balance = models.DecimalField(max_digits=7, decimal_places=2, default=0)

   def __str__(self):
        return str(self.balance)