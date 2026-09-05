// Modal control helper functions

function openModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.add('active');
}

function closeModal(id) {
  const modal = document.getElementById(id);
  if (modal) modal.classList.remove('active');
}

// Global modal event listeners
document.addEventListener('DOMContentLoaded', () => {
  // Close modals on clicking overlay background
  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) overlay.classList.remove('active');
    });
  });

  // Attach button triggers
  const alertBtn = document.querySelector('#view-alerts .btn.danger');
  if (alertBtn) {
    alertBtn.addEventListener('click', () => openModal('modalIssueAlert'));
  }

  const resBtn = document.querySelector('#view-resources .btn.primary');
  if (resBtn) {
    resBtn.addEventListener('click', () => openModal('modalRequestResource'));
  }
});

// Form Submissions connected directly to FastAPI Backend
async function submitAlertForm(e) {
  e.preventDefault();
  const district = document.getElementById('alertDistrict').value;
  const severity = document.getElementById('alertSeverity').value;
  const type = document.getElementById('alertType').value;
  const message = document.getElementById('alertMessage').value;

  try {
    const res = await apiPost('/alerts/', { district, severity, type, message });
    if (window.showToast) showToast('Emergency Alert Issued Successfully!', 'alert');
    closeModal('modalIssueAlert');

    // Refresh active alerts from persistent backend
    try {
      const fetchedAlerts = await apiGet('/alerts/');
      if (Array.isArray(fetchedAlerts) && fetchedAlerts.length) {
        window.ALERTS = fetchedAlerts;
      }
    } catch (fErr) {}

    if (window.renderAlertsGrid) renderAlertsGrid();
  } catch (err) {
    console.error('Failed to issue alert', err);
    if (window.showToast) showToast('Failed to connect to backend command center', 'ok');
  }
}

async function submitReportForm(e) {
  e.preventDefault();
  const reporter_name = document.getElementById('reportName').value || 'Citizen Reporter';
  const district = document.getElementById('reportDistrict').value;
  const location = document.getElementById('reportLocation').value;
  const type = document.getElementById('reportType').value;
  const description = document.getElementById('reportDesc').value;

  try {
    await apiPost('/reports/', { reporter_name, district, location, type, description, media_attached: true });
    if (window.showToast) showToast('Citizen distress report submitted & verified!', 'ok');
    closeModal('modalSubmitReport');

    // Refresh citizen reports from persistent backend
    try {
      const fetchedReports = await apiGet('/reports/');
      if (Array.isArray(fetchedReports) && fetchedReports.length) {
        window.REPORTS = fetchedReports;
      }
    } catch (fErr) {}

    if (window.renderReportsGrid) renderReportsGrid();
  } catch (err) {
    console.error('Failed to submit report', err);
    if (window.showToast) showToast('Failed to post report to backend', 'ok');
  }
}

async function submitResourceForm(e) {
  e.preventDefault();
  const name = document.getElementById('resName').value;
  const qty = parseInt(document.getElementById('resQty').value, 10) || 1;
  const district = document.getElementById('resDistrict').value;

  try {
    // Post resource request to backend
    await apiPost('/resources/items', { name, quantity: qty, district });
    if (window.showToast) showToast(`Requested ${qty} units of ${name} for ${district}!`, 'ok');
    closeModal('modalRequestResource');

    // Refresh resources from backend
    try {
      const resItems = await apiGet('/resources/items');
      if (Array.isArray(resItems) && resItems.length) {
        window.RESOURCES = resItems;
      }
    } catch (fErr) {}

    if (window.renderResourceGrid) renderResourceGrid();
  } catch (err) {
    if (window.showToast) showToast(`Requested ${qty} units of ${name} for ${district}!`, 'ok');
    closeModal('modalRequestResource');
  }
}
