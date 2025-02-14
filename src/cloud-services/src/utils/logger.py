from cloud_services.src.utils.logger import Logger

# Obtener el logger
logger = Logger.get_logger()

def example_function():
  logger.debug("Este es un mensaje de debug")
  logger.info("Este es un mensaje de información")
  logger.warning("Este es un mensaje de advertencia")
  try:
    result = 1 / 0
  except Exception as e:
    logger.error(f"Ocurrió un error: {e}") # registrar un error con mensaje y la excepción
    logger.exception("Este es un error con detalles") # Registrar un error con detalle del stacktrace
  logger.critical("Este es un mensaje crítico")

example_function()
