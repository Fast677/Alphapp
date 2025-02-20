# src/community/backend/tests/test_user_routes.py
from fastapi.testclient import TestClient
from src.community.backend.main import app  # Importa la instancia de FastAPI
from src.community.backend.models import user_models  # Importa los modelos de usuario
from src.community.backend.utils import auth_utils # Importa funciones de autenticación y autorización
import pytest
from unittest.mock import patch

client = TestClient(app)

# Mock de la base de datos para las pruebas
@pytest.fixture
def mock_db():
    # Aquí puedes configurar un mock de la base de datos
    # Por ejemplo, usando una lista en memoria
    users = []
    return users

def test_create_user(mock_db):
    # Prueba la creación de un usuario
    user_data = {"username": "testuser", "email": "test@example.com", "password": "password123"}
    response = client.post("/community/users/", json=user_data)
    assert response.status_code == 201
    #assert response.json()["username"] == "testuser" #Comprueba si el json de respuesta es correcto
    #assert len(mock_db) == 1 #comprueba si el usuario se agregó a la base de datos mockeada

def test_get_user():
    #Prueba la obtención de un usuario específico (simulando autenticación)
    #Simula la autenticación del usuario (necesitarías un token JWT válido o un mock)
    with patch.object(auth_utils, "verify_token", return_value=True): #Simula que el token es válido
        response = client.get("/community/users/1") #cambia 1 por un id existente
        assert response.status_code == 200
        #assert response.json()["username"] == "existinguser" #verifica que el usuario existente sea correcto

def test_get_nonexistent_user():
    # Prueba la obtención de un usuario que no existe (simulando autenticación)
    with patch.object(auth_utils, "verify_token", return_value=True): #Simula que el token es válido
        response = client.get("/community/users/999")  # ID que no existe
        assert response.status_code == 404
        #assert response.json()["detail"] == "User not found" #verifica que el mensaje de error sea correcto

def test_update_user():
    #Prueba la actualización de un usuario existente (simulando autenticación)
    with patch.object(auth_utils, "verify_token", return_value=True): #Simula que el token es válido
        user_data = {"username": "updateduser", "email": "updated@example.com"}
        response = client.put("/community/users/1", json=user_data) #cambia 1 por un id existente
        assert response.status_code == 200
        #assert response.json()["username"] == "updateduser"  #verifica que el json de respuesta sea correcto

def test_delete_user():
    #Prueba la eliminación de un usuario existente (simulando autenticación)
    with patch.object(auth_utils, "verify_token", return_value=True): #Simula que el token es válido
        response = client.delete("/community/users/1") #cambia 1 por un id existente
        assert response.status_code == 204 #verifica que la respuesta sea "No Content"

# Puedes agregar más pruebas para cubrir otros casos de uso,
# como validaciones de entrada, manejo de errores, etc.
