from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.practice import PracticeCreate, PracticeOut
from app.models.practice import PracticeSession
from app.services.pitch_service import score_audio

router = APIRouter(prefix="/practice", tags=["practice"])

@router.post("/", response_model=PracticeOut)
def submit_practice(payload: PracticeCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    pitch, rhythm, overall = score_audio(payload.audio_url)
    row = PracticeSession(
        user_id=user.id,
        lesson_id=payload.lesson_id,
        audio_url=payload.audio_url,
        pitch_score=pitch,
        rhythm_score=rhythm,
        overall_score=overall
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

@router.get("/me", response_model=list[PracticeOut])
def my_practice(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(PracticeSession).filter(PracticeSession.user_id == user.id).all()