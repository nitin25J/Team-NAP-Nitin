/**
 * Hospitals — Medical facility monitoring.
 */
import React from 'react';
import { useApi } from '../hooks/useApi';
import { api } from '../services/api';
import { Card, SectionLabel, LoadingState, ErrorState, Badge } from '../components/ui';
import type { Hospital } from '../types';

export const Hospitals: React.FC = () => {
  const { data: hospitals, loading, error, refetch } = useApi<Hospital[]>(api.getHospitals);

  if (loading) return <LoadingState count={4} />;
  if (error) return <ErrorState message={error} onRetry={refetch} />;
  if (!hospitals) return null;

  return (
    <div className="animate-fade-up">
      <div className="view-head">
        <div>
          <h1>Medical Facilities</h1>
          <p>Live bed, ICU, and oxygen availability tracking across {hospitals.length} district hospitals.</p>
        </div>
      </div>

      <SectionLabel icon="building-hospital" title="Hospital Network Status" />
      <Card style={{ padding: 0, overflow: 'hidden' }}>
        <table>
          <thead>
            <tr>
              <th>Facility Name</th>
              <th>District</th>
              <th>Gen. Beds</th>
              <th>ICU Beds</th>
              <th>O2 Stock</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {hospitals.map((h: Hospital) => (
                <tr key={h.id}>
                  <td style={{ fontWeight: 500 }}>{h.name}</td>
                  <td>{h.district}</td>
                  <td>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span className="font-mono">{h.beds_available}/{h.beds_total}</span>
                    </div>
                  </td>
                  <td>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span className="font-mono" style={{ color: (h.icu_available / h.icu_total) * 100 < 20 ? 'var(--alert)' : 'inherit' }}>
                        {h.icu_available}/{h.icu_total}
                      </span>
                    </div>
                  </td>
                  <td>
                    {h.oxygen_available ? (
                      <span style={{ color: 'var(--safe)', fontSize: '16px' }}><i className="ti ti-circle-check-filled" /></span>
                    ) : (
                      <span style={{ color: 'var(--alert)', fontSize: '16px' }}><i className="ti ti-alert-circle-filled" /></span>
                    )}
                  </td>
                  <td>
                    <Badge variant={h.status.includes('Critical') ? 'critical' : h.status.includes('High') ? 'severe' : 'ok'}>
                      {h.status}
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
