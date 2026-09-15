// Renders Hospitals table from HOSPITALS (see mock-data.js)

window.renderHospitalsTable = function(hospitalsData) {
  const list = hospitalsData || window.HOSPITALS || [];
  const tbody = document.getElementById('hospitalsTbody');
  if (!tbody) return;

  if (!list.length) {
    tbody.innerHTML = `<tr><td colspan="5" style="text-align:center;padding:16px;color:var(--text-faint)">No hospital records available</td></tr>`;
    return;
  }

  tbody.innerHTML = list.map(h => {
    const avail = h.beds_available ?? 0;
    const total = h.beds_total ?? 100;
    const icu = h.icu_beds ?? 0;
    const isLow = avail < 15;
    const statusClass = isLow ? 'critical' : (avail < 40 ? 'moderate' : 'ok');
    
    return `
      <tr>
        <td style="font-weight:600">${h.name}</td>
        <td>${h.district || 'Assam'}</td>
        <td class="mono"><b>${avail}</b> / ${total}</td>
        <td class="mono">${icu} ICU beds</td>
        <td><span class="tag ${statusClass}">${h.status || (isLow ? 'High Load' : 'Operational')}</span></td>
      </tr>
    `;
  }).join('');
};

document.addEventListener('DOMContentLoaded', () => {
  if (window.renderHospitalsTable) window.renderHospitalsTable();
});
