from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.patient_dashboard, name='patient_dashboard'),
    path('list/patients/', views.patient, name='patient_list'),
]
