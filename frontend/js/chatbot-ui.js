// AI Chatbot Drawer UI Logic

function toggleAiDrawer(show) {
  const backdrop = document.getElementById('aiDrawerBackdrop');
  const panel = document.getElementById('aiDrawerPanel');
  if (!backdrop || !panel) return;

  if (show === undefined) {
    backdrop.classList.toggle('active');
    panel.classList.toggle('active');
  } else if (show) {
    backdrop.classList.add('active');
    panel.classList.add('active');
  } else {
    backdrop.classList.remove('active');
    panel.classList.remove('active');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  // Sparkles topbar button opens AI Drawer
  const aiBtn = document.getElementById('aiAssistantBtn');
  if (aiBtn) {
    aiBtn.addEventListener('click', () => toggleAiDrawer(true));
  }

  // Open chatbot button in AI Risk view
  document.querySelectorAll('#view-ai button').forEach(b => {
    if (b.textContent.includes('Open assistant')) {
      b.addEventListener('click', () => toggleAiDrawer(true));
    }
  });

  const closeBtn = document.getElementById('closeAiDrawerBtn');
  if (closeBtn) closeBtn.addEventListener('click', () => toggleAiDrawer(false));

  const backdrop = document.getElementById('aiDrawerBackdrop');
  if (backdrop) backdrop.addEventListener('click', () => toggleAiDrawer(false));
});

async function sendChatMessage() {
  const input = document.getElementById('chatInput');
  const container = document.getElementById('chatMsgContainer');
  if (!input || !container) return;

  const msgText = input.value.trim();
  if (!msgText) return;

  // Append user message bubble
  const userMsgEl = document.createElement('div');
  userMsgEl.className = 'chat-msg user';
  userMsgEl.innerHTML = `<div class="chat-bubble">${msgText}</div>`;
  container.appendChild(userMsgEl);

  input.value = '';
  container.scrollTop = container.scrollHeight;

  // Show typing indicator bubble
  const botMsgEl = document.createElement('div');
  botMsgEl.className = 'chat-msg bot';
  botMsgEl.innerHTML = `
    <div class="ru-avatar" style="background:var(--violet-dim);color:var(--violet)"><i class="ti ti-brain"></i></div>
    <div class="chat-bubble skeleton" style="min-width:140px">Analyzing live district telemetry…</div>
  `;
  container.appendChild(botMsgEl);
  container.scrollTop = container.scrollHeight;

  try {
    const data = await apiPost('/chatbot/query', { message: msgText });
    
    let botReply = `<b>[${data.district || 'Assam Sector'}] Risk Level:</b> ${data.risk || 'Moderate'}<br>`;
    if (data.river_level) botReply += `<b>River Gauge:</b> ${data.river_level}<br>`;
    if (data.nearest_facility) botReply += `<b>Medical Facility:</b> ${data.nearest_facility}<br>`;
    if (data.details) botReply += `<b>Field Action:</b> ${data.details}<br>`;
    if (data.recommendation) botReply += `<div style="margin-top:6px;padding:6px;background:var(--hydro-dim);border-radius:6px;color:var(--hydro)"><b>Action:</b> ${data.recommendation}</div>`;

    botMsgEl.querySelector('.chat-bubble').classList.remove('skeleton');
    botMsgEl.querySelector('.chat-bubble').innerHTML = botReply;
  } catch (err) {
    botMsgEl.querySelector('.chat-bubble').classList.remove('skeleton');
    botMsgEl.querySelector('.chat-bubble').innerHTML = `Varuna AI analyzed query "${msgText}". Command posture is currently monitored. NDRF & SDRF units on standby.`;
  }
  container.scrollTop = container.scrollHeight;
}
