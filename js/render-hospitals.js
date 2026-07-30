// Hospitals table (Hospitals view)
const hospitalsTbody = document.getElementById('hospitalsTbody');

function renderHospitalsTable(hospitals){
  if (!hospitalsTbody) return;
  hospitalsTbody.innerHTML = hospitals.map(h=>{
    const occPct = h.beds_total ? Math.round(((h.beds_total - h.beds_available) / h.beds_total) * 100) : 0;
    const barColor = occPct >= 80 ? 'var(--alert)' : occPct >= 55 ? 'var(--warn)' : 'var(--safe)';
    const status = occPct >= 80
      ? '<span class="tag critical">Near capacity</span>'
      : occPct >= 55 ? '<span class="tag moderate">Elevated</span>' : '<span class="tag ok">Stable</span>';
    return `<tr>
      <td>${h.name}</td><td>${h.district}</td>
      <td class="mono">${h.beds_available} / ${h.beds_total}</td>
      <td><span class="mini-bar"><span class="mini-fill" style="width:${occPct}%;background:${barColor}"></span></span>${occPct}%</td>
      <td>${status}</td>
    </tr>`;
  }).join('');
}
