from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

urlpatterns = [
    path('', views.getProducts),
    path('add/', views.addProduct),
    path('update/', views.updateProduct),
    path('delete/', views.deleteProduct),
]

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls