// Live Disaster Map — Leaflet init + toggleable overlay layers.
// Replace the marker/circle coordinates below with real feed data once the
// backend is wired up (see config.js for API_BASE).

const GUWAHATI = [26.1445, 91.7362];

const liveMap = L.map('liveMap', { zoomControl: true }).setView(GUWAHATI, 10);
window.liveMapInstance = liveMap; // exposed so nav.js can invalidateSize() on tab switch

L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; OpenStreetMap &copy; CARTO',
  subdomains: 'abcd',
  maxZoom: 19
}).addTo(liveMap);

// ---- Layer groups, one per chip ----
const layers = {
  flood:      L.layerGroup([ L.circle([26.10, 91.90], { radius: 6000, color:'#5B9CFF', fillColor:'#5B9CFF', fillOpacity:0.25, weight:1 }) ]),
  wildfire:   L.layerGroup([ L.circle([26.30, 91.60], { radius: 4000, color:'#FF6A4D', fillColor:'#FF6A4D', fillOpacity:0.25, weight:1 }) ]),
  cyclone:    L.layerGroup([ L.polyline([[25.9,92.3],[26.05,92.0],[26.2,91.7],[26.35,91.4]], { color:'#9B7BFF', weight:3, dashArray:'6,6' }) ]),
  landslide:  L.layerGroup([ L.circle([26.35, 92.05], { radius: 5000, color:'#B08968', fillColor:'#B08968', fillOpacity:0.22, weight:1 }) ]),
  earthquake: L.layerGroup([ L.circle([26.0, 91.5], { radius: 7000, color:'#F5B94D', fillColor:'#F5B94D', fillOpacity:0.18, weight:1 }) ]),
  traffic:    L.layerGroup([ L.polyline([[26.14,91.70],[26.16,91.75],[26.18,91.80]], { color:'#F5B94D', weight:5, opacity:0.6 }) ]),
  radar:      L.layerGroup([ L.circle(GUWAHATI, { radius: 20000, color:'#8CA3AE', fillColor:'#8CA3AE', fillOpacity:0.06, weight:1, dashArray:'4,6' }) ]),
  drones:     L.layerGroup([
                mkDot([26.12, 91.86], '#9B7BFF', 'ti-drone', 'Drone-01 · airborne'),
                mkDot([26.25, 91.65], '#9B7BFF', 'ti-drone', 'Drone-02 · airborne'),
              ]),
  sensors:    L.layerGroup([
                mkDot([26.15, 91.95], '#3ED598', 'ti-antenna', 'River gauge · Sivasagar'),
                mkDot([26.32, 91.55], '#3ED598', 'ti-antenna', 'Rainfall sensor · Golaghat'),
              ]),
  hospitals:  L.layerGroup([
                mkDot([26.13, 91.80], '#3ED598', 'ti-building-hospital', 'Sivasagar Civil Hospital · 88% ICU'),
                mkDot([26.30, 91.62], '#3ED598', 'ti-building-hospital', 'Golaghat District Hospital · 61% ICU'),
              ]),
  shelters:   L.layerGroup([
                mkDot([26.11, 91.92], '#17C9C0', 'ti-home', 'Govt school shelter · 71% full'),
                mkDot([26.20, 91.75], '#17C9C0', 'ti-home', 'Community hall shelter · 39% full'),
              ]),
  units:      L.layerGroup([
                mkDot([26.145, 91.83], '#5B9CFF', 'ti-truck', 'NDRF Team Alpha · en route'),
                mkDot([26.28, 91.60], '#5B9CFF', 'ti-anchor', 'Boat unit · deployed'),
              ]),
};

function mkDot(latlng, color, icon, label){
  const html = `<div style="width:26px;height:26px;border-radius:50%;background:${color};display:flex;align-items:center;justify-content:center;border:2px solid #0E1B26;box-shadow:0 0 0 2px ${color}55;">
                  <i class="ti ${icon}" style="font-size:13px;color:#04211f"></i>
                </div>`;
  const divIcon = L.divIcon({ html, className:'', iconSize:[26,26], iconAnchor:[13,13] });
  return L.marker(latlng, { icon: divIcon }).bindTooltip(label, { direction:'top', offset:[0,-10] });
}

// Turn on the layers that start "on" per the chip markup in index.html
document.querySelectorAll('.chip').forEach(chip=>{
  const key = chip.dataset.layer;
  if (chip.classList.contains('on') && layers[key]) layers[key].addTo(liveMap);

  chip.addEventListener('click', ()=>{
    chip.classList.toggle('on');
    if (!layers[key]) return;
    if (chip.classList.contains('on')) layers[key].addTo(liveMap);
    else liveMap.removeLayer(layers[key]);
  });
});
