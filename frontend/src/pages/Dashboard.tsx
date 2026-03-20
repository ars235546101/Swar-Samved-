import { useEffect, useState } from "react";
import { api } from "../api";

type Lesson = { id: number; title: string; level: string; raga: string; description: string; reference_audio_url: string; };
type Practice = { id: number; lesson_id: number; audio_url: string; pitch_score: number; rhythm_score: number; overall_score: number; };

export default function Dashboard() {
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [practice, setPractice] = useState<Practice[]>([]);
  const [lessonId, setLessonId] = useState<number>(0);
  const [audioUrl, setAudioUrl] = useState("");

  async function load() {
    const l = await api.get("/lessons");
    setLessons(l.data);
    try {
      const p = await api.get("/practice/me");
      setPractice(p.data);
    } catch {}
  }

  async function submitPractice() {
    await api.post("/practice", { lesson_id: lessonId, audio_url: audioUrl });
    setAudioUrl("");
    load();
  }

  useEffect(() => { load(); }, []);

  return (
    <div>
      <h2>Lessons</h2>
      <ul>
        {lessons.map(l => <li key={l.id}>{l.title} ({l.level}) - {l.raga}</li>)}
      </ul>

      <h2>Submit Practice</h2>
      <select onChange={e => setLessonId(Number(e.target.value))} defaultValue="">
        <option value="" disabled>Select lesson</option>
        {lessons.map(l => <option key={l.id} value={l.id}>{l.title}</option>)}
      </select>
      <input placeholder="Audio URL" value={audioUrl} onChange={e => setAudioUrl(e.target.value)} />
      <button onClick={submitPractice}>Submit</button>

      <h2>My Scores</h2>
      <ul>
        {practice.map(p => (
          <li key={p.id}>
            Lesson #{p.lesson_id} | Pitch: {p.pitch_score} | Rhythm: {p.rhythm_score} | Overall: {p.overall_score}
          </li>
        ))}
      </ul>
    </div>
  );
}