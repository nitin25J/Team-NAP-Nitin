// Dark / light theme toggle
function setTheme(mode){
  document.documentElement.setAttribute('data-theme', mode);
  document.querySelectorAll('.theme-toggle button').forEach(b=>{
    b.classList.toggle('active', b.dataset.theme === mode);
  });
  localStorage.setItem('varuna-theme', mode);
}

document.querySelectorAll('.theme-toggle button').forEach(btn=>{
  btn.addEventListener('click', ()=> setTheme(btn.dataset.theme));
});

// Restore saved preference, default dark
setTheme(localStorage.getItem('varuna-theme') || 'dark');
