import axios from "axios";

export const api = axios.create({
  baseURL: "http://localhost:8000",
});

export function setToken(token: string) {
  localStorage.setItem("token", token);
  api.defaults.headers.common.Authorization = `Bearer ${token}`;
}

export function loadToken() {
  const t = localStorage.getItem("token");
  if (t) api.defaults.headers.common.Authorization = `Bearer ${t}`;
}