// Small toast notifications — floating live-update style messages.
function showToast(message, icon){
  const wrap = document.getElementById('toastWrap');
  const el = document.createElement('div');
  el.className = 'toast';
  el.innerHTML = `<i class="ti ${icon || 'ti-bell-ringing'}"></i><span>${message}</span>`;
  wrap.appendChild(el);
  setTimeout(()=>{
    el.style.transition = 'opacity .3s';
    el.style.opacity = '0';
    setTimeout(()=> el.remove(), 300);
  }, 4200);
}

// Demo: one toast shortly after load, to show the pattern working live
setTimeout(()=> showToast('New citizen report verified in Sivasagar', 'ti-rosette-discount-check'), 1600);

document.getElementById('aiAssistantBtn').addEventListener('click', ()=>{
  showToast('AI assistant: 3 recommended actions ready in Live Map view', 'ti-sparkles');
});
