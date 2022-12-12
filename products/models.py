from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2 ,null=False)
    description = models.CharField(max_length=500, null=False)
    image = models.ImageField(null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_products")
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2 ,null=False)
    description = models.CharField(max_length=500, null=False)
    image = models.ImageField(null=True)