# src/community/backend/models/event.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Configuración de la base de datos (ejemplo con SQLite)
engine = create_engine('sqlite:///./community.db', connect_args={'check_same_thread': False})

Base = declarative_base()

# Definición del modelo de Evento
class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String)
    category = Column(String)

    # Clave foránea al usuario (organizador del evento)
    organizer_id = Column(Integer, ForeignKey('users.id'))
    organizer = relationship("User", back_populates="events")#Relacion con el modelo User

    def __repr__(self):
        return f"<Event(name='{self.name}', organizer_id='{self.organizer_id}')>"

# Importante: Definir la relación en el modelo User
# Ejemplo (en src/community/backend/models/user.py):
# from sqlalchemy.orm import relationship
# class User(Base):
#     ...
#     events = relationship("Event", back_populates="organizer")

Base.metadata.create_all(engine) #Crear la tabla en la base de datos

# Creación de una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ejemplo de uso (fuera de la definición del modelo):
def get_event(db: SessionLocal, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()

def create_event(db: SessionLocal, name: str, description: str, start_time: datetime, end_time: datetime, organizer_id: int, location: str = None, category: str = None):
    db_event = Event(name=name, description=description, start_time=start_time, end_time=end_time, organizer_id=organizer_id, location=location, category=category)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
  
