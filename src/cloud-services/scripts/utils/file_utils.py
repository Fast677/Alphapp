# cloud-services/scripts/utils/file_utils.py
import os
import json
from utils import config_utils  # Importa el módulo config_utils

# Función para leer un archivo de texto
def read_file(file_path):
    """
    Lee el contenido de un archivo de texto.
    Args:
        file_path (str): La ruta al archivo.
    Returns:
        str: El contenido del archivo, o None si hay un error.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{file_path}': {e}")
        return None

# Función para escribir en un archivo de texto
def write_file(file_path, content):
    """
    Escribe contenido en un archivo de texto.
    Args:
        file_path (str): La ruta al archivo.
        content (str): El contenido a escribir.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Se ha escrito en el archivo '{file_path}'")
    except Exception as e:
        print(f"Error al escribir en el archivo '{file_path}': {e}")

# Función para leer un archivo JSON
def read_json_file(file_path):
    """
    Lee el contenido de un archivo JSON.
    Args:
        file_path (str): La ruta al archivo JSON.
    Returns:
        dict: El contenido del archivo JSON como un diccionario, o None si hay un error.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo JSON '{file_path}' no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo JSON '{file_path}' no es un JSON válido.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo JSON '{file_path}': {e}")
        return None

# Función para escribir en un archivo JSON
def write_json_file(file_path, data):
    """
    Escribe datos en un archivo JSON.
    Args:
        file_path (str): La ruta al archivo JSON.
        data (dict): Los datos a escribir en formato de diccionario.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)  # Indentación para legibilidad
        print(f"Se ha escrito en el archivo JSON '{file_path}'")
    except Exception as e:
        print(f"Error al escribir en el archivo JSON '{file_path}': {e}")

# Función para crear un directorio si no existe
def create_directory(dir_path):
    """
    Crea un directorio si no existe.
    Args:
        dir_path (str): La ruta del directorio a crear.
    """
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Se ha creado el directorio '{dir_path}'")
        else:
            print(f"El directorio '{dir_path}' ya existe.")
    except Exception as e:
        print(f"Error al crear el directorio '{dir_path}': {e}")

# Función para verificar si un archivo existe
def file_exists(file_path):
    """
    Verifica si un archivo existe.
    Args:
        file_path (str): La ruta del archivo a verificar.
    Returns:
        bool: True si el archivo existe, False en caso contrario.
    """
    return os.path.exists(file_path)

# Función para eliminar un archivo
def delete_file(file_path):
    """
    Elimina un archivo.
    Args:
        file_path (str): La ruta del archivo a eliminar.
    """
    try:
        os.remove(file_path)
        print(f"Se ha eliminado el archivo '{file_path}'")
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
    except Exception as e:
        print(f"Error al eliminar el archivo '{file_path}': {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de lectura de un archivo
    file_content = read_file('example.txt')
    if file_content:
        print(f"Contenido del archivo: {file_content}")

    # Ejemplo de escritura en un archivo
    write_file('example.txt', 'Este es un ejemplo de contenido.')

    # Ejemplo de lectura de un archivo JSON
    json_data = read_json_file('example.json')
    if json_data:
        print(f"Contenido del archivo JSON: {json_data}")

    # Ejemplo de escritura en un archivo JSON
    data = {'nombre': 'Juan', 'edad': 30}
    write_json_file('example.json', data)

    # Ejemplo de creación de un directorio
    create_directory('new_directory')

    # Ejemplo de verificación de existencia de un archivo
    if file_exists('example.txt'):
        print("El archivo 'example.txt' existe.")
    else:
        print("El archivo 'example.txt' no existe.")

    # Ejemplo de eliminación de un archivo
    delete_file('example.txt')
