import { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate, useNavigate, useLocation } from 'react-router-dom';
import { AppShell } from './components/layout/AppShell';
import { Dashboard } from './pages/Dashboard';
import { LiveMap } from './pages/LiveMap';
import { AIPrediction } from './pages/AIPrediction';
import { Resources } from './pages/Resources';
import { Hospitals } from './pages/Hospitals';
import { RescueTeams } from './pages/RescueTeams';
import { Alerts } from './pages/Alerts';
import { CitizenReports } from './pages/CitizenReports';
import { SatelliteAnalysis } from './pages/SatelliteAnalysis';
import { Analytics } from './pages/Analytics';
import { Settings } from './pages/Settings';
import { api } from './services/api';
import type { ViewId } from './types';

// Wrapper to handle navigation state
const AppContent = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const [isConnected, setIsConnected] = useState(true);

  // Check connection status periodically
  useEffect(() => {
    const checkConnection = async () => {
      try {
        await api.healthCheck();
        setIsConnected(true);
      } catch {
        setIsConnected(false);
      }
    };
    checkConnection();
    const interval = setInterval(checkConnection, 30000);
    return () => clearInterval(interval);
  }, []);

  // Map path to view ID
  const getCurrentView = (): ViewId => {
    const path = location.pathname.substring(1);
    return (path || 'dashboard') as ViewId;
  };

  const handleNavigate = (view: ViewId) => {
    navigate(`/${view}`);
  };

  return (
    <AppShell
      currentView={getCurrentView()}
      onNavigate={handleNavigate}
      isConnected={isConnected}
    >
      <Routes>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/map" element={<LiveMap />} />
        <Route path="/ai" element={<AIPrediction />} />
        <Route path="/resources" element={<Resources />} />
        <Route path="/hospitals" element={<Hospitals />} />
        <Route path="/rescue" element={<RescueTeams />} />
        <Route path="/alerts" element={<Alerts />} />
        <Route path="/reports" element={<CitizenReports />} />
        <Route path="/satellite" element={<SatelliteAnalysis />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </AppShell>
  );
};

export const App = () => {
  return (
    <BrowserRouter>
      <AppContent />
    </BrowserRouter>
  );
};
