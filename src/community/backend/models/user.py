# src/community/backend/models/user.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Configuración de la base de datos (ejemplo con SQLite)
engine = create_engine('sqlite:///./community.db', connect_args={'check_same_thread': False})

Base = declarative_base()

# Definición del modelo de Usuario
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False) #**Importante: Almacenar contraseñas de forma segura**
    registration_date = Column(DateTime, default=datetime.utcnow)
    role = Column(String, default="user") # Ejemplo: user, moderator, admin
    # Otros campos relevantes:
    # - bio: Biografía del usuario
    # - profile_picture: Enlace a la imagen de perfil

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}', role='{self.role}')>"

Base.metadata.create_all(engine) #Crear la tabla en la base de datos

# Creación de una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ejemplo de uso (fuera de la definición del modelo):
def get_user(db: SessionLocal, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: SessionLocal, name: str, email: str, hashed_password: str):
    db_user = User(name=name, email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
