# src/utils/data_validator.py

import re
import logging

def validate_email(email):
    """
    Valida si una cadena de texto tiene el formato de un correo electrónico.

    Args:
        email (str): La cadena de texto a validar.

    Returns:
        bool: True si el correo electrónico es válido, False en caso contrario.
    """
    if not isinstance(email, str):
      logging.error(f"Error: El email debe ser una cadena de texto: {email}")
      return False

    # Patrón regex para validar un email (simple)
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
      logging.error(f"Error: El email no tiene un formato valido: {email}")
      return False


def validate_password(password):
    """
    Valida si una cadena de texto cumple con criterios mínimos de seguridad para una contraseña.
    La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número.

    Args:
        password (str): La cadena de texto a validar.

    Returns:
        bool: True si la contraseña es válida, False en caso contrario.
    """
    if not isinstance(password, str):
      logging.error("Error: La contraseña debe ser una cadena de texto.")
      return False

    if len(password) < 8:
        logging.error("Error: La contraseña debe tener al menos 8 caracteres.")
        return False
    if not re.search("[a-z]", password):
        logging.error("Error: La contraseña debe tener al menos una letra minúscula.")
        return False
    if not re.search("[A-Z]", password):
        logging.error("Error: La contraseña debe tener al menos una letra mayúscula.")
        return False
    if not re.search("[0-9]", password):
        logging.error("Error: La contraseña debe tener al menos un número.")
        return False
    return True


def validate_non_empty_string(text, field_name="campo"):
    """
    Valida si una cadena de texto no está vacía después de eliminar espacios en blanco al inicio y al final.

    Args:
        text (str): La cadena de texto a validar.
        field_name (str): El nombre del campo que se valida.

    Returns:
        bool: True si la cadena no está vacía, False en caso contrario.
    """
    if not isinstance(text, str):
      logging.error(f"Error: El {field_name} debe ser una cadena de texto: {text}")
      return False
    if not text.strip():
        logging.error(f"Error: El {field_name} no puede estar vacio: {text}")
        return False
    return True


def validate_integer(value, field_name="campo"):
    """
    Valida si un valor es un número entero.

    Args:
        value (any): El valor a validar.
        field_name (str): El nombre del campo que se valida.
    Returns:
        bool: True si el valor es un entero, False en caso contrario.
    """
    if not isinstance(value, int):
        logging.error(f"Error: El {field_name} debe ser un número entero: {value}")
        return False
    return True


def validate_float(value, field_name="campo"):
    """
    Valida si un valor es un número de punto flotante.

    Args:
        value (any): El valor a validar.
        field_name (str): El nombre del campo que se valida.
    Returns:
        bool: True si el valor es un número de punto flotante, False en caso contrario.
    """
    if not isinstance(value, float):
      logging.error(f"Error: El {field_name} debe ser un número de punto flotante: {value}")
      return False
    return True

def validate_date(date_text, field_name="campo"):
    """
    Valida si una cadena de texto tiene el formato de una fecha (YYYY-MM-DD).
        
    Args:
        date_text (str): La cadena de texto a validar.
        field_name (str): El nombre del campo que se valida.
    Returns:
        bool: True si la cadena es una fecha válida, False en caso contrario.
    """
    if not isinstance(date_text, str):
        logging.error(f"Error: El {field_name} debe ser una cadena de texto: {date_text}")
        return False

    try:
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_text):
            logging.error(f"Error: El {field_name} no tiene el formato correcto (YYYY-MM-DD): {date_text}")
            return False
        year, month, day = map(int, date_text.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
           logging.error(f"Error: El {field_name} no tiene una fecha válida: {date_text}")
           return False
        return True
    except ValueError:
        logging.error(f"Error: El {field_name} no tiene un formato de fecha válido: {date_text}")
        return False
