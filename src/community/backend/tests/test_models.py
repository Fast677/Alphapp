import pytest
from src.community.backend import models  # Importa los modelos a probar
# Ejemplo de prueba para un modelo llamado 'User'
def test_user_creation():
    user = models.User(username='testuser', email='test@example.com')
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    # Puedes añadir más aserciones para validar otros atributos
# Ejemplo de prueba para un modelo llamado 'Post'
def test_post_creation():
    user = models.User(username='testuser', email='test@example.com')
    post = models.Post(title='Test Post', content='This is a test post.', author=user)
    assert post.title == 'Test Post'
    assert post.content == 'This is a test post.'
    assert post.author == user
