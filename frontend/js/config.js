// Central place for backend connection settings & API bridge.
// Auto-detects custom VITE_API_URL, local dev (http://127.0.0.1:8000/api), or relative path (/api).
const API_BASE = (function() {
  if (window.VITE_API_URL) return window.VITE_API_URL;
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' || window.location.protocol === 'file:') {
    return 'http://127.0.0.1:8000/api';
  }
  return '/api';
})();

function showBackendErrorBanner(msg) {
  let banner = document.getElementById('backendErrorBanner');
  if (!banner) {
    banner = document.createElement('div');
    banner.id = 'backendErrorBanner';
    banner.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 99999;
      background: #E5484D;
      color: #FFFFFF;
      padding: 10px 16px;
      font-size: 13px;
      font-weight: 600;
      font-family: Inter, sans-serif;
      text-align: center;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
    `;
    document.body.prepend(banner);
  }
  banner.innerHTML = `<i class="ti ti-plug-off" style="font-size:16px"></i> <span>${msg || 'Unable to connect to live backend command center. Showing cached system status.'}</span>`;
  banner.style.display = 'flex';
}

function hideBackendErrorBanner() {
  const banner = document.getElementById('backendErrorBanner');
  if (banner) banner.style.display = 'none';
}

async function apiGet(endpoint) {
  const cleanEp = endpoint.startsWith('/') ? endpoint : '/' + endpoint;
  try {
    const res = await fetch(`${API_BASE}${cleanEp}`);
    if (!res.ok) {
      const errText = `HTTP ${res.status} from ${endpoint}`;
      showBackendErrorBanner(`Backend API Error (${res.status}) on ${endpoint}`);
      throw new Error(errText);
    }
    hideBackendErrorBanner();
    return await res.json();
  } catch (err) {
    showBackendErrorBanner(`Unable to connect to live backend at ${API_BASE}`);
    throw err;
  }
}

async function apiPost(endpoint, body) {
  const cleanEp = endpoint.startsWith('/') ? endpoint : '/' + endpoint;
  try {
    const res = await fetch(`${API_BASE}${cleanEp}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });
    if (!res.ok) {
      const errText = `HTTP ${res.status} from ${endpoint}`;
      showBackendErrorBanner(`Backend POST Error (${res.status}) on ${endpoint}`);
      throw new Error(errText);
    }
    hideBackendErrorBanner();
    return await res.json();
  } catch (err) {
    showBackendErrorBanner(`Unable to post data to live backend at ${API_BASE}`);
    throw err;
  }
}
