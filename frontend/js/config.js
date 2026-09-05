// Central place for backend connection settings.
// Auto-detects local backend (http://127.0.0.1:8000/api), Vercel serverless (/api), or custom VITE_API_URL.
const API_BASE = (function() {
  if (window.VITE_API_URL) return window.VITE_API_URL;
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    return 'http://127.0.0.1:8000/api';
  }
  return '/api';
})();

async function apiGet(endpoint) {
  const cleanEp = endpoint.startsWith('/') ? endpoint : '/' + endpoint;
  const res = await fetch(`${API_BASE}${cleanEp}`);
  if (!res.ok) throw new Error(`HTTP ${res.status} from ${endpoint}`);
  return await res.json();
}

async function apiPost(endpoint, body) {
  const cleanEp = endpoint.startsWith('/') ? endpoint : '/' + endpoint;
  const res = await fetch(`${API_BASE}${cleanEp}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  });
  if (!res.ok) throw new Error(`HTTP ${res.status} from ${endpoint}`);
  return await res.json();
}

