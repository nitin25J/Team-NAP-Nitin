/**
 * Citizen Reports — Crowd-sourced distress signals.
 */
import React from 'react';
import { useApi } from '../hooks/useApi';
import { api } from '../services/api';
import { Card, SectionLabel, LoadingState, ErrorState, Badge } from '../components/ui';
import type { CitizenReport } from '../types';

export const CitizenReports: React.FC = () => {
  const { data: reports, loading, error, refetch } = useApi<CitizenReport[]>(api.getReports);

  if (loading) return <LoadingState count={6} />;
  if (error) return <ErrorState message={error} onRetry={refetch} />;
  if (!reports) return null;

  return (
    <div className="animate-fade-up">
      <div className="view-head">
        <div>
          <h1>Citizen Distress Reports</h1>
          <p>Crowd-sourced field reports with AI verification status.</p>
        </div>
      </div>

      <SectionLabel icon="file-text" title="Recent Field Submissions" />
      <div className="grid grid--3">
        {reports.map((report: CitizenReport) => (
          <Card key={report.id} style={{ padding: '16px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <div style={{
              height: '140px',
              borderRadius: '12px',
              backgroundImage: `url(${report.image})`,
              backgroundSize: 'cover',
              backgroundPosition: 'center',
              position: 'relative'
            }}>
              {report.verified && (
                <div style={{
                  position: 'absolute',
                  top: '8px',
                  right: '8px',
                  background: 'var(--safe-dim)',
                  color: 'var(--safe)',
                  fontSize: '9.5px',
                  fontWeight: 700,
                  padding: '3px 8px',
                  borderRadius: '6px',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px'
                }}>
                  <i className="ti ti-discount-check-filled" /> AI Verified
                </div>
              )}
            </div>

            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                <div style={{ width: '26px', height: '26px', borderRadius: '50%', background: 'var(--surface-hi)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '12px', flexShrink: 0 }}>
                  <i className="ti ti-user" />
                </div>
                <span style={{ fontWeight: 600, fontSize: '13px' }}>{report.user || report.reporter_name}</span>
                <span style={{ fontSize: '10px', color: 'var(--text-faint)', marginLeft: 'auto', fontFamily: 'var(--font-mono)' }}>{report.time}</span>
              </div>
              
              <div style={{ fontSize: '12px', color: 'var(--text-dim)', display: 'flex', gap: '6px', marginBottom: '8px' }}>
                <i className="ti ti-map-pin" style={{ color: 'var(--primary)', flexShrink: 0, marginTop: '2px' }} />
                <span>{report.location}</span>
              </div>

              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 'auto', paddingTop: '8px', borderTop: '1px solid var(--border)' }}>
                <Badge variant={report.severity.toLowerCase() === 'critical' ? 'critical' : report.severity.toLowerCase() === 'moderate' ? 'moderate' : 'ok'}>
                  {report.severity}
                </Badge>
                <span style={{ fontSize: '11px', color: 'var(--text-faint)' }}>{report.status}</span>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};
