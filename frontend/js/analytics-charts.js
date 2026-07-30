// Analytics view — four Chart.js charts. Swap the data arrays for real
// aggregates from the backend once /api/analytics endpoints exist.
Chart.defaults.color = '#93AAB6';
Chart.defaults.font.family = "'Inter', sans-serif";
Chart.defaults.borderColor = 'rgba(255,255,255,0.06)';

new Chart(document.getElementById('chartFreq'), {
  type: 'bar',
  data: {
    labels: ['Feb','Mar','Apr','May','Jun','Jul'],
    datasets: [{
      label: 'Disasters recorded',
      data: [2, 3, 5, 7, 9, 14],
      backgroundColor: '#17C9C0',
      borderRadius: 6,
      maxBarThickness: 34
    }]
  },
  options: { plugins:{ legend:{ display:false } }, scales:{ y:{ grid:{ color:'rgba(255,255,255,0.06)'} }, x:{ grid:{ display:false } } } }
});

new Chart(document.getElementById('chartResponse'), {
  type: 'line',
  data: {
    labels: ['Feb','Mar','Apr','May','Jun','Jul'],
    datasets: [{
      label: 'Avg. response time',
      data: [58, 52, 47, 41, 38, 33],
      borderColor: '#5B9CFF',
      backgroundColor: 'rgba(91,156,255,0.15)',
      fill: true,
      tension: 0.35,
      pointRadius: 3
    }]
  },
  options: { plugins:{ legend:{ display:false } }, scales:{ y:{ grid:{ color:'rgba(255,255,255,0.06)'} }, x:{ grid:{ display:false } } } }
});

new Chart(document.getElementById('chartUtil'), {
  type: 'doughnut',
  data: {
    labels: ['Ambulances','Boats','Helicopters','Fire trucks','Volunteers'],
    datasets: [{
      data: [71, 73, 67, 69, 78],
      backgroundColor: ['#FF6A4D','#17C9C0','#9B7BFF','#F5B94D','#3ED598'],
      borderWidth: 0
    }]
  },
  options: { plugins:{ legend:{ position:'bottom', labels:{ boxWidth:10, font:{size:10.5} } } }, cutout:'62%' }
});

new Chart(document.getElementById('chartConf'), {
  type: 'line',
  data: {
    labels: ['Week 1','Week 2','Week 3','Week 4','Week 5','Week 6'],
    datasets: [{
      label: 'AI model confidence',
      data: [81, 84, 83, 88, 90, 92],
      borderColor: '#3ED598',
      backgroundColor: 'rgba(62,213,152,0.15)',
      fill: true,
      tension: 0.35,
      pointRadius: 3
    }]
  },
  options: { plugins:{ legend:{ display:false } }, scales:{ y:{ min:70, max:100, grid:{ color:'rgba(255,255,255,0.06)'} }, x:{ grid:{ display:false } } } }
});
