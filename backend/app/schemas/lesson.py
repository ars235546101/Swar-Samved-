from pydantic import BaseModel

class LessonCreate(BaseModel):
    title: str
    level: str
    raga: str = ""
    description: str = ""
    reference_audio_url: str = ""

class LessonOut(LessonCreate):
    id: int
    class Config:
        from_attributes = True