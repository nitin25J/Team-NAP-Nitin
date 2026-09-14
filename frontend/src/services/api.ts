/**
 * Varuna AI — API Service Layer
 * Typed API client for all backend communication.
 */

const API_BASE = (() => {
  // Check for explicit env override
  if (import.meta.env.VITE_API_URL) return import.meta.env.VITE_API_URL;
  // Local development
  if (
    window.location.hostname === 'localhost' ||
    window.location.hostname === '127.0.0.1'
  ) {
    return 'http://127.0.0.1:8000/api';
  }
  // Production (relative path)
  return '/api';
})();

class ApiError extends Error {
  public status: number;
  public endpoint: string;

  constructor(status: number, endpoint: string, message: string) {
    super(message);
    this.status = status;
    this.endpoint = endpoint;
    this.name = 'ApiError';
  }
}

async function apiGet<T>(endpoint: string): Promise<T> {
  const cleanEp = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  const res = await fetch(`${API_BASE}${cleanEp}`);
  if (!res.ok) {
    throw new ApiError(res.status, endpoint, `HTTP ${res.status} from ${endpoint}`);
  }
  return res.json();
}

async function apiPost<T>(endpoint: string, body: unknown): Promise<T> {
  const cleanEp = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  const res = await fetch(`${API_BASE}${cleanEp}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    throw new ApiError(res.status, endpoint, `HTTP ${res.status} from ${endpoint}`);
  }
  return res.json();
}

// ---- Typed API Functions ----

import type {
  DashboardData,
  Hospital,
  RescueTeam,
  EmergencyAlert,
  CitizenReport,
  ResourceData,
  ResourceItem,
  Shelter,
  Prediction,
  PredictionData,
  WeatherForecast,
  ChatbotResponse,
} from '../types';

export const api = {
  // Dashboard
  getDashboard: () => apiGet<DashboardData>('/dashboard/'),

  // Hospitals
  getHospitals: () => apiGet<Hospital[]>('/hospitals/'),

  // Rescue Teams
  getRescueTeams: () => apiGet<RescueTeam[]>('/rescue/'),

  // Alerts
  getActiveAlerts: () => apiGet<EmergencyAlert[]>('/alerts/active'),
  getAllAlerts: () => apiGet<EmergencyAlert[]>('/alerts/'),

  // Citizen Reports
  getReports: () => apiGet<CitizenReport[]>('/reports/'),
  submitReport: (data: Record<string, unknown>) =>
    apiPost<{ status: string }>('/reports/', data),

  // Resources
  getResources: () => apiGet<ResourceData>('/resources/'),
  getResourceItems: () => apiGet<ResourceItem[]>('/resources/items'),
  getShelters: () => apiGet<Shelter[]>('/resources/shelters'),
  requestResource: (data: { name: string; quantity: number; district: string }) =>
    apiPost<{ status: string }>('/resources/items', data),

  // Predictions
  getPredictions: () => apiGet<PredictionData>('/prediction/'),
  getAllPredictions: () => apiGet<Prediction[]>('/prediction/all'),

  // Weather
  getWeather: () =>
    apiGet<{ district_forecast: WeatherForecast[] }>('/weather/'),
  getHeavyRain: () => apiGet<WeatherForecast[]>('/weather/heavy-rain'),

  // Chatbot
  queryChatbot: (message: string) =>
    apiPost<ChatbotResponse>('/chatbot/query', { message }),

  // Health
  healthCheck: () => apiGet<{ status: string }>('/health'),
};

export { ApiError, API_BASE };
export default api;
