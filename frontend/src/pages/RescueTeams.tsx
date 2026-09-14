/**
 * RescueTeams — Field unit tracking and deployment.
 */
import React from 'react';
import { useApi } from '../hooks/useApi';
import { api } from '../services/api';
import { Card, SectionLabel, LoadingState, ErrorState, Badge } from '../components/ui';
import type { RescueTeam } from '../types';

export const RescueTeams: React.FC = () => {
  const { data: teams, loading, error, refetch } = useApi<RescueTeam[]>(api.getRescueTeams);

  if (loading) return <LoadingState count={4} />;
  if (error) return <ErrorState message={error} onRetry={refetch} />;
  if (!teams) return null;

  return (
    <div className="animate-fade-up">
      <div className="view-head">
        <div>
          <h1>Rescue Teams & Field Units</h1>
          <p>Live tracking of NDRF, SDRF, and Military relief deployments.</p>
        </div>
      </div>

      <SectionLabel icon="shield" title="Active Deployments" />
      <Card style={{ padding: 0, overflow: 'hidden' }}>
        <table>
          <thead>
            <tr>
              <th>Unit Designation</th>
              <th>Force Type</th>
              <th>District Location</th>
              <th>Personnel</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {teams.map((t: RescueTeam) => (
              <tr key={t.id}>
                <td style={{ fontWeight: 600 }}>{t.name}</td>
                <td><span className="text-dim">{t.type}</span></td>
                <td>{t.location}</td>
                <td className="font-mono">{t.members || t.personnel_count}</td>
                <td>
                  <Badge variant={t.status.toLowerCase() === 'deployed' ? 'info' : 'ok'}>
                    {t.status}
                  </Badge>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
};
