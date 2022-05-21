from django.db import models

# Create your models here.
class Product(models.Model):
    Title = models.CharField(max_length=70)
    bjNumber = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.Title
