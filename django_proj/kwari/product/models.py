from django.db import models
import uuid

class Category(models.Model):
    # id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True)
    desc = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
 
    def __str__(self):
        return self.name
    
    
    

class ProductItem(models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.TextField()
    price = models.FloatField()
    quantity_available = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name