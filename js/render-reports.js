// Renders the Citizen Reports grid from REPORTS (see mock-data.js)
const reportsGrid = document.getElementById('reportsGrid');

if (reportsGrid) {
  reportsGrid.innerHTML = REPORTS.map(r=>`
    <div class="card hoverable report-card">
      <div class="report-media" style="background:linear-gradient(180deg,rgba(7,15,23,.05) 55%,rgba(7,15,23,.88) 100%),url('${r.image}') center/cover no-repeat;">
        ${r.verified ? '<span class="verified-badge"><i class="ti ti-rosette-discount-check"></i>AI verified</span>' : ''}
      </div>
      <div class="report-user">
        <div class="ru-avatar"><i class="ti ti-user"></i></div>
        <div>
          <div style="font-size:12.5px;font-weight:600">${r.user}</div>
          <div style="font-size:10.5px;color:var(--text-faint)">${r.time}</div>
        </div>
      </div>
      <div style="font-size:12.5px;color:var(--text-dim);display:flex;align-items:center;gap:5px;margin-bottom:8px">
        <i class="ti ti-map-pin" style="font-size:13px"></i>${r.location}
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center">
        <span class="tag ${r.severity === 'critical' ? 'critical' : 'moderate'}">${r.severity}</span>
        <span style="font-size:11px;color:var(--text-faint)">${r.status}</span>
      </div>
    </div>`).join('');
}
