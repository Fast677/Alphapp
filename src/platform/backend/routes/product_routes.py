from django.urls import path
from src.backend.views import product_views  # Ajusta la ruta según tu proyecto

urlpatterns = [
    path('products/', product_views.product_list, name='product-list'),
    path('products/<int:pk>/', product_views.product_detail, name='product-detail'),
    path('products/create/', product_views.product_create, name='product-create'),
    path('products/update/<int:pk>/', product_views.product_update, name='product-update'),
    path('products/delete/<int:pk>/', product_views.product_delete, name='product-delete'),
]
