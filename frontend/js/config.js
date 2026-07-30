// Central place for backend connection settings.
// Point this at your live backend URL once it's deployed.
const API_BASE = "http://localhost:8000/api"; // FastAPI backend (see app/main.py)

// Small fetch helper used by every render block below.
async function apiGet(path) {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) throw new Error(`${path} -> ${res.status}`);
  return res.json();
}
