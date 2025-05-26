from django.urls import path
from . import views

urlpatterns = [
    path('', views.getProducts),
    path('add/', views.addProduct),
    path('update/', views.updateProduct),
    path('delete/', views.deleteProduct),
]