import { useState } from "react";
import { api, setToken } from "../api";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const nav = useNavigate();
  const [full_name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    const res = await api.post("/auth/register", { full_name, email, password });
    setToken(res.data.access_token);
    nav("/");
  }

  return (
    <form onSubmit={submit}>
      <h2>Register</h2>
      <input placeholder="Full name" value={full_name} onChange={e => setName(e.target.value)} /><br />
      <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} /><br />
      <input placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} /><br />
      <button type="submit">Create account</button>
    </form>
  );
}