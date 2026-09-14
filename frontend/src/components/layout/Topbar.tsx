/**
 * Topbar — Application header with brand, search, and actions.
 */
import React from 'react';
import { useTheme } from '../../hooks/useTheme';
import { Button } from '../ui';
import './layout.css';

interface TopbarProps {
  onToggleSidebar: () => void;
  onOpenAICopilot: () => void;
  searchQuery: string;
  onSearchChange: (query: string) => void;
  isConnected: boolean;
}

export const Topbar: React.FC<TopbarProps> = ({
  onToggleSidebar,
  onOpenAICopilot,
  searchQuery,
  onSearchChange,
  isConnected,
}) => {
  const { theme, toggle } = useTheme();

  return (
    <header className="topbar">
      {/* Brand & Sidebar Toggle */}
      <div className="topbar__brand">
        <div className="topbar__logo">
          <i className="ti ti-droplet-half-2" />
        </div>
        <span className="font-sans">VARUNA AI</span>
      </div>

      <button className="topbar__toggle-btn" onClick={onToggleSidebar} aria-label="Toggle Sidebar">
        <i className="ti ti-menu-2" />
      </button>

      {/* Global Search */}
      <div className="topbar__search">
        <i className="ti ti-search" />
        <input
          type="text"
          placeholder="Search locations, units, reports (Press '/')"
          value={searchQuery}
          onChange={(e) => onSearchChange(e.target.value)}
        />
      </div>

      {/* Right Actions */}
      <div className="topbar__actions">
        {/* Connection Status */}
        <div className="topbar__status" title={isConnected ? 'Connected to live database' : 'Operating in offline mode'}>
          <span className={`status-dot ${isConnected ? 'status-dot--live' : 'status-dot--offline'}`} />
          <span className="sr-only">{isConnected ? 'Live' : 'Offline'}</span>
          <span className="topbar__status-text">{isConnected ? 'LIVE' : 'OFFLINE'}</span>
        </div>

        {/* AI Copilot Toggle */}
        <Button variant="ghost" className="icon-btn" onClick={onOpenAICopilot} aria-label="Open AI Copilot">
          <i className="ti ti-brain" />
          <span className="icon-btn__badge" />
        </Button>

        {/* Theme Toggle */}
        <div className="theme-toggle">
          <button
            className={theme === 'light' ? 'active' : ''}
            onClick={() => toggle()}
            aria-label="Light theme"
          >
            <i className="ti ti-sun" />
          </button>
          <button
            className={theme === 'dark' ? 'active' : ''}
            onClick={() => toggle()}
            aria-label="Dark theme"
          >
            <i className="ti ti-moon" />
          </button>
        </div>

        {/* User Profile */}
        <div className="profile-btn">
          SG
        </div>
      </div>
    </header>
  );
};
