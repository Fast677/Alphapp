# src/community/backend/routes/event_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.community.backend.models import Event
from src.community.backend.models import User  # Para que un evento tenga un organizador
from src.community.backend.models import SessionLocal  # Para la base de datos
from typing import List

router = APIRouter()

# Dependency para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un nuevo evento
@router.post("/events/", response_model=Event)
def create_event(event: Event, db: Session = Depends(get_db)):
    # Aquí podrías agregar lógica para verificar si el usuario existe y tiene permisos
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

# Ruta para obtener un evento por su ID
@router.get("/events/{event_id}", response_model=Event)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

# Ruta para obtener todos los eventos
@router.get("/events/", response_model=List[Event])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = db.query(Event).offset(skip).limit(limit).all()
    return events

# Ruta para actualizar un evento por su ID
@router.put("/events/{event_id}", response_model=Event)
def update_event(event_id: int, event: Event, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    for var, value in vars(event).items():
        setattr(db_event, var, value) if value else None
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

# Ruta para eliminar un evento por su ID
@router.delete("/events/{event_id}", response_model=Event)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()
    return db_event
