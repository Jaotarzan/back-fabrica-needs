from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    amount = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name
