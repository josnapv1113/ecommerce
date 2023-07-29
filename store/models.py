from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Product(models.Model):
    Product_name = models.CharField(max_length=100)


    def __str__(self):
        return self.Product_name


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    Product_name = models.ForeignKey(Product,on_delete=models.CASCADE,default=1 )
    description = models.CharField(max_length=100)
    price= models.IntegerField(default=0)
    image= models.ImageField(upload_to='uploads/products/')
    is_active = models.BooleanField(default=True)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.customer_name

    def save(self, *args, **kwargs):
        # Check if the product is older than 2 months and set is_active to False
        two_months_ago = timezone.now() - timedelta(days=60)
        if self.registration_date < two_months_ago:
            self.is_active = False
        super(Customer, self).save(*args, **kwargs)

