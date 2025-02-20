# src/community/backend/routes/comment_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.community.backend.models import Comment
from src.community.backend.models import User  # Para que un comentario tenga un autor
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

# Ruta para crear un nuevo comentario
@router.post("/comments/", response_model=Comment)
def create_comment(comment: Comment, db: Session = Depends(get_db)):
    # Aquí podrías agregar lógica para verificar si el usuario existe y tiene permisos
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

# Ruta para obtener un comentario por su ID
@router.get("/comments/{comment_id}", response_model=Comment)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

# Ruta para obtener todos los comentarios
@router.get("/comments/", response_model=List[Comment])
def read_comments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = db.query(Comment).offset(skip).limit(limit).all()
    return comments

# Ruta para actualizar un comentario por su ID
@router.put("/comments/{comment_id}", response_model=Comment)
def update_comment(comment_id: int, comment: Comment, db: Session = Depends(get_db)):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    for var, value in vars(comment).items():
        setattr(db_comment, var, value) if value else None
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# Ruta para eliminar un comentario por su ID
@router.delete("/comments/{comment_id}", response_model=Comment)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    db.delete(db_comment)
    db.commit()
    return db_comment
