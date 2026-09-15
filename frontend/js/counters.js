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

document.querySelectorAll('.ki-val[data-count]').forEach(el=>{
  const target = Number(el.dataset.count);
  const suffix = el.dataset.suffix || '';
  animateCount(el, target, suffix);
});

window.setKpi = function(id, val, suffix) {
  const el = document.getElementById(id);
  if (!el) return;
  el.dataset.count = val;
  el.dataset.suffix = suffix || '';
  animateCount(el, Number(val), suffix);
};

// Also define setSeverityRing which is called in index.html
window.setSeverityRing = function(score) {
  const ringFill = document.getElementById('ringFill');
  const ringNum = document.getElementById('ringNum');
  const CIRCUMFERENCE = 440; // 2 * PI * r(70)
  if (ringFill) {
    const offset = CIRCUMFERENCE - (score / 100) * CIRCUMFERENCE;
    requestAnimationFrame(()=>{ ringFill.style.strokeDashoffset = offset; });
    if (ringNum) animateCount(ringNum, score, '');
  }
};

// Command ring — animates the severity arc to its value
const SEVERITY_SCORE = 74; // 0-100, drives both the ring and its number
const ringFill = document.getElementById('ringFill');
const ringNum = document.getElementById('ringNum');
const CIRCUMFERENCE = 440; // 2 * PI * r(70), matches the SVG circle

if (ringFill) {
  const offset = CIRCUMFERENCE - (SEVERITY_SCORE / 100) * CIRCUMFERENCE;
  requestAnimationFrame(()=>{ ringFill.style.strokeDashoffset = offset; });
  animateCount(ringNum, SEVERITY_SCORE, '');
}
