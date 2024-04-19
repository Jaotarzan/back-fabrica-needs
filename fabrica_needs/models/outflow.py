from django.db import models

class Outflow(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.amount