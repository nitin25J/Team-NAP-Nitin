// current_risk_level from the backend is a tier name, not a 0-100 score,
// so it's mapped onto the ring's numeric scale here.
const RISK_LEVEL_SCORE = { Severe: 92, Critical: 92, High: 74, Moderate: 50, Low: 25 };

// RESOURCES stays a local list: the backend's /resources endpoint only
// exposes state-wide totals (boats, food packets, medical kits, tents,
// water-purification units) with no matching "currently available" figure,
// so there is no backend field to drive the have/total bars below without
// inventing numbers. RESCUE_TEAMS, ALERTS and REPORTS are now fetched live
// from the backend instead of being hardcoded.
const RESOURCES = [
  { name:'Ambulances',        icon:'ti-ambulance',      have:34, total:48, color:'var(--alert)' },
  { name:'Fire trucks',       icon:'ti-flame',          have:11, total:16, color:'var(--warn)' },
  { name:'Boats',             icon:'ti-anchor',         have:22, total:30, color:'var(--hydro)' },
  { name:'Rescue helicopters',icon:'ti-helicopter',     have:4,  total:6,  color:'var(--violet)' },
  { name:'Medical kits',      icon:'ti-first-aid-kit',  have:860,total:1200,color:'var(--safe)' },
  { name:'Food supplies',     icon:'ti-bread',          have:640,total:1000,color:'var(--warn)' },
  { name:'Water supplies',    icon:'ti-droplet',        have:410,total:900, color:'var(--blue)' },
  { name:'Volunteers',        icon:'ti-users',          have:312,total:400, color:'var(--safe)' },
];

// Fetched live from the backend at runtime; declared here so every module
// that reads them (render-rescue.js, render-alerts.js, render-reports.js)
// shares the same reference.
let RESCUE_TEAMS = [];
let ALERTS = [];
let REPORTS = [];

// Guwahati coordinates, used as the Live Map's default center.
const GUWAHATI = [26.1445, 91.7362];

// Flood risk tier -> marker color, shared by live-map.js.
const FLOOD_RISK_COLOR = { Severe:'#FF6A4D', High:'#F5B94D', Moderate:'#5B9CFF', Low:'#3ED598' };
