import pytest
from src.community.backend import routes, models  # Importa las rutas y modelos a probar
from flask import Flask

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    routes.init_app(app)  # Inicializa las rutas en la app de prueba
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_comments(client):
    """Prueba para la ruta GET /comments"""
    response = client.get('/comments')
    assert response.status_code == 200
    # Aquí puedes añadir más aserciones para verificar el contenido de la respuesta
    # Por ejemplo, verificar que la respuesta es un JSON y que contiene una lista de comentarios

def test_create_comment(client):
    """Prueba para la ruta POST /comments"""
    # Datos de ejemplo para crear un comentario
    comment_data = {
        'text': 'This is a test comment.',
        'author': 'Test User',
        'post_id': 1  # Asumiendo que el comentario está asociado a un post con ID 1
    }
    response = client.post('/comments', json=comment_data)
    assert response.status_code == 201
    # Aquí puedes añadir más aserciones para verificar que el comentario se creó correctamente
    # Por ejemplo, verificar que la respuesta es un JSON y que contiene los datos del comentario creado

def test_get_comment_by_id(client):
    """Prueba para la ruta GET /comments/<comment_id>"""
    # Primero, crea un comentario para luego obtenerlo por ID
    comment_data = {
        'text': 'This is a test comment.',
        'author': 'Test User',
        'post_id': 1
    }
    create_response = client.post('/comments', json=comment_data)
    assert create_response.status_code == 201
    comment_id = create_response.get_json()['id']  # Asume que la respuesta contiene el ID del comentario creado

    response = client.get(f'/comments/{comment_id}')
    assert response.status_code == 200
    # Aquí puedes añadir más aserciones para verificar que el comentario obtenido es el correcto
    # Por ejemplo, verificar que la respuesta es un JSON y que contiene los datos del comentario con el ID especificado

def test_update_comment(client):
    """Prueba para la ruta PUT /comments/<comment_id>"""
    # Primero, crea un comentario para luego actualizarlo
    comment_data = {
        'text': 'This is a test comment.',
        'author': 'Test User',
        'post_id': 1
    }
    create_response = client.post('/comments', json=comment_data)
    assert create_response.status_code == 201
    comment_id = create_response.get_json()['id']

    # Datos para actualizar el comentario
    update_data = {
        'text': 'This is an updated test comment.',
        'author': 'Updated Test User'
    }
    update_response = client.put(f'/comments/{comment_id}', json=update_data)
    assert update_response.status_code == 200
    # Aquí puedes añadir más aserciones para verificar que el comentario se actualizó correctamente

def test_delete_comment(client):
    """Prueba para la ruta DELETE /comments/<comment_id>"""
    # Primero, crea un comentario para luego eliminarlo
    comment_data = {
        'text': 'This is a test comment.',
        'author': 'Test User',
        'post_id': 1
    }
    create_response = client.post('/comments', json=comment_data)
    assert create_response.status_code == 201
    comment_id = create_response.get_json()['id']

    delete_response = client.delete(f'/comments/{comment_id}')
    assert delete_response.status_code == 204
