// All mock records live here so each render-*.js file only handles rendering.
// Fallback datasets ensure the UI functions 100% even if backend network calls fail.

let RESOURCES = [
  { name:'Ambulances',        icon:'ti-ambulance',      have:34, total:48, color:'var(--alert)' },
  { name:'Fire trucks',       icon:'ti-flame',          have:11, total:16, color:'var(--warn)' },
  { name:'Boats',             icon:'ti-anchor',         have:22, total:30, color:'var(--hydro)' },
  { name:'Rescue helicopters',icon:'ti-helicopter',     have:4,  total:6,  color:'var(--violet)' },
  { name:'Medical kits',      icon:'ti-first-aid-kit',  have:860,total:1200,color:'var(--safe)' },
  { name:'Food supplies',     icon:'ti-bread',          have:640,total:1000,color:'var(--warn)' },
  { name:'Water supplies',    icon:'ti-droplet',        have:410,total:900, color:'var(--blue)' },
  { name:'Volunteers',        icon:'ti-users',          have:312,total:400, color:'var(--safe)' },
];

let RESCUE_TEAMS = [
  { name:'NDRF Team Alpha',   type:'NDRF Battalion 12', members:45, location:'Sivasagar', status:'deployed' },
  { name:'SDRF Unit Bravo',   type:'SDRF State Force',  members:30, location:'Golaghat',  status:'deployed' },
  { name:'Indian Army Column 4', type:'Military Relief', members:60, location:'Cachar',   status:'deployed' },
  { name:'Sivasagar Motorboat Fleet', type:'Inflatable Boat Unit', members:16, location:'Sivasagar', status:'deployed' },
  { name:'Guwahati Quick Response', type:'Medical Evac QRT', members:20, location:'Kamrup Metropolitan', status:'standby' },
  { name:'NDRF Team Echo',   type:'NDRF Deep Water',   members:35, location:'Dibrugarh', status:'deployed' },
  { name:'Jorhat Fire & Rescue Unit', type:'Fire & Emergency Svc', members:18, location:'Jorhat', status:'standby' },
  { name:'IAF Chopper Rescue Sqn 3', type:'Air Evacuation Squadron', members:12, location:'Lakhimpur', status:'deployed' },
];

let ALERTS = [
  { title:'Flash Flood & River Breach Warning — Sivasagar', level:'critical', districts:'Sivasagar, Charaideo', population:'1.2 L', confidence:91, endsIn: 3*3600 },
  { title:'Heavy Rainfall & Landslide Watch — Charaideo', level:'warning', districts:'Charaideo, Sivasagar', population:'2.1 L', confidence:88, endsIn: 6*3600 },
  { title:'Embankment Erosion Advisory — Dhansiri (Golaghat)', level:'critical', districts:'Golaghat', population:'340,000', confidence:94, endsIn: 4*3600 },
  { title:'Urban Waterlogging Advisory — GS Road Link', level:'warning', districts:'Kamrup Metropolitan', population:'1.5 L', confidence:85, endsIn: 2*3600 + 30*60 },
  { title:'Subansiri Surge & Inundation Watch — Lakhimpur', level:'critical', districts:'Lakhimpur, Dhemaji', population:'1.8 L', confidence:92, endsIn: 8*3600 },
];

