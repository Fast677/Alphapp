# src/community/backend/models/resource.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Configuración de la base de datos (ejemplo con SQLite)
engine = create_engine('sqlite:///./community.db', connect_args={'check_same_thread': False})

Base = declarative_base()

# Definición del modelo de Recurso
class Resource(Base):
    __tablename__ = 'resources'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    resource_type = Column(String, nullable=False) # Ej: "tutorial", "documentación", "plantilla"
    url = Column(String, nullable=True) # Si el recurso es un link externo
    file_path = Column(String, nullable=True) # Si el recurso es un archivo subido
    publication_date = Column(DateTime, default=datetime.utcnow)
    tags = Column(String, nullable=True) # Ej: "python", "react", "api"
    category = Column(String, nullable=True)

    # Clave foránea al usuario (autor del recurso)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="resources") # Relación con el modelo User

    def __repr__(self):
        return f"<Resource(title='{self.title}', author_id='{self.author_id}')>"

# Importante: Definir la relación en el modelo User
# Ejemplo (en src/community/backend/models/user.py):
# from sqlalchemy.orm import relationship
# class User(Base):
#     ...
#     resources = relationship("Resource", back_populates="author")

Base.metadata.create_all(engine) # Crear la tabla en la base de datos

# Creación de una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ejemplo de uso (fuera de la definición del modelo):
def get_resource(db: SessionLocal, resource_id: int):
    return db.query(Resource).filter(Resource.id == resource_id).first()

def create_resource(db: SessionLocal, title: str, description: str, resource_type: str, author_id: int, url: str = None, file_path: str = None, tags: str = None, category: str = None):
    db_resource = Resource(title=title, description=description, resource_type=resource_type, author_id=author_id, url=url, file_path=file_path, tags=tags, category=category)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource
