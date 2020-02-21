from django.urls import path, include
from . import views

urlpatterns = [
    path('list/inventory/', views.inventory, name='inventory_list'),
]
