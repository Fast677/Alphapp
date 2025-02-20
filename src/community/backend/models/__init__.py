# src/community/backend/models/__init__.py

from .user import User
from .resource import Resource
# Aquí se pueden añadir más importaciones de otros modelos

__all__ = ['User', 'Resource'] # Opcional: Define qué nombres se exportan al usar from models import *
