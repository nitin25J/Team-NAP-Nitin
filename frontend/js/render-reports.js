// Renders the Citizen Reports grid from REPORTS (see mock-data.js)

window.renderReportsGrid = function() {
  const reportsGrid = document.getElementById('reportsGrid');
  if (!reportsGrid) return;
  const list = window.REPORTS || [];

  reportsGrid.innerHTML = list.map(r => `
    <div class="card hoverable report-card">
      <div class="report-media" style="background:linear-gradient(180deg,rgba(7,15,23,.05) 55%,rgba(7,15,23,.88) 100%),url('${r.image || 'https://images.unsplash.com/photo-1657069343871-fd1476990d04?auto=format&fit=crop&w=1200&q=80'}') center/cover no-repeat;">
        ${r.verified || r.media_attached ? '<span class="verified-badge"><i class="ti ti-rosette-discount-check"></i>AI verified</span>' : ''}
      </div>
      <div class="report-user">
        <div class="ru-avatar"><i class="ti ti-user"></i></div>
        <div>
          <div style="font-size:12.5px;font-weight:600">${r.user || r.reporter_name || 'Citizen Reporter'}</div>
          <div style="font-size:10.5px;color:var(--text-faint)">${r.time || 'Just now'}</div>
        </div>
      </div>
      <div style="font-size:12.5px;color:var(--text-dim);display:flex;align-items:center;gap:5px;margin-bottom:8px">
        <i class="ti ti-map-pin" style="font-size:13px"></i>${r.location || r.district || 'Assam Command'}
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center">
        <span class="tag ${r.severity === 'critical' || r.severity === 'Critical' ? 'critical' : 'moderate'}">${r.severity || 'Moderate'}</span>
        <span style="font-size:11px;color:var(--text-faint)">${r.status || 'Verified'}</span>
      </div>
    </div>`).join('');
};

document.addEventListener('DOMContentLoaded', () => {
  if (window.renderReportsGrid) window.renderReportsGrid();
});

