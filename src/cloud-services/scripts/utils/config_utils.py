# src/cloud-services/scripts/utils/config_utils.py
import os
import configparser  # Para leer archivos .ini
import json # Para leer archivos .json

CONFIG_FILE_PATH = os.environ.get('CONFIG_FILE_PATH', 'config/development.ini') # archivo de configuración por defecto

def load_config():
    """
    Carga la configuración desde un archivo .ini o .json.

    Returns:
        dict: Un diccionario con la configuración.
    """
    config = {}
    if CONFIG_FILE_PATH.endswith('.ini'):
        config = load_ini_config(CONFIG_FILE_PATH)
    elif CONFIG_FILE_PATH.endswith('.json'):
        config = load_json_config(CONFIG_FILE_PATH)
    else:
        print("Formato de archivo de configuración no soportado. Usando configuración por defecto.")
    return config

def load_ini_config(file_path):
    """
    Carga la configuración desde un archivo .ini.

    Args:
        file_path (str): La ruta al archivo .ini.

    Returns:
        dict: Un diccionario con la configuración.
    """
    config = configparser.ConfigParser()
    config.read(file_path)
    # Convertir la configuración a un diccionario
    config_dict = {}
    for section in config.sections():
        config_dict[section] = dict(config.items(section))
    return config_dict

def load_json_config(file_path):
    """
    Carga la configuración desde un archivo .json.

    Args:
        file_path (str): La ruta al archivo .json.

    Returns:
        dict: Un diccionario con la configuración.
    """
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Archivo de configuración no encontrado: {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: {file_path}")
        return {}

def get_config_value(section, key, default=None):
    """
    Obtiene un valor de configuración específico.

    Args:
        section (str): La sección en el archivo de configuración.
        key (str): La clave del valor a obtener.
        default (any, optional): El valor por defecto si la clave no se encuentra. Defaults to None.

    Returns:
        any: El valor de configuración, o el valor por defecto si no se encuentra.
    """
    config = load_config()
    try:
        return config[section][key]
    except KeyError:
        return default

# Ejemplo de uso:
if __name__ == "__main__":
    config = load_config()
    print(f"Configuración cargada: {config}")
    api_url = get_config_value('api', 'base_url', 'http://localhost:8000')
    print(f"URL de la API: {api_url}")
