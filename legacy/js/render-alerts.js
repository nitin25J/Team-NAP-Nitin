// Renders Emergency Alert cards from ALERTS (see mock-data.js) and keeps
// each countdown timer ticking down every second.

function formatCountdown(totalSeconds) {
  if (!totalSeconds || isNaN(totalSeconds)) return '00:00:00';
  const h = Math.floor(totalSeconds / 3600);
  const m = Math.floor((totalSeconds % 3600) / 60);
  const s = totalSeconds % 60;
  return [h, m, s].map(n => String(n).padStart(2, '0')).join(':');
}

window.renderAlertsGrid = function() {
  const alertsGrid = document.getElementById('alertsGrid');
  if (!alertsGrid) return;
  const list = window.ALERTS || [];

  alertsGrid.innerHTML = list.map((a, i) => {
    const isCritical = a.level === 'critical' || a.severity === 'critical';
    const ends = a.endsIn || 10800;
    return `
      <div class="card hoverable alert-card ${isCritical ? '' : 'warning'}">
        <div class="alert-top">
          <div>
            <span class="tag ${isCritical ? 'critical' : 'moderate'}">${isCritical ? 'Critical' : 'Warning'}</span>
            <div class="alert-title" style="margin-top:8px">${a.title || a.message || 'Disaster Advisory'}</div>
          </div>
          <div class="countdown" data-remaining="${ends}" id="countdown-${i}">${formatCountdown(ends)}</div>
        </div>
        <div class="alert-meta">
          <span>Districts: <b>${a.districts || a.district || 'Assam Sector'}</b></span>
          <span>Population: <b>${a.population || 'Affected area'}</b></span>
          <span>AI confidence: <b>${a._predictedConfidence ?? a.confidence ?? 85}%</b></span>
        </div>
        <button class="btn ${isCritical ? 'danger' : 'primary'}" style="margin-top:14px">
          <i class="ti ti-broadcast"></i>${isCritical ? 'Escalate now' : 'Review advisory'}
        </button>
      </div>`;
  }).join('');
};

document.addEventListener('DOMContentLoaded', () => {
  if (window.renderAlertsGrid) window.renderAlertsGrid();

  setInterval(() => {
    document.querySelectorAll('.countdown').forEach(el => {
      let remaining = Number(el.dataset.remaining) - 1;
      if (remaining < 0) remaining = 0;
      el.dataset.remaining = remaining;
      el.textContent = formatCountdown(remaining);
    });
  }, 1000);
});

