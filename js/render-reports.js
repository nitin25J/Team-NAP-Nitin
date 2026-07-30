// Renders the Citizen Reports grid from REPORTS (fetched from /reports/).
// The backend has no photo/media URL or explicit severity tier for a
// report, only a "type" and a review "status" plus a media_attached flag —
// so the tag now shows the report type and the "AI verified" badge is
// driven by media_attached instead of a fabricated value.
const reportsGrid = document.getElementById('reportsGrid');

function timeAgo(isoString){
  if (!isoString) return '';
  const then = new Date(isoString).getTime();
  if (Number.isNaN(then)) return '';
  const diffSec = Math.max(0, Math.floor((Date.now() - then) / 1000));
  if (diffSec < 60) return `${diffSec} sec ago`;
  const diffMin = Math.floor(diffSec / 60);
  if (diffMin < 60) return `${diffMin} min ago`;
  const diffHr = Math.floor(diffMin / 60);
  if (diffHr < 24) return `${diffHr} hr ago`;
  return `${Math.floor(diffHr / 24)} day(s) ago`;
}

function renderReportsGrid(){
  if (!reportsGrid) return;
  reportsGrid.innerHTML = REPORTS.map(r=>`
    <div class="card hoverable report-card">
      <div class="report-media">
        ${r.media_attached ? '<span class="verified-badge"><i class="ti ti-rosette-discount-check"></i>Media attached</span>' : ''}
      </div>
      <div class="report-user">
        <div class="ru-avatar"><i class="ti ti-user"></i></div>
        <div>
          <div style="font-size:12.5px;font-weight:600">${r.reporter_name}</div>
          <div style="font-size:10.5px;color:var(--text-faint)">${timeAgo(r.submitted_at)}</div>
        </div>
      </div>
      <div style="font-size:12.5px;color:var(--text-dim);display:flex;align-items:center;gap:5px;margin-bottom:8px">
        <i class="ti ti-map-pin" style="font-size:13px"></i>${r.location}, ${r.district}
      </div>
      <div style="display:flex;justify-content:space-between;align-items:center">
        <span class="tag ${r.status === 'Verified' ? 'ok' : r.status === 'Pending Review' ? 'moderate' : 'critical'}">${r.type}</span>
        <span style="font-size:11px;color:var(--text-faint)">${r.status}</span>
      </div>
    </div>`).join('');
}
