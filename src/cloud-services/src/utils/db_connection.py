# cloud-services/src/utils/db_connection.py

import os
import logging
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    """
    Clase para manejar la conexión a la base de datos PostgreSQL.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection_pool = None
        return cls._instance

    def __init__(self):
        if self.connection_pool is None:
           self.initialize_connection_pool()

    def initialize_connection_pool(self):
      """
      Inicializa el pool de conexiones a la base de datos utilizando variables de entorno.
      """
      try:
          db_host = os.getenv("DB_HOST")
          db_name = os.getenv("DB_NAME")
          db_user = os.getenv("DB_USER")
          db_password = os.getenv("DB_PASSWORD")
          db_port = os.getenv("DB_PORT", "5432")
          min_conn = int(os.getenv("DB_MIN_CONN", "1"))
          max_conn = int(os.getenv("DB_MAX_CONN", "10"))


          if not all([db_host, db_name, db_user, db_password]):
              logging.error("Error: No todas las variables de entorno de la base de datos están configuradas.")
              raise ValueError("Faltan variables de entorno de la base de datos.")


          self.connection_pool = pool.SimpleConnectionPool(
              min_conn,
              max_conn,
              host=db_host,
              database=db_name,
              user=db_user,
              password=db_password,
              port=db_port
          )

          logging.info("Pool de conexiones a la base de datos inicializado correctamente.")
      except (psycopg2.Error, ValueError) as e:
          logging.error(f"Error al inicializar el pool de conexiones: {e}")
          raise

    def get_connection(self):
        """
        Obtiene una conexión del pool de conexiones.

        Returns:
            psycopg2.extensions.connection: Una conexión a la base de datos.
        """
        if not self.connection_pool:
           self.initialize_connection_pool()
        try:
           connection = self.connection_pool.getconn()
           logging.debug("Conexión obtenida del pool.")
           return connection
        except psycopg2.Error as e:
           logging.error(f"Error al obtener una conexión del pool: {e}")
           raise

    def release_connection(self, connection):
        """
        Libera una conexión de vuelta al pool de conexiones.

        Args:
            connection (psycopg2.extensions.connection): La conexión a liberar.
        """
        try:
            self.connection_pool.putconn(connection)
            logging.debug("Conexión liberada al pool.")
        except psycopg2.Error as e:
            logging.error(f"Error al liberar la conexión al pool: {e}")

    def close_all_connections(self):
        """
        Cierra todas las conexiones en el pool.
        """
        try:
            if self.connection_pool:
               self.connection_pool.closeall()
               logging.info("Todas las conexiones del pool han sido cerradas.")
               self.connection_pool = None
        except psycopg2.Error as e:
            logging.error(f"Error al cerrar todas las conexiones: {e}")
          
