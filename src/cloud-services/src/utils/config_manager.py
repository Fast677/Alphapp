# cloud-services/src/utils/config_manager.py

import os
import configparser
from cloud_services.src.utils.logger import Logger

class ConfigManager:
    """
    Clase para gestionar la configuración de la aplicación.
    """
    _instance = None
    _config = None
    _logger = None

    def __new__(cls):
        """
        Implementa el patrón Singleton para asegurar que solo exista una instancia de ConfigManager.
        """
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._logger = Logger.get_logger()
            cls._instance._config = cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        """
        Carga la configuración desde un archivo INI y variables de entorno.
        
        Returns:
            configparser.ConfigParser: El objeto configparser con la configuración cargada.
        """
        config = configparser.ConfigParser()
        
        # Obtener la ruta del directorio config
        config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'config')
        
        # Archivos de configuración por defecto
        default_config_files = ['default.ini']

        # Archivo de configuración específico del entorno
        environment = os.getenv('ENVIRONMENT', 'development')
        env_config_file = f'{environment}.ini'
        
        config_files = default_config_files + [env_config_file]
        
        # Cargar archivos de configuración, si existen
        for config_file in config_files:
          full_config_path = os.path.join(config_dir, config_file)
          if os.path.exists(full_config_path):
            try:
              config.read(full_config_path)
              self._logger.info(f"Configuración cargada desde '{full_config_path}'")
            except Exception as e:
              self._logger.error(f"Error al cargar el archivo de configuración '{full_config_path}': {e}")

        # Cargar variables de entorno, sobreescribiendo los valores de config
        for section in config.sections():
            for key in config[section]:
                env_var_name = f'{section.upper()}_{key.upper()}'
                env_var_value = os.getenv(env_var_name)
                if env_var_value:
                   try:
                      config[section][key] = env_var_value
                      self._logger.info(f"Variable de entorno '{env_var_name}' cargada, sobreescribiendo '{key}' en la sección '{section}'")
                   except Exception as e:
                       self._logger.error(f"Error al procesar variable de entorno '{env_var_name}': {e}")
        
        return config

    def get(self, section, key, default=None):
        """
        Obtiene un valor de configuración.
        
        Args:
            section (str): La sección del archivo de configuración.
            key (str): La clave dentro de la sección.
            default (any): Valor por defecto si la clave no se encuentra.
            
        Returns:
            str: El valor de configuración, o el valor por defecto si no se encuentra.
        """
        try:
            return self._config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            if default is not None:
              self._logger.warning(f"Clave '{key}' no encontrada en sección '{section}'. Retornando valor por defecto.")
              return default
            self._logger.error(f"Clave '{key}' no encontrada en sección '{section}'. No se ha proporcionado valor por defecto.")
            return None
    
    def get_int(self, section, key, default=None):
      """
      Obtiene un valor de configuración como entero.
      
      Args:
        section (str): La sección del archivo de configuración.
        key (str): La clave dentro de la sección.
        default (int): Valor por defecto si la clave no se encuentra.
      
      Returns:
        int: El valor de configuración como entero, o el valor por defecto si no se encuentra.
      """
      try:
          return self._config.getint(section, key)
      except (configparser.NoSectionError, configparser.NoOptionError):
          if default is not None:
            self._logger.warning(f"Clave '{key}' no encontrada en sección '{section}'. Retornando valor por defecto.")
            return default
          self._logger.error(f"Clave '{key}' no encontrada en sección '{section}'. No se ha proporcionado valor por defecto.")
          return None
    
    def get_boolean(self, section, key, default=None):
      """
      Obtiene un valor de configuración como booleano.
        
      Args:
        section (str): La sección del archivo de configuración.
        key (str): La clave dentro de la sección.
        default (bool): Valor por defecto si la clave no se encuentra.
        
      Returns:
        bool: El valor de configuración como booleano, o el valor por defecto si no se encuentra.
      """
      try:
          return self._config.getboolean(section, key)
      except (configparser.NoSectionError, configparser.NoOptionError):
        if default is not None:
          self._logger.warning(f"Clave '{key}' no encontrada en sección '{section}'. Retornando valor por defecto.")
          return default
        self._logger.error(f"Clave '{key}' no encontrada en sección '{section}'. No se ha proporcionado valor por defecto.")
        return None
