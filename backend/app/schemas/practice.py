from pydantic import BaseModel

class PracticeCreate(BaseModel):
    lesson_id: int
    audio_url: str

class PracticeOut(BaseModel):
    id: int
    lesson_id: int
    audio_url: str
    pitch_score: float
    rhythm_score: float
    overall_score: float

    class Config:
        from_attributes = True