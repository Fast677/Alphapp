# cloud-services/src/modules/module-name/module_utils.py

# Importaciones necesarias
import os
import json
import logging

# Configuración básica del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file):
    """
    Carga la configuración desde un archivo JSON.
    Args:
        config_file (str): Ruta al archivo de configuración.
    Returns:
        dict: Diccionario con la configuración cargada.
              Retorna None si el archivo no existe o hay un error al cargar.
    """
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
            logging.info(f"Configuración cargada desde {config_file}")
            return config
    except FileNotFoundError:
        logging.error(f"Archivo de configuración no encontrado: {config_file}")
        return None
    except json.JSONDecodeError:
        logging.error(f"Error al decodificar el archivo JSON: {config_file}")
        return None

def get_environment_variable(variable_name, default_value=None):
    """
    Obtiene una variable de entorno.
    Args:
        variable_name (str): Nombre de la variable de entorno.
        default_value (str, optional): Valor por defecto si la variable no está definida. Defaults to None.
    Returns:
        str: Valor de la variable de entorno.
             Retorna el valor por defecto si la variable no está definida.
             Retorna None si no se proporciona un valor por defecto.
    """
    value = os.environ.get(variable_name)
    if value is None:
        if default_value is not None:
            logging.warning(f"Variable de entorno {variable_name} no definida. Usando el valor por defecto.")
            return default_value
        else:
            logging.error(f"Variable de entorno {variable_name} no definida y no se proporcionó un valor por defecto.")
            return None
    else:
        return value

def validate_data(data, schema):
    """
    Valida los datos según un esquema definido.
    Args:
        data (dict): Datos a validar.
        schema (dict): Esquema de validación.
    Returns:
        bool: True si los datos son válidos, False en caso contrario.
    """
    # Implementar lógica de validación (ejemplo básico)
    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            logging.error(f"Error de validación: {key} debe ser de tipo {expected_type}")
            return False
    return True

def process_data(data):
    """
    Función de ejemplo para procesar datos.
    Args:
        data (any): Datos a procesar.
    Returns:
        any: Datos procesados.
    """
    # Implementar lógica de procesamiento de datos
    logging.info(f"Datos procesados: {data}")
    return data

# Ejemplo de esquema de validación
EXAMPLE_SCHEMA = {
    "name": str,
    "age": int,
    "email": str
}

if __name__ == "__main__":
    # Ejemplo de uso de las funciones
    config = load_config('config.json')
    if config:
        print(f"Configuración: {config}")

    db_host = get_environment_variable('DB_HOST', 'localhost')
    print(f"Host de la base de datos: {db_host}")

    data = {"name": "Test", "age": 30, "email": "test@example.com"}
    if validate_data(data, EXAMPLE_SCHEMA):
        print("Datos validados correctamente.")
        processed_data = process_data(data)
        print(f"Datos procesados: {processed_data}")
    else:
        print("Error de validación de datos.")
