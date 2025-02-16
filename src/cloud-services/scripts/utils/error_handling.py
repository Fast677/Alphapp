# cloud-services/scripts/utils/error_handling.py
import logging
import json
from utils import config_utils  # Importa el módulo config_utils si es necesario

# Configuración básica del logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class AppError(Exception):
    """
    Clase base para errores personalizados de la aplicación.
    """
    def __init__(self, message, status_code=500, details=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}

    def to_dict(self):
        """
        Convierte el error a un diccionario para facilitar la serialización JSON.
        """
        return {
            'error': self.message,
            'status_code': self.status_code,
            'details': self.details
        }

def handle_error(error):
    """
    Maneja una excepción, registra el error y retorna una respuesta JSON formateada.
    Args:
        error (Exception): La excepción a manejar.
    Returns:
        tuple: Una tupla que contiene la respuesta JSON y el código de estado HTTP.
    """
    if isinstance(error, AppError):
        # Si es un error de la aplicación, usa la información del error
        error_dict = error.to_dict()
        status_code = error.status_code
    else:
        # Si es un error inesperado, crea un error genérico
        error_dict = {'error': 'Error interno del servidor', 'status_code': 500, 'details': {}}
        status_code = 500
        logging.exception(error)  # Registra el error con el traceback

    # Registra el error
    logging.error(f"Error: {error_dict['error']}, Detalles: {error_dict['details']}")

    # Formatea la respuesta como JSON
    response_json = json.dumps(error_dict, indent=4)
    return response_json, status_code

def raise_app_error(message, status_code=400, details=None):
    """
    Función auxiliar para lanzar un AppError con facilidad.
    Args:
        message (str): El mensaje de error.
        status_code (int): El código de estado HTTP.
        details (dict): Detalles adicionales del error.
    Raises:
        AppError: Una instancia de AppError.
    """
    raise AppError(message, status_code, details)

# Ejemplo de uso
if __name__ == "__main__":
    try:
        # Simula un error
        raise ValueError("Valor inválido")
    except ValueError as e:
        # Maneja el error
        error_response, status_code = handle_error(e)
        print(f"Error Response: {error_response}")
        print(f"Status Code: {status_code}")

    try:
        # Simula un error de la aplicación
        raise_app_error("Error de validación", status_code=400, details={'campo': 'nombre', 'mensaje': 'El nombre es requerido'})
    except AppError as e:
        # Maneja el error de la aplicación
        error_response, status_code = handle_error(e)
        print(f"Error Response: {error_response}")
        print(f"Status Code: {status_code}")
