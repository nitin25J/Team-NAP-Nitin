// Renders Emergency Alert cards from ALERTS (see mock-data.js) and keeps
// each countdown timer ticking down every second.
const alertsGrid = document.getElementById('alertsGrid');

function formatCountdown(totalSeconds){
  const h = Math.floor(totalSeconds / 3600);
  const m = Math.floor((totalSeconds % 3600) / 60);
  const s = totalSeconds % 60;
  return [h, m, s].map(n => String(n).padStart(2, '0')).join(':');
}

if (alertsGrid) {
  alertsGrid.innerHTML = ALERTS.map((a, i)=>{
    const isCritical = a.level === 'critical';
    return `
      <div class="card hoverable alert-card ${isCritical ? '' : 'warning'}">
        <div class="alert-top">
          <div>
            <span class="tag ${isCritical ? 'critical' : 'moderate'}">${isCritical ? 'Critical' : 'Warning'}</span>
            <div class="alert-title" style="margin-top:8px">${a.title}</div>
          </div>
          <div class="countdown" data-remaining="${a.endsIn}" id="countdown-${i}">${formatCountdown(a.endsIn)}</div>
        </div>
        <div class="alert-meta">
          <span>Districts: <b>${a.districts}</b></span>
          <span>Population: <b>${a.population}</b></span>
          <span>AI confidence: <b>${a.confidence}%</b></span>
        </div>
        <button class="btn ${isCritical ? 'danger' : 'primary'}" style="margin-top:14px">
          <i class="ti ti-broadcast"></i>${isCritical ? 'Escalate now' : 'Review advisory'}
        </button>
      </div>`;
  }).join('');

  setInterval(()=>{
    document.querySelectorAll('.countdown').forEach(el=>{
      let remaining = Number(el.dataset.remaining) - 1;
      if (remaining < 0) remaining = 0;
      el.dataset.remaining = remaining;
      el.textContent = formatCountdown(remaining);
    });
  }, 1000);
}
