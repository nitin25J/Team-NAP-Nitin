// Renders Emergency Alert cards from ALERTS (fetched from /alerts/active) and
// keeps each countdown timer ticking down every second (derived from the
// backend's issued_at/valid_until timestamps).
const alertsGrid = document.getElementById('alertsGrid');

function formatCountdown(totalSeconds){
  const h = Math.floor(totalSeconds / 3600);
  const m = Math.floor((totalSeconds % 3600) / 60);
  const s = totalSeconds % 60;
  return [h, m, s].map(n => String(n).padStart(2, '0')).join(':');
}

function renderAlertsGrid(){
  if (!alertsGrid) return;
  alertsGrid.innerHTML = ALERTS.map((a, i)=>{
    const isCritical = (a.severity || '').toLowerCase() === 'critical' || (a.severity || '').toLowerCase() === 'severe';
    const endsIn = Math.max(0, Math.round((new Date(a.valid_until).getTime() - Date.now()) / 1000));
    const confidence = a._predictedConfidence != null ? `${a._predictedConfidence}%` : '—';
    return `
      <div class="card hoverable alert-card ${isCritical ? '' : 'warning'}">
        <div class="alert-top">
          <div>
            <span class="tag ${isCritical ? 'critical' : 'moderate'}">${a.severity}</span>
            <div class="alert-title" style="margin-top:8px">${a.type} — ${a.district}${a.river ? ' · ' + a.river : ''}</div>
          </div>
          <div class="countdown" data-remaining="${endsIn}" id="countdown-${i}">${formatCountdown(endsIn)}</div>
        </div>
        <div class="alert-meta">
          <span>Districts: <b>${a.district}</b></span>
          <span>Issued by: <b>${a.issued_by || '—'}</b></span>
          <span>AI confidence: <b>${confidence}</b></span>
        </div>
        <div style="font-size:12px;color:var(--text-dim);margin-top:10px">${a.message || ''}</div>
        <button class="btn ${isCritical ? 'danger' : 'primary'}" style="margin-top:14px">
          <i class="ti ti-broadcast"></i>${isCritical ? 'Escalate now' : 'Review advisory'}
        </button>
      </div>`;
  }).join('');

  clearInterval(window._alertCountdownTimer);
  window._alertCountdownTimer = setInterval(()=>{
    document.querySelectorAll('.countdown').forEach(el=>{
      let remaining = Number(el.dataset.remaining) - 1;
      if (remaining < 0) remaining = 0;
      el.dataset.remaining = remaining;
      el.textContent = formatCountdown(remaining);
    });
  }, 1000);
}
