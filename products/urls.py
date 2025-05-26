from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.getProducts),
    path('admin/', admin.site.urls),
    path('add/', views.addProduct),
    path('update/', views.updateProduct),
    path('delete/', views.deleteProduct),
]