from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *

# Create your views here.
class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
    