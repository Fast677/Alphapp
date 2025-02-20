# src/community/backend/routes/__init__.py
from fastapi import FastAPI

from . import comment_routes
from . import user_routes  # Ejemplo: si también tuvieras rutas de usuario
# Importa aquí otros módulos de rutas según sea necesario

def include_routes(app: FastAPI):
    app.include_router(comment_routes.router, prefix="/community", tags=["comments"])
    # app.include_router(user_routes.router, prefix="/community", tags=["users"]) # Si tuvieras rutas de usuario
    # Incluye aquí otros routers según sea necesario
