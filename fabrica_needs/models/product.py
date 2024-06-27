from django.db import models
from uploader.models import Image


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    amount = models.IntegerField(default=0, null=True, blank=True)
    min = models.IntegerField(default=0, null=True, blank=True)
    appearence = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )
    def __str__(self):
        return self.name
