from django.urls import path
from src.backend.views import user_views  # Ajusta la ruta según tu proyecto

urlpatterns = [
    path('users/', user_views.user_list, name='user-list'),
    path('users/<int:pk>/', user_views.user_detail, name='user-detail'),
    path('users/create/', user_views.user_create, name='user-create'),
    path('users/update/<int:pk>/', user_views.user_update, name='user-update'),
    path('users/delete/<int:pk>/', user_views.user_delete, name='user-delete'),
]
