from django.db import models
from users.models import User
from cars.models import Car


class Order(models.Model):
    ORDER_TYPES = (
        ('comprar', 'Comprar'),
        ('alugar', 'Alugar')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=10, choices=ORDER_TYPES)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.order_type.title()} - {self.car.model} by {self.user.name}"
