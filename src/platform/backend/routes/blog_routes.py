from django.urls import path
from src.backend.views import blog_views  # Ajusta la ruta según tu proyecto

urlpatterns = [
    path('blogs/', blog_views.blog_list, name='blog-list'),
    path('blogs/<int:pk>/', blog_views.blog_detail, name='blog-detail'),
    path('blogs/create/', blog_views.blog_create, name='blog-create'),
    path('blogs/update/<int:pk>/', blog_views.blog_update, name='blog-update'),
    path('blogs/delete/<int:pk>/', blog_views.blog_delete, name='blog-delete'),
]
