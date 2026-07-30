// All mock records live here so each render-*.js file only handles rendering.
// When the backend is ready, replace these arrays with fetch(`${API_BASE}/api/...`) calls.

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

const RESCUE_TEAMS = [
  { name:'NDRF Team Alpha',   type:'NDRF',      members:12, location:'Sivasagar', status:'deployed' },
  { name:'SDRF Unit 3',       type:'SDRF',      members:9,  location:'Golaghat',  status:'deployed' },
  { name:'District Police RRT', type:'Police',  members:15, location:'Jorhat',    status:'standby' },
  { name:'Red Cross Volunteers', type:'Volunteer', members:22, location:'Charaideo', status:'deployed' },
  { name:'NDRF Team Bravo',   type:'NDRF',      members:12, location:'Numaligarh', status:'standby' },
  { name:'Fire & Emergency Svc', type:'Fire',   members:8,  location:'Sivasagar', status:'deployed' },
  { name:'Coast Guard Boat Unit', type:'Boat',  members:6,  location:'Dhansiri River', status:'deployed' },
  { name:'Civil Defence Corps', type:'Volunteer', members:30, location:'Jorhat', status:'standby' },
];

const ALERTS = [
  { title:'Severe flood warning — Sivasagar', level:'critical', districts:'Sivasagar, Charaideo', population:'1.2 L', confidence:91, endsIn: 3*3600 },
  { title:'River level advisory — Dhansiri (Golaghat)', level:'warning', districts:'Golaghat', population:'340,000', confidence:84, endsIn: 6*3600 },
  { title:'Heavy rainfall alert — Upper Assam', level:'warning', districts:'Jorhat, Sivasagar, Golaghat', population:'2.1 L', confidence:78, endsIn: 12*3600 },
  { title:'Road closure advisory — GS Road link', level:'critical', districts:'Guwahati sector', population:'—', confidence:95, endsIn: 1*3600 + 40*60 },
];

const REPORTS = [
  {
    user: "Anonymous citizen",
    location: "Riverside Colony, Sivasagar",
    severity: "critical",
    verified: true,
    time: "4 min ago",
    status: "Dispatched",
    image: "https://images.unsplash.com/photo-1657069343871-fd1476990d04?auto=format&fit=crop&w=1200&q=80"
  },
  {
    user: "Anonymous citizen",
    location: "Golaghat Bridge",
    severity: "critical",
    verified: true,
    time: "11 min ago",
    status: "En route",
    image: "https://images.unsplash.com/photo-1657069342814-ef2dcfb25f6f?auto=format&fit=crop&w=1200&q=80"
  },
  {
    user: "Anonymous citizen",
    location: "Market Road",
    severity: "moderate",
    verified: false,
    time: "22 min ago",
    status: "Reviewing",
    image: "https://images.unsplash.com/photo-1657069342866-2d11c2509b02?auto=format&fit=crop&w=1200&q=80"
  },
  {
    user: "Anonymous citizen",
    location: "Relief Shelter",
    severity: "moderate",
    verified: true,
    time: "40 min ago",
    status: "Monitoring",
    image: "https://images.unsplash.com/photo-1762624822556-921847c110d9?auto=format&fit=crop&w=1200&q=80"
  },
  {
    user: "Anonymous citizen",
    location: "Overflowing River",
    severity: "critical",
    verified: true,
    time: "1 hr ago",
    status: "Dispatched",
    image: "https://images.unsplash.com/photo-1545276070-ec815f01c6ec?auto=format&fit=crop&w=1200&q=80"
  },
  {
    user: "Anonymous citizen",
    location: "NDRF Rescue Operation",
    severity: "critical",
    verified: true,
    time: "2 hr ago",
    status: "Rescue Ongoing",
    image: "https://images.unsplash.com/photo-1741081288260-877057e3fa27?auto=format&fit=crop&w=1200&q=80"
  }
];