let REPORTS = [
  {
    user: "Bhaben Kalita",
    location: "Riverside colony, Ward 4, Sivasagar",
    severity: "critical",
    verified: true,
    time: "25 min ago",
    status: "Verified & Dispatched",
    image: "https://images.unsplash.com/photo-1657069343871-fd1476990d04?auto=format&fit=crop&w=1200&q=80"
  },
  {
    user: "Priyanka Gogoi",
    location: "Sector 12 approach bridge, Golaghat",
    severity: "critical",
    verified: true,
    time: "50 min ago",
    status: "En route",
    image: "https://images.unsplash.com/photo-1657069342814-ef2dcfb25f6f?auto=format&fit=crop&w=1200&q=80"
  },
  {
    user: "Anil Saikia",
    location: "Market road junction, Charaideo",
    severity: "moderate",
    verified: false,
    time: "1 hr ago",
    status: "Reviewing",
    image: "https://images.unsplash.com/photo-1657069342866-2d11c2509b02?auto=format&fit=crop&w=1200&q=80"
  },
  {
    user: "Mukesh Sharma",
    location: "Relief Camp Entrance, Jorhat",
    severity: "moderate",
    verified: true,
    time: "1 hr ago",
    status: "Monitoring",
    image: "https://images.unsplash.com/photo-1762624822556-921847c110d9?auto=format&fit=crop&w=1200&q=80"
  },
  {
    user: "Rituraj Baruah",
    location: "Overflowing Brahmaputra Bank, Dibrugarh",
    severity: "critical",
    verified: true,
    time: "2 hr ago",
    status: "Dispatched",
    image: "https://images.unsplash.com/photo-1545276070-ec815f01c6ec?auto=format&fit=crop&w=1200&q=80"
  },
  {
    user: "Kavita Das",
    location: "NDRF Evacuation Operation, Lakhimpur",
    severity: "critical",
    verified: true,
    time: "3 hr ago",
    status: "Rescue Ongoing",
    image: "https://images.unsplash.com/photo-1741081288260-877057e3fa27?auto=format&fit=crop&w=1200&q=80"
  }
];

let HOSPITALS = [
  { name: 'Guwahati Medical College & Hospital', district: 'Kamrup Metropolitan', status: 'Operational', beds_available: 45, beds_total: 350, icu_beds: 8, oxygen_available: true, lat: 26.1558, lng: 91.7686, contact: '+91 361 2529457' },
  { name: 'Sivasagar Civil Hospital', district: 'Sivasagar', status: 'High Load', beds_available: 12, beds_total: 120, icu_beds: 2, oxygen_available: true, lat: 26.9826, lng: 94.6425, contact: '+91 3772 222100' },
  { name: 'Jorhat Medical College & Hospital', district: 'Jorhat', status: 'Operational', beds_available: 84, beds_total: 450, icu_beds: 18, oxygen_available: true, lat: 26.7570, lng: 94.2031, contact: '+91 376 2370010' },
  { name: 'Golaghat Civil Hospital', district: 'Golaghat', status: 'Critical Surge', beds_available: 5, beds_total: 90, icu_beds: 2, oxygen_available: true, lat: 26.5194, lng: 93.9634, contact: '+91 3774 280222' },
  { name: 'Assam Medical College Hospital (AMCH)', district: 'Dibrugarh', status: 'Operational', beds_available: 140, beds_total: 800, icu_beds: 35, oxygen_available: true, lat: 27.4728, lng: 94.9120, contact: '+91 373 2300080' },
  { name: 'Silchar Medical College Hospital', district: 'Cachar', status: 'Moderate', beds_available: 62, beds_total: 500, icu_beds: 15, oxygen_available: true, lat: 24.8333, lng: 92.7789, contact: '+91 3842 240445' },
  { name: 'Sonari Civil Hospital', district: 'Charaideo', status: 'High Load', beds_available: 15, beds_total: 80, icu_beds: 2, oxygen_available: true, lat: 26.9000, lng: 94.8800, contact: '+91 3772 256211' },
  { name: 'Lakhimpur Medical College & Hospital', district: 'Lakhimpur', status: 'Operational', beds_available: 38, beds_total: 200, icu_beds: 6, oxygen_available: true, lat: 27.2340, lng: 94.1030, contact: '+91 3752 222300' },
  { name: 'Dhemaji District Civil Hospital', district: 'Dhemaji', status: 'Critical Surge', beds_available: 9, beds_total: 75, icu_beds: 1, oxygen_available: true, lat: 27.4800, lng: 94.5800, contact: '+91 3753 224100' },
  { name: 'Nagaon BP Civil Hospital', district: 'Nagaon', status: 'Operational', beds_available: 42, beds_total: 220, icu_beds: 7, oxygen_available: true, lat: 26.3450, lng: 92.6830, contact: '+91 3672 233200' }
];
