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

def test_get_events(client):
    """Prueba para la ruta GET /events"""
    response = client.get('/events')
    assert response.status_code == 200
    # Aquí puedes añadir más aserciones para verificar el contenido de la respuesta
    # Por ejemplo, verificar que la respuesta es un JSON y que contiene una lista de eventos

def test_create_event(client):
    """Prueba para la ruta POST /events"""
    # Datos de ejemplo para crear un evento
    event_data = {
        'title': 'Test Event',
        'description': 'This is a test event.',
        'date': '2024-12-31'
    }
    response = client.post('/events', json=event_data)
    assert response.status_code == 201
    # Aquí puedes añadir más aserciones para verificar que el evento se creó correctamente
    # Por ejemplo, verificar que la respuesta es un JSON y que contiene los datos del evento creado

def test_get_event_by_id(client):
    """Prueba para la ruta GET /events/<event_id>"""
    # Primero, crea un evento para luego obtenerlo por ID
    event_data = {
        'title': 'Test Event',
        'description': 'This is a test event.',
        'date': '2024-12-31'
    }
    create_response = client.post('/events', json=event_data)
    assert create_response.status_code == 201
    event_id = create_response.get_json()['id']  # Asume que la respuesta contiene el ID del evento creado

    response = client.get(f'/events/{event_id}')
    assert response.status_code == 200
