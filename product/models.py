from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug  = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()

    
    
    
    def __str__(self):
        return self.name
    