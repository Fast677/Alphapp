# cloud-services/src/utils/error_handler.py

import logging
from flask import jsonify

class ErrorHandler:
    """
    Clase para manejar errores de manera centralizada.
    """
    @staticmethod
    def handle_error(e, status_code=500):
        """
        Maneja excepciones y retorna una respuesta JSON con el error.

        Args:
            e (Exception): La excepción ocurrida.
            status_code (int): Código de estado HTTP a retornar.

        Returns:
            flask.Response: Respuesta JSON con el error y el código de estado.
        """
        logging.exception(f"Error: {e}") # Registra la excepción con detalles
        return jsonify(
            {
                "error": {
                    "message": str(e),
                    "type": e.__class__.__name__,
                }
            }
        ), status_code


    @staticmethod
    def handle_404_error(e):
        """
        Maneja errores 404 (Recurso no encontrado).

        Args:
            e (Exception): La excepción 404.

        Returns:
            flask.Response: Respuesta JSON con el error 404.
        """
        logging.warning(f"Recurso no encontrado: {e}")
        return jsonify(
            {
                "error": {
                    "message": "Recurso no encontrado",
                    "type": "NotFound",
                }
            }
        ), 404


    @staticmethod
    def handle_400_error(e):
        """
        Maneja errores 400 (Solicitud incorrecta).

        Args:
            e (Exception): La excepción 400.

        Returns:
            flask.Response: Respuesta JSON con el error 400.
        """
        logging.warning(f"Solicitud incorrecta: {e}")
        return jsonify(
            {
                "error": {
                    "message": str(e),
                    "type": "BadRequest",
                }
            }
        ), 400

    @staticmethod
    def handle_custom_error(message, status_code=500, error_type="CustomError"):
      """
        Maneja errores personalizados con un mensaje específico.

        Args:
            message (str): El mensaje de error personalizado.
            status_code (int): Código de estado HTTP a retornar.
            error_type (str): El tipo de error personalizado.

        Returns:
            flask.Response: Respuesta JSON con el error personalizado y el código de estado.
        """
      logging.error(f"Error personalizado: {message}, type: {error_type}")
      return jsonify(
          {
              "error": {
                  "message": message,
                  "type": error_type,
              }
          }
      ), status_code
