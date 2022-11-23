from rest_framework import serializers
from .models import ProductItem, Category

class ProductItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = ProductItem
        
        
        

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = Category
        
        
        