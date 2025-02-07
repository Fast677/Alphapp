from django.urls import path
from src.backend.views import order_views  # Ajusta la ruta según tu proyecto

urlpatterns = [
    path('orders/', order_views.order_list, name='order-list'),
    path('orders/<int:pk>/', order_views.order_detail, name='order-detail'),
    path('orders/create/', order_views.order_create, name='order-create'),
    path('orders/update/<int:pk>/', order_views.order_update, name='order-update'),
    path('orders/delete/<int:pk>/', order_views.order_delete, name='order-delete'),
]
