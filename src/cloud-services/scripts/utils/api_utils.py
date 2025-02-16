# cloud-services/scripts/utils/api_utils.py

import requests
import json
from . import config_utils  # Importa utilidades de configuración
from . import error_handling # Importa utilidades para el manejo de errores

# Cargar la configuración de la API (ejemplo)
api_config = config_utils.load_config().get('api', {})
BASE_URL = api_config.get('base_url', 'https://api.alphapp.xyz') # URL base de la API

def make_api_request(method, endpoint, data=None, headers=None):
    """
    Realiza una solicitud a la API de Alphapp.

    Args:
        method (str): Método HTTP ('GET', 'POST', 'PUT', 'DELETE').
        endpoint (str): Endpoint de la API (ej., '/users').
        data (dict, optional): Datos a enviar en el cuerpo de la solicitud (para POST, PUT). Defaults to None.
        headers (dict, optional): Encabezados adicionales para la solicitud. Defaults to None.

    Returns:
        requests.Response: Objeto de respuesta de la solicitud.
    """
    url = f"{BASE_URL}{endpoint}"
    try:
        if headers is None:
            headers = {}
        # Añadir encabezado para indicar que se envía JSON si hay datos
        if data:
            headers['Content-Type'] = 'application/json'
            data = json.dumps(data)  # Convertir a JSON

        response = requests.request(method, url, data=data, headers=headers)
        response.raise_for_status()  # Lanza una excepción para códigos de error 4XX/5XX
        return response
    except requests.exceptions.RequestException as e:
        error_handling.handle_error(f"Error en la solicitud a la API: {e}") #Utiliza la función para manejo de errores
        return None  # O quizás lanzar la excepción, dependiendo de cómo quieras manejar los errores

def get_resource(endpoint, headers=None):
    """
    Obtiene un recurso de la API utilizando el método GET.

    Args:
        endpoint (str): Endpoint del recurso a obtener.
        headers (dict, optional): Encabezados adicionales para la solicitud. Defaults to None.

    Returns:
        dict: Datos del recurso en formato JSON, o None si hay un error.
    """
    response = make_api_request('GET', endpoint, headers=headers)
    if response:
        try:
            return response.json()
        except json.JSONDecodeError:
            error_handling.handle_error("Error al decodificar la respuesta JSON.")
            return None
    return None

def create_resource(endpoint, data, headers=None):
    """
    Crea un nuevo recurso en la API utilizando el método POST.

    Args:
        endpoint (str): Endpoint para crear el recurso.
        data (dict): Datos del nuevo recurso.
        headers (dict, optional): Encabezados adicionales para la solicitud. Defaults to None.

    Returns:
        dict: Datos del recurso creado en formato JSON, o None si hay un error.
    """
    response = make_api_request('POST', endpoint, data=data, headers=headers)
    if response:
        try:
            return response.json()
        except json.JSONDecodeError:
            error_handling.handle_error("Error al decodificar la respuesta JSON.")
            return None
    return None

#Ejemplo de uso de autenticación con tokens JWT
def set_jwt_header(token):
    """
    Crea un encabezado de autorización con un token JWT.
    Args:
        token (str): El token JWT.
    Returns:
        dict: Un diccionario con el encabezado de autorización.
    """
    return {'Authorization': f'Bearer {token}'}

# Otras funciones para actualizar, eliminar recursos, etc.
