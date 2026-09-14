/**
 * Sidebar — Main navigation rail with collapsible sections.
 */
import React from 'react';
import type { ViewId } from '../../types';
import './layout.css';

interface NavItem {
  id: ViewId;
  label: string;
  icon: string;
  section: string;
}

const NAV_ITEMS: NavItem[] = [
  // Command
  { id: 'dashboard', label: 'Dashboard', icon: 'layout-dashboard', section: 'Command' },
  { id: 'map', label: 'Live Disaster Map', icon: 'map-2', section: 'Command' },
  { id: 'ai', label: 'AI Risk Prediction', icon: 'brain', section: 'Command' },
  // Response
  { id: 'resources', label: 'Resource Management', icon: 'package', section: 'Response' },
  { id: 'hospitals', label: 'Hospitals', icon: 'building-hospital', section: 'Response' },
  { id: 'rescue', label: 'Rescue Teams', icon: 'shield', section: 'Response' },
  { id: 'alerts', label: 'Emergency Alerts', icon: 'bell-ringing', section: 'Response' },
  // Intelligence
  { id: 'satellite', label: 'Satellite Analysis', icon: 'satellite', section: 'Intelligence' },
  { id: 'reports', label: 'Citizen Reports', icon: 'file-text', section: 'Intelligence' },
  { id: 'analytics', label: 'Analytics', icon: 'chart-bar', section: 'Intelligence' },
  // System
  { id: 'settings', label: 'Settings', icon: 'settings', section: 'System' },
];

interface SidebarProps {
  currentView: ViewId;
  collapsed: boolean;
  onNavigate: (view: ViewId) => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ currentView, collapsed, onNavigate }) => {
  return (
    <nav className="sidebar" role="navigation" aria-label="Main navigation">
      {Object.entries(
        NAV_ITEMS.reduce((acc, item) => {
          if (!acc[item.section]) acc[item.section] = [];
          acc[item.section].push(item);
          return acc;
        }, {} as Record<string, NavItem[]>)
      ).map(([section, items]) => (
        <React.Fragment key={section}>
          <div className="sidebar__section-label">{section}</div>
          {items.map((item) => (
            <button
              key={item.id}
              className={`sidebar__item ${currentView === item.id ? 'sidebar__item--active' : ''}`}
              onClick={() => onNavigate(item.id)}
              title={collapsed ? item.label : undefined}
              aria-current={currentView === item.id ? 'page' : undefined}
            >
              <i className={`ti ti-${item.icon}`} />
              {!collapsed && <span>{item.label}</span>}
            </button>
          ))}
        </React.Fragment>
      ))}
    </nav>
  );
};
