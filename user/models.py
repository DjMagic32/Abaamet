from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_Ventas = models.BooleanField(default=False)
    is_Metrologia = models.BooleanField(default=False)
    is_Direccion = models.BooleanField(default=False)
    is_Compras = models.BooleanField(default=False)