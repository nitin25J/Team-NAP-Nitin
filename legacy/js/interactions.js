// Universal Interactivity & Live Search Handler for Varuna AI

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sidebar Navigation Event Delegation
  const rail = document.getElementById('rail');
  if (rail) {
    rail.addEventListener('click', (e) => {
      const btn = e.target.closest('.nav-item');
      if (!btn) return;

      const viewId = btn.dataset.view;
      if (!viewId) return;

      document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
      const targetView = document.getElementById('view-' + viewId);
      if (targetView) targetView.classList.add('active');

      if (viewId === 'map' && window.liveMapInstance) {
        setTimeout(() => window.liveMapInstance.invalidateSize(), 100);
      }
    });
  }

  // 2. Universal Live Search Filter
  const searchInput = document.querySelector('.searchbar input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase().trim();
      filterAllViews(query);
    });
  }

  // 3. Quick Links & Dashboard Navigation Cards
  document.addEventListener('click', (e) => {
    // Quick link card clicks
    const qCard = e.target.closest('.hero-kpis .card, .feat-card');
    if (qCard && qCard.dataset.view) {
      switchView(qCard.dataset.view);
    }

    // Refresh button
    if (e.target.closest('#view-dashboard .btn.primary')) {
      if (window.initFromBackend) window.initFromBackend();
      if (window.showToast) showToast('System posture refreshed from live server', 'ok');
    }

    // Try voice input button
    if (e.target.closest('button') && e.target.closest('button').textContent.includes('voice input')) {
      if (window.showToast) showToast('Voice command listener active: Speak command...', 'ok');
    }
  });
});

function switchView(viewId) {
  const navBtn = document.querySelector(`.nav-item[data-view="${viewId}"]`);
  if (navBtn) navBtn.click();
}

function filterAllViews(query) {
  if (!query) {
    // Reset visibility
    document.querySelectorAll('tr, .res-card, .alert-card, .report-card, .feat-card').forEach(el => {
      el.style.display = '';
    });
    return;
  }

  // Filter Table Rows
  document.querySelectorAll('tbody tr').forEach(row => {
    const text = row.textContent.toLowerCase();
    row.style.display = text.includes(query) ? '' : 'none';
  });

  // Filter Cards
  document.querySelectorAll('.res-card, .alert-card, .report-card, .feat-card').forEach(card => {
    const text = card.textContent.toLowerCase();
    card.style.display = text.includes(query) ? '' : 'none';
  });
}
