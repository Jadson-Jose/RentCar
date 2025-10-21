from django.db import models
from cars.models import Car

class Store(models.Model):
    STORE_TYPES = (
        ("purchase", "Purchase"),
        ("rental", "Rental"),
    )
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    store_type = models.CharField(max_length=10, choices=STORE_TYPES)
    cars = models.ManyToManyField(Car, related_name="stores")
    
    def __str__(self):
        return f"{self.name} ({self.store_type})"
