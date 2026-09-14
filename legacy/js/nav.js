// Sidebar navigation — switches the visible view
document.querySelectorAll('.nav-item').forEach(btn=>{
  btn.addEventListener('click', ()=>{
    document.querySelectorAll('.nav-item').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));
    document.getElementById('view-' + btn.dataset.view).classList.add('active');

    // Leaflet needs a resize nudge whenever its container becomes visible again
    if (btn.dataset.view === 'map' && window.liveMapInstance) {
      setTimeout(()=> window.liveMapInstance.invalidateSize(), 80);
    }
  });
});

// Collapse sidebar to icon-only
document.getElementById('collapseBtn').addEventListener('click', ()=>{
  document.getElementById('appShell').classList.toggle('collapsed');
  if (window.liveMapInstance) {
    setTimeout(()=> window.liveMapInstance.invalidateSize(), 300);
  }
});
