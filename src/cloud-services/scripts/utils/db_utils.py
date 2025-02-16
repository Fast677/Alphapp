# cloud-services/scripts/utils/db_utils.py
import os
import psycopg2  # Para PostgreSQL
#import mysql.connector # Para MySQL
from utils import config_utils # Importa el módulo config_utils

# Obtener la configuración de la base de datos desde el archivo de configuración
db_config = config_utils.load_config().get('database')

# Función para establecer la conexión a la base de datos
def connect_db():
    """
    Establece una conexión a la base de datos PostgreSQL.
    Returns:
        psycopg2.extensions.connection: Objeto de conexión a la base de datos.
    """
    try:
        conn = psycopg2.connect(
            host=db_config.get('host'),
            database=db_config.get('database'),
            user=db_config.get('user'),
            password=db_config.get('password')
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def execute_query(query, params=None):
    """
    Ejecuta una consulta SQL en la base de datos.
    Args:
        query (str): La consulta SQL a ejecutar.
        params (tuple, optional): Parámetros para la consulta. Defaults to None.
    Returns:
        list: Lista de resultados de la consulta.
    """
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()  # Guarda los cambios
            if cur.description:
                results = cur.fetchall()
            else:
                results = None
            cur.close()
            conn.close()
            return results
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            conn.rollback()  # Revierte los cambios en caso de error
            return None

def fetch_data(query, params=None):
    """
    Obtiene datos de la base de datos.
    Args:
        query (str): La consulta SQL para obtener los datos.
        params (tuple, optional): Parámetros para la consulta. Defaults to None.
    Returns:
        list: Lista de resultados de la consulta.
    """
    return execute_query(query, params)

def insert_data(query, params=None):
    """
    Inserta datos en la base de datos.
    Args:
        query (str): La consulta SQL para insertar los datos.
        params (tuple, optional): Parámetros para la consulta. Defaults to None.
    """
    execute_query(query, params)

def update_data(query, params=None):
    """
    Actualiza datos en la base de datos.
    Args:
        query (str): La consulta SQL para actualizar los datos.
        params (tuple, optional): Parámetros para la consulta. Defaults to None.
    """
    execute_query(query, params)

def delete_data(query, params=None):
    """
    Elimina datos de la base de datos.
    Args:
        query (str): La consulta SQL para eliminar los datos.
        params (tuple, optional): Parámetros para la consulta. Defaults to None.
    """
    execute_query(query, params)

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una tabla de ejemplo
    create_table_query = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL
    )
    """
    execute_query(create_table_query)

    # Insertar un usuario
    insert_query = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
    insert_params = ('Juan Pérez', 'juan@example.com')
    insert_data(insert_query, insert_params)

    # Obtener todos los usuarios
    select_query = "SELECT * FROM usuarios"
    usuarios = fetch_data(select_query)
    print(f"Usuarios en la base de datos: {usuarios}")

    # Actualizar el email de un usuario
    update_query = "UPDATE usuarios SET email = %s WHERE nombre = %s"
    update_params = ('juan.perez@example.com', 'Juan Pérez')
    update_data(update_query, update_params)

    # Eliminar un usuario
    delete_query = "DELETE FROM usuarios WHERE nombre = %s"
    delete_params = ('Juan Pérez',)
    delete_data(delete_query, delete_params)
