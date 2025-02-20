# src/community/backend/models/comment.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Configuración de la base de datos (ejemplo con SQLite)
engine = create_engine('sqlite:///./community.db', connect_args={'check_same_thread': False})

Base = declarative_base()

# Definición del modelo de Comentario
class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)

    # Clave foránea al usuario (autor del comentario)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="comments")#Relacion con el modelo User

    # Clave foránea a la publicación (a qué publicación pertenece el comentario)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship("Post", back_populates="comments")#Relacion con el modelo Post


    def __repr__(self):
        return f"<Comment(content='{self.content}', author_id='{self.author_id}', post_id='{self.post_id}')>"

# Importante:  Definir la relación en el modelo User
# Ejemplo (en src/community/backend/models/user.py):
# from sqlalchemy.orm import relationship
# class User(Base):
#     ...
#     comments = relationship("Comment", back_populates="author")

# Importante:  Definir la relación en el modelo Post
# Ejemplo (en src/community/backend/models/post.py):
# from sqlalchemy.orm import relationship
# class Post(Base):
#     ...
#     comments = relationship("Comment", back_populates="post")

Base.metadata.create_all(engine) #Crear la tabla en la base de datos

# Creación de una sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ejemplo de uso (fuera de la definición del modelo):
def get_comment(db: SessionLocal, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def create_comment(db: SessionLocal, content: str, author_id: int, post_id: int):
    db_comment = Comment(content=content, author_id=author_id, post_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
