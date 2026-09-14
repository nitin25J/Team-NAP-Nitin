/**
 * Dashboard — Main command center view.
 */
import React from 'react';
import { useApi } from '../hooks/useApi';
import { api } from '../services/api';
import { KPICard, SeverityRing, SectionLabel, LoadingState, ErrorState, Card, Badge } from '../components/ui';
import type { DashboardData, TopDistrict } from '../types';

export const Dashboard: React.FC = () => {
  const { data, loading, error, refetch } = useApi<DashboardData>(api.getDashboard);

  if (loading) return <LoadingState count={6} />;
  if (error) return <ErrorState message={error} onRetry={refetch} />;
  if (!data) return null;

  const { overview_stats: stats, top_districts } = data;

  return (
    <div className="animate-fade-up">
      <div className="view-head">
        <div>
          <div className="eyebrow">National Disaster Response Force</div>
          <h1>Assam Flood Intelligence Command</h1>
          <p>Real-time telemetry and AI risk predictions across {stats.hospitals_monitored} monitored districts.</p>
        </div>
      </div>

      {/* Hero Section */}
      <div className="grid grid--3" style={{ marginBottom: 'var(--sp-6)' }}>
        <SeverityRing
          score={stats.max_severity_score}
          label="Peak Severity Level"
          subtitle={`Current State: ${stats.current_risk_level}`}
        />
        
        <div style={{ gridColumn: 'span 2' }} className="grid grid--2">
          <KPICard
            label="Active Emergency Alerts"
            value={stats.active_alerts}
            icon="bell-ringing"
            iconBg="var(--alert-dim)"
            iconColor="var(--alert)"
            delta="+2"
            deltaType="up"
          />
          <KPICard
            label="High Risk Districts"
            value={stats.high_risk_districts}
            icon="map-pin-exclamation"
            iconBg="var(--warn-dim)"
            iconColor="var(--warn)"
          />
          <KPICard
            label="Rescue Teams Deployed"
            value={stats.rescue_teams_deployed}
            icon="shield"
            iconBg="var(--primary-dim)"
            iconColor="var(--primary)"
          />
          <KPICard
            label="Est. Population Affected"
            value={stats.total_population_affected.toLocaleString()}
            icon="users"
            iconBg="var(--blue-dim)"
            iconColor="var(--blue)"
          />
        </div>
      </div>

      {/* Critical Sectors */}
      <SectionLabel icon="alert-triangle" title="Critical Sectors" subtitle="Districts requiring immediate attention based on AI severity scoring" />
      
      <Card style={{ padding: 0, overflow: 'hidden' }}>
        <table>
          <thead>
            <tr>
              <th>District</th>
              <th>Primary River</th>
              <th>Risk Level</th>
              <th>Severity</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {top_districts.map((d: TopDistrict, i: number) => (
              <tr key={i}>
                <td style={{ fontWeight: 600 }}>{d.district}</td>
                <td>{d.river}</td>
                <td>
                  <Badge variant={
                    d.risk_level.toLowerCase().includes('extreme') ? 'critical' :
                    d.risk_level.toLowerCase().includes('high') ? 'severe' : 'moderate'
                  }>
                    {d.risk_level}
                  </Badge>
                </td>
                <td className="font-mono">{d.severity_score}/100</td>
                <td className="text-dim">{d.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
};
