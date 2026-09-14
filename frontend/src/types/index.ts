/* ============================================================================
   VARUNA AI 2.0 — TypeScript Interfaces
   All shared types for the application.
   ============================================================================ */

// ---- Dashboard ----
export interface OverviewStats {
  active_alerts: number;
  high_risk_districts: number;
  total_population_affected: number;
  rescue_teams_deployed: number;
  relief_camps_active: number;
  hospitals_monitored: number;
  citizen_reports_logged: number;
  current_risk_level: string;
  max_severity_score: number;
}

export interface DashboardData {
  state: string;
  overview_stats: OverviewStats;
  top_districts: TopDistrict[];
  quick_links: QuickLink[];
  recent_activity: RecentActivity[];
}

export interface TopDistrict {
  district: string;
  risk_level: string;
  severity_score: number;
  river: string;
  status: string;
}

export interface QuickLink {
  label: string;
  view: string;
  icon: string;
}

export interface RecentActivity {
  time: string;
  event: string;
}

// ---- Hospital ----
export interface Hospital {
  id: number;
  name: string;
  district: string;
  beds_available: number;
  beds_total: number;
  icu_available: number;
  icu_total: number;
  icu_beds: number;
  oxygen_available: boolean;
  status: string;
  contact: string;
  lat: number | null;
  lng: number | null;
  coordinates: { lat: number; lng: number } | null;
}

// ---- Rescue Team ----
export interface RescueTeam {
  id: string;
  team_id: string;
  name: string;
  type: string;
  district: string;
  location: string;
  members: number;
  personnel_count: number;
  status: string;
  lat: number | null;
  lng: number | null;
  coordinates: { lat: number; lng: number } | null;
}

// ---- Emergency Alert ----
export interface EmergencyAlert {
  id: number;
  alert_id: string;
  type: string;
  title: string;
  severity: string;
  level: string;
  district: string;
  districts: string;
  river: string | null;
  message: string;
  population: string;
  confidence: number;
  endsIn: number;
  issued_by: string;
  issued_at: string | null;
  valid_until: string | null;
  status: string;
}

// ---- Citizen Report ----
export interface CitizenReport {
  id: number;
  report_id: string;
  reporter_name: string;
  user: string;
  type: string;
  location: string;
  district: string;
  description: string;
  severity: string;
  status: string;
  verified: boolean;
  media_attached: boolean;
  time: string;
  submitted_at: string | null;
  image: string;
}

// ---- Resource ----
export interface ResourceItem {
  id: number;
  name: string;
  icon: string;
  have: number;
  total: number;
  color: string;
}

export interface Shelter {
  id: number;
  name: string;
  district: string;
  capacity: number;
  occupancy: number;
  lat: number | null;
  lng: number | null;
  coordinates: { lat: number; lng: number } | null;
}

export interface ResourceData {
  inventory: ResourceItem[];
  shelters: Shelter[];
}

// ---- AI Prediction ----
export interface Prediction {
  district: string;
  hazard_type: string;
  risk_level: string;
  risk_score: number;
  severity_score: number;
  confidence: number;
  river_name: string;
  water_level_m: number;
  danger_mark_m: number;
  rainfall_mm_24h: number;
  wind_speed_kmh: number;
  recommendations: string[];
  last_updated: string;
}

export interface PredictionData {
  model_name: string;
  model_version: string;
  last_run: string;
  predictions: Prediction[];
}

// ---- Weather ----
export interface WeatherForecast {
  district: string;
  temperature_c: number;
  humidity_pct: number;
  rainfall_mm_24h: number;
  current_rain_mm_h: number;
  wind_speed_kmh: number;
  pressure_hpa: number;
  condition: string;
  coordinates: { lat: number; lng: number };
  data_source: string;
}

// ---- Chatbot ----
export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  data?: Record<string, unknown>;
}

export interface ChatbotResponse {
  risk: string;
  district: string;
  confidence: string;
  recommendation: string;
  action?: string;
  details?: string;
  nearest_facility?: string;
  river_level?: string;
}

// ---- UI State ----
export type ViewId =
  | 'dashboard'
  | 'map'
  | 'ai'
  | 'resources'
  | 'hospitals'
  | 'rescue'
  | 'alerts'
  | 'satellite'
  | 'reports'
  | 'analytics'
  | 'settings';

export type Theme = 'dark' | 'light';

export type SeverityLevel = 'critical' | 'severe' | 'moderate' | 'low';
