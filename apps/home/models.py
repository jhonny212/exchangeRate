import re
from django.db import models

class ExchangeRate(models.Model):
    """Model definition for ExchangeRate."""
    date = models.DateField("Fecha", auto_now=False, auto_now_add=False,null=False,unique=True)
    sale_price = models.FloatField(null=False)
    purchase_price = models.FloatField(null=False)

    class Meta:
        """Meta definition for ExchangeRate."""

        verbose_name = 'ExchangeRate'
        verbose_name_plural = 'ExchangeRates'

    def __str__(self):
        return f'Fecha: {self.date} tipo de cambio: {self.sale_price}'

