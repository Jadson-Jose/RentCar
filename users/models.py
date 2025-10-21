from django.db import models

class User(models.Model):
    TYPES = (
        ('cliente', 'Cliente'),
        ('admin', 'Administrador')
    )
    name = models.CharField(max_length=103)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    types = models.CharField(max_length=10, choices=TYPES)    
