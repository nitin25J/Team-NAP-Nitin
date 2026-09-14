/**
 * Resources — Inventory and logistics management.
 */
import React from 'react';
import { useApi } from '../hooks/useApi';
import { api } from '../services/api';
import { Card, SectionLabel, LoadingState, ErrorState, ProgressBar } from '../components/ui';
import type { ResourceData, ResourceItem, Shelter } from '../types';

export const Resources: React.FC = () => {
  const { data, loading, error, refetch } = useApi<ResourceData>(api.getResources);

  if (loading) return <LoadingState count={4} />;
  if (error) return <ErrorState message={error} onRetry={refetch} />;
  if (!data) return null;

  const { inventory, shelters } = data;

  return (
    <div className="animate-fade-up">
      <div className="view-head">
        <div>
          <h1>Resource Management & Relief</h1>
          <p>National disaster inventory and active relief camp occupancies.</p>
        </div>
      </div>

      <SectionLabel icon="package" title="Strategic Inventory" subtitle="Equipment and supplies currently tracked in Assam" />
      <div className="grid grid--4" style={{ marginBottom: 'var(--sp-8)' }}>
        {inventory.map((item: ResourceItem) => (
          <Card key={item.id}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
              <div style={{ fontSize: '13.5px', fontWeight: 600 }}>{item.name}</div>
              <div style={{ width: '36px', height: '36px', borderRadius: '10px', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'var(--surface-hi)', color: item.color }}>
                <i className={`ti ${item.icon}`} style={{ fontSize: '18px' }} />
              </div>
            </div>
            <ProgressBar have={item.have} total={item.total} color={item.color} />
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: 'var(--text-faint)', marginTop: '8px' }}>
              <span>Available: <strong style={{ color: 'var(--text)' }}>{item.have}</strong></span>
              <span>Total: {item.total}</span>
            </div>
          </Card>
        ))}
      </div>

      <SectionLabel icon="home" title="Active Relief Camps" subtitle="Currently operating shelters across affected districts" />
      <Card style={{ padding: 0, overflow: 'hidden' }}>
        <table>
          <thead>
            <tr>
              <th>Shelter Facility</th>
              <th>District</th>
              <th>Occupancy</th>
              <th>Capacity</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {shelters.map((s: Shelter) => {
              const pct = (s.occupancy / s.capacity) * 100;
              const statusColor = pct > 90 ? 'var(--alert)' : pct > 75 ? 'var(--warn)' : 'var(--safe)';
              
              return (
                <tr key={s.id}>
                  <td style={{ fontWeight: 500 }}>{s.name}</td>
                  <td>{s.district}</td>
                  <td>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                      <div style={{ width: '60px', height: '6px', background: 'var(--surface-hi)', borderRadius: '3px', overflow: 'hidden' }}>
                        <div style={{ width: `${pct}%`, height: '100%', background: statusColor }} />
                      </div>
                      <span className="font-mono text-dim">{s.occupancy}</span>
                    </div>
                  </td>
                  <td className="font-mono text-dim">{s.capacity}</td>
                  <td>
                    <span style={{ fontSize: '11px', color: statusColor, fontWeight: 500 }}>
                      {pct > 90 ? 'Critical Load' : pct > 75 ? 'High Load' : 'Available'}
                    </span>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </Card>
    </div>
  );
};
