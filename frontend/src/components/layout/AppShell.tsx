/**
 * AppShell — Main application layout wrapper.
 */
import React, { useState } from 'react';
import { Sidebar } from './Sidebar';
import { Topbar } from './Topbar';
import type { ViewId } from '../../types';
import './layout.css';

interface AppShellProps {
  children: React.ReactNode;
  currentView: ViewId;
  onNavigate: (view: ViewId) => void;
  isConnected?: boolean;
}

export const AppShell: React.FC<AppShellProps> = ({
  children,
  currentView,
  onNavigate,
  isConnected = true,
}) => {
  const [collapsed, setCollapsed] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [isCopilotOpen, setIsCopilotOpen] = useState(false);

  return (
    <div className={`app-shell ${collapsed ? 'app-shell--collapsed' : ''}`}>
      <Topbar
        onToggleSidebar={() => setCollapsed(!collapsed)}
        onOpenAICopilot={() => setIsCopilotOpen(true)}
        searchQuery={searchQuery}
        onSearchChange={setSearchQuery}
        isConnected={isConnected}
      />
      <div className="app-shell__body">
        <Sidebar
          currentView={currentView}
          collapsed={collapsed}
          onNavigate={onNavigate}
        />
        <main className="app-shell__main" role="main">
          {children}
        </main>
      </div>

      {/* AI Copilot Drawer (Placeholder for now) */}
      {isCopilotOpen && (
        <div className="copilot-drawer">
          <div className="copilot-drawer__header">
            <h3>AI Copilot</h3>
            <button onClick={() => setIsCopilotOpen(false)}>
              <i className="ti ti-x" />
            </button>
          </div>
          <div className="copilot-drawer__body">
            <p>AI Copilot coming soon...</p>
          </div>
        </div>
      )}
    </div>
  );
};
