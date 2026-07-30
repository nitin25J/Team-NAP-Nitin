// Animate KPI number counters on load
function animateCount(el, target, suffix){
  const duration = 1200;
  const start = performance.now();
  function tick(now){
    const p = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - p, 3);
    const val = Math.round(target * eased);
    el.textContent = val.toLocaleString('en-IN') + (suffix || '');
    if (p < 1) requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
}

function animateAllKpis(){
  document.querySelectorAll('.ki-val[data-count]').forEach(el=>{
    const target = Number(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    animateCount(el, target, suffix);
  });
}

// Command ring — animates the severity arc to its value
const ringFill = document.getElementById('ringFill');
const ringNum = document.getElementById('ringNum');
const CIRCUMFERENCE = 440; // 2 * PI * r(70), matches the SVG circle

function setSeverityRing(score){
  if (!ringFill) return;
  const offset = CIRCUMFERENCE - (score / 100) * CIRCUMFERENCE;
  requestAnimationFrame(()=>{ ringFill.style.strokeDashoffset = offset; });
  animateCount(ringNum, score, '');
}

function setKpi(id, value, suffix){
  const el = document.getElementById(id);
  if (!el) return;
  el.dataset.count = value;
  if (suffix !== undefined) el.dataset.suffix = suffix;
}
