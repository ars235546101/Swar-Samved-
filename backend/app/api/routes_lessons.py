from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.lesson import Lesson
from app.schemas.lesson import LessonCreate, LessonOut

router = APIRouter(prefix="/lessons", tags=["lessons"])

@router.get("/", response_model=list[LessonOut])
def list_lessons(db: Session = Depends(get_db)):
    return db.query(Lesson).all()

@router.post("/", response_model=LessonOut)
def create_lesson(payload: LessonCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create lessons")
    lesson = Lesson(**payload.model_dump())
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return lesson