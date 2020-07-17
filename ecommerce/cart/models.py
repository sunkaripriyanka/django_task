from django.db import models

# Create your models here.
class Login(models.Model):
    userName = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Item(models.Model):
    productName = models.CharField(max_length=20)
    productPrice = models.CharField(max_length=7)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Order(models.Model):
    productName = models.ForeignKey(Item, on_delete = models.CASCADE)
    userName = models.ForeignKey(Login, on_delete = models.CASCADE)
    quantity = models.CharField(max_length=7)
    paymentMethod = models.CharField(max_length=50)
    dateOfPurchase = models.CharField(max_length=80)
    
    