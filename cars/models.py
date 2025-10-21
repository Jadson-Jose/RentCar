from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    marca_id = models.IntegerField(null=True, blank=True)
    modelo_id = models.IntegerField(null=True, blank=True)
    ano_codigo = models.CharField(max_length=10, null=True, blank=True)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"
