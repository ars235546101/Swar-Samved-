import { useState } from "react";
import { api, setToken } from "../api";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const nav = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    const res = await api.post("/auth/login", { email, password });
    setToken(res.data.access_token);
    nav("/");
  }

  return (
    <form onSubmit={submit}>
      <h2>Login</h2>
      <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} /><br />
      <input placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} /><br />
      <button type="submit">Login</button>
    </form>
  );
}