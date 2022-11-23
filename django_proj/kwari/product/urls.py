from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryListCreateView().as_view()),
    path("categories/<int:id>/", views.CategoryRetrieveUpdateDestroyView().as_view()),
    
]
