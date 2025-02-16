# cloud-services/scripts/utils/log_utils.py
import logging
import logging.config
import os

# Definir el nivel de registro por defecto
DEFAULT_LOG_LEVEL = logging.INFO

def configure_logging(log_level=None, log_file=None):
    """
    Configura el sistema de registro.

    Args:
        log_level (int, opcional): Nivel de registro. Por defecto, logging.INFO.
        log_file (str, opcional): Ruta al archivo de registro. Si no se especifica,
                                  se registra en la salida estándar.
    """
    if log_level is None:
        log_level = DEFAULT_LOG_LEVEL

    # Crear el logger principal
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Crear el formateador
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Crear el manejador (handler)
    if log_file:
        # Si se especifica un archivo de registro, usar un FileHandler
        handler = logging.FileHandler(log_file)
    else:
        # Si no, usar un StreamHandler para la salida estándar
        handler = logging.StreamHandler()

    handler.setFormatter(formatter)

    # Añadir el manejador al logger
    logger.addHandler(handler)

    return logger

def get_logger(name):
    """
    Obtiene un logger con el nombre especificado.

    Args:
        name (str): El nombre del logger.

    Returns:
        logging.Logger: El logger configurado.
    """
    return logging.getLogger(name)

# Ejemplo de uso
if __name__ == "__main__":
    # Configurar el logging
    logger = configure_logging(log_level=logging.DEBUG, log_file='app.log')

    # Obtener un logger específico para este módulo
    module_logger = get_logger(__name__)

    # Registrar mensajes de diferentes niveles
    logger.debug("Este es un mensaje de depuración")
    logger.info("Este es un mensaje informativo")
    logger.warning("Esta es una advertencia")
    logger.error("Este es un error")
    logger.critical("Este es un error crítico")

    module_logger.info("Mensaje desde el logger del módulo")
