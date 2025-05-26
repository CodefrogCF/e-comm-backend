from django.urls import path
from . import views

urlpatterns = [
    path('', views.getProducts),
    path('add/', views.addProduct),
]