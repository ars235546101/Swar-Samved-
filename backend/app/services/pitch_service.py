import random

def score_audio(audio_url: str) -> tuple[float, float, float]:
    # Placeholder scoring; replace with librosa-based analysis
    pitch = round(random.uniform(60, 95), 2)
    rhythm = round(random.uniform(55, 95), 2)
    overall = round((pitch + rhythm) / 2, 2)
    return pitch, rhythm, overall