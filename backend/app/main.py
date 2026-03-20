from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.api.routes_auth import router as auth_router
from app.api.routes_lessons import router as lessons_router
from app.api.routes_practice import router as practice_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Music Tutor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(lessons_router)
app.include_router(practice_router)

@app.get("/health")
def health():
    return {"ok": True}