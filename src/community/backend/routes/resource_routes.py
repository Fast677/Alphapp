# src/community/backend/routes/resource_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.community.backend.models import Resource
from src.community.backend.models import User #Para que un recurso tenga un dueño
from src.community.backend.models import SessionLocal #Para la base de datos
from typing import List

router = APIRouter()

# Dependency para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo recurso
@router.post("/resources/", response_model=Resource)
def create_resource(resource: Resource, db: Session = Depends(get_db)):
    db_resource = db.query(Resource).filter(Resource.name == resource.name).first()
    if db_resource:
        raise HTTPException(status_code=400, detail="Resource already registered")
    db.add(resource)
    db.commit()
    db.refresh(resource)
    return resource

# Ruta para obtener un recurso por su ID
@router.get("/resources/{resource_id}", response_model=Resource)
def read_resource(resource_id: int, db: Session = Depends(get_db)):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return db_resource

# Ruta para obtener todos los recursos
@router.get("/resources/", response_model=List[Resource])
def read_resources(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    resources = db.query(Resource).offset(skip).limit(limit).all()
    return resources

# Ruta para actualizar un recurso por su ID
@router.put("/resources/{resource_id}", response_model=Resource)
def update_resource(resource_id: int, resource: Resource, db: Session = Depends(get_db)):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    for var, value in vars(resource).items():
        setattr(db_resource, var, value) if value else None
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

# Ruta para eliminar un recurso por su ID
@router.delete("/resources/{resource_id}", response_model=Resource)
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    db_resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    db.delete(db_resource)
    db.commit()
    return db_resource
