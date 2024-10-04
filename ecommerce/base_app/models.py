# models.py
from django.conf import settings
from django.db import models



 
# models.py
class Category(models.Model):
    Category_name = models.CharField(max_length=100,null=True)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.Category_name



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(default="No description available",null=True)  # Provide a default value
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    feedback=models.TextField()


    def __str__(self):
        return self.name




