// Renders the Rescue Teams grid from RESCUE_TEAMS (see mock-data.js)
const rescueGrid = document.getElementById('rescueGrid');

if (rescueGrid) {
  rescueGrid.innerHTML = RESCUE_TEAMS.map(t=>{
    const deployed = t.status === 'deployed';
    return `
      <div class="card hoverable res-card">
        <div class="rc-top">
          <div class="rc-icon" style="background:var(--hydro-dim);color:var(--hydro)"><i class="ti ti-shield-check"></i></div>
          <span class="tag ${deployed ? 'critical' : 'ok'}">${deployed ? 'Deployed' : 'Standby'}</span>
        </div>
        <div style="font-weight:600;font-size:13.5px">${t.name}</div>
        <div style="font-size:11.5px;color:var(--text-faint);margin-top:2px">${t.type} · ${t.members} members</div>
        <div class="res-foot" style="margin-top:12px">
          <span><i class="ti ti-map-pin" style="font-size:12px;vertical-align:-1px"></i> ${t.location}</span>
        </div>
      </div>`;
  }).join('');
}
