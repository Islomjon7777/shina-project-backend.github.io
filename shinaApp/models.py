from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass
    

class Product(models.Model):
    CURRENCY_CHOICES = [
        ('UZS', 'UZS'),
        ('USD', 'USDT'),
        ('EUR', 'Eur'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=10)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return self.title



class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)