from django.db import models

# Create your models here.
class Services(models.Model):
    email=models.CharField(max_length=50)
    name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=10)
    reason=models.TextField()

class Checkout(models.Model):
    email=models.CharField(max_length=50)
    name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    quantity=models.CharField(max_length=20)
    creditcardno=models.CharField(max_length=20)
    exp=models.CharField(max_length=10)
    ccv=models.CharField(max_length=10)
        

    def __str__(self):
        return self.name
    
