# src/community/backend/models/post.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Configuración de la base de datos (ejemplo con SQLite)
engine = create_engine('sqlite:///./community.db', connect_args={'check_same_thread': False})

Base = declarative_base()

# Definición del modelo de Publicación
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    category = Column(String)

    # Clave foránea al usuario (autor de la publicación)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")#Relacion con el modelo User

    #Relación con el modelo Comment
    comments = relationship("Comment", back_populates="post")

    def __repr__(self):
        return f"<Post(title='{self.title}', author_id='{self.author_id}')>"

# Importante: Definir la relación en el modelo User
# Ejemplo (en src/community/backend/models/user.py):
# from sqlalchemy.orm import relationship
# class User(Base):
#     ...
#     posts = relationship("Post", back_populates="author")

Base.metadata.create_all(engine) #Crear la tabla en la base de datos

# Creación de una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ejemplo de uso (fuera de la definición del modelo):
def get_post(db: SessionLocal, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def create_post(db: SessionLocal, title: str, content: str, author_id: int, category: str = None):
    db_post = Post(title=title, content=content, author_id=author_id, category=category)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
