from email.policy import default
from django.db import models
from User.models import User
from django.utils import timezone

# Create your models here.

# class MenuItem to be ordred by the user
class MenuItem(models.Model):
    name = models.CharField(max_length=30, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.CharField(max_length=30, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Item : {self.name}  ({self.price} MAD)'

# class Card to add menu items to the cart
class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.menu_item} x {self.quantity} . total of{self.total} MAD'


# class Order to add all orders in the card, many to many relationship

class Order(models.Model):
    STATUS_CHOICES = (
        ("COOKING", "Cooking"),
        ("READY", "Ready"),
        ("ONTHEWAY", "On the way"),
        ("DELIVERED" ,"Delivered"),
    )

    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    orders=models.ManyToManyField(Card)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    payment_method = models.CharField(max_length=60, default='cash on delivery')
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default="COOKING")

    
    def __str__(self):
        return f'Order {self.id} by {self.user}'


# Review class to add reviews to the menu items
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=10)
    
    def __str__(self):
        return f'{self.user} review {self.menu_item}'