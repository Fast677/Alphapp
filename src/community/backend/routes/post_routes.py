# src/community/backend/routes/post_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.community.backend.models import Post
from src.community.backend.models import User  # Para que una publicación tenga un autor
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

# Ruta para crear una nueva publicación
@router.post("/posts/", response_model=Post)
def create_post(post: Post, db: Session = Depends(get_db)):
    # Aquí podrías agregar lógica para verificar si el usuario existe y tiene permisos
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

# Ruta para obtener una publicación por su ID
@router.get("/posts/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

# Ruta para obtener todas las publicaciones
@router.get("/posts/", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = db.query(Post).offset(skip).limit(limit).all()
    return posts

# Ruta para actualizar una publicación por su ID
@router.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, post: Post, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    for var, value in vars(post).items():
        setattr(db_post, var, value) if value else None
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Ruta para eliminar una publicación por su ID
@router.delete("/posts/{post_id}", response_model=Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(db_post)
    db.commit()
    return db_post
