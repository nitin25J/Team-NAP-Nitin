// Renders the Resource Management grid from RESOURCES (see mock-data.js)
const resourceGrid = document.getElementById('resourceGrid');

if (resourceGrid) {
  resourceGrid.innerHTML = RESOURCES.map(r=>{
    const pct = Math.round((r.have / r.total) * 100);
    return `
      <div class="card hoverable res-card">
        <div class="rc-top">
          <div class="rc-icon" style="background:color-mix(in srgb, ${r.color} 18%, transparent);color:${r.color}">
            <i class="ti ${r.icon}"></i>
          </div>
          <span class="tag ${pct < 40 ? 'critical' : pct < 70 ? 'moderate' : 'ok'}">${pct}% avail.</span>
        </div>
        <div style="font-weight:600;font-size:13.5px">${r.name}</div>
        <div class="progress"><div class="progress-fill" style="width:${pct}%;background:${r.color}"></div></div>
        <div class="res-foot"><span>${r.have} available</span><span>${r.total} total</span></div>
      </div>`;
  }).join('');
}
