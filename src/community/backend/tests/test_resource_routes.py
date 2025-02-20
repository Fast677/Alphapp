# src/community/backend/tests/test_resource_routes.py
from fastapi.testclient import TestClient
from src.community.backend.main import app  # Importa la instancia de FastAPI
from src.community.backend.models import resource_models  # Importa los modelos de recursos
from src.community.backend.utils import auth_utils # Importa funciones de autenticación y autorización
import pytest
from unittest.mock import patch

client = TestClient(app)

# Mock de la base de datos para las pruebas
@pytest.fixture
def mock_db():
    # Aquí puedes configurar un mock de la base de datos
    # Por ejemplo, usando una lista en memoria
    resources = []
    return resources

def test_create_resource(mock_db):
    # Prueba la creación de un recurso
    resource_data = {"title": "Tutorial de FastAPI", "url": "https://example.com/fastapi", "description": "Un tutorial para aprender FastAPI"}
    #Simula la autenticación del usuario (necesitarías un token JWT válido o un mock)
    with patch.object(auth_utils, "verify_token", return_value=True): #Simula que el token es válido
        response = client.post("/community/resources/", json=resource_data)
        assert response.status_code == 201
        #assert response.json()["title"] == "Tutorial de FastAPI" #Comprueba si el json de respuesta es correcto
        #assert len(mock_db) == 1 #comprueba si el recurso se agregó a la base de datos mockeada

def test_get_resource():
    #Prueba la obtención de un recurso específico (simulando autenticación)
    with patch.object(auth_utils, "verify_token", return_value=True): #Simula que el token es válido
        response = client.get("/community/resources/1") #cambia 1 por un id existente
        assert response.status_code == 200
        #assert response.json()["title"] == "existing resource" #verifica que el recurso existente sea correcto

def test_get_nonexistent_resource():
    # Prueba la obtención de un recurso que no existe (simulando autenticación)
    with patch.object(auth_utils, "verify_token", return_value=True): #Simula que el token es válido
        response = client.get("/community/resources/999")  # ID que no existe
        assert response.status_code == 404
        #assert response.json()["detail"] == "Resource not found" #verifica que el mensaje de error sea correcto

def test_update_resource():
    #Prueba la actualización de un recurso existente (simulando autenticación)
    with patch.object(auth_utils, "verify_token", return_value=True): #Simula que el token es válido
        resource_data = {"title": "Tutorial de FastAPI actualizado", "url": "https://example.com/fastapi-updated", "description": "Un tutorial actualizado para aprender FastAPI"}
        response = client.put("/community/resources/1", json=resource_data) #cambia 1 por un id existente
        assert response.status_code == 200
        #assert response.json()["title"] == "Tutorial de FastAPI actualizado"  #verifica que el json de respuesta sea correcto

def test_delete_resource():
    #Prueba la eliminación de un recurso existente (simulando autenticación)
    with patch.object(auth_utils, "verify_token", return_value=True): #Simula que el token es válido
        response = client.delete("/community/resources/1") #cambia 1 por un id existente
        assert response.status_code == 204 #verifica que la respuesta sea "No Content"

# Puedes agregar más pruebas para cubrir otros casos de uso,
# como validaciones de entrada, manejo de errores, etc.
