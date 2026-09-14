/**
 * AI Prediction — Real-time risk analysis and modeling engine UI.
 */
import React, { useState } from 'react';
import { useApi } from '../hooks/useApi';
import { api } from '../services/api';
import { Card, ConfidenceBar, Badge, LoadingState, ErrorState, SectionLabel } from '../components/ui';
import type { PredictionData, Prediction } from '../types';

export const AIPrediction: React.FC = () => {
  const { data, loading, error, refetch } = useApi<PredictionData>(api.getPredictions);
  const [selectedDistrict, setSelectedDistrict] = useState<string | null>(null);

  if (loading) return <LoadingState count={4} />;
  if (error) return <ErrorState message={error} onRetry={refetch} />;
  if (!data) return null;

  const { predictions, model_name, last_run } = data;
  const activePred = selectedDistrict 
    ? predictions.find((p: Prediction) => p.district === selectedDistrict) 
    : predictions[0];

  return (
    <div className="animate-fade-up">
      <div className="view-head">
        <div>
          <div className="eyebrow">{model_name}</div>
          <h1>AI Risk Prediction Engine</h1>
          <p>Fusing real-time hydrological data with meteorological forecasting models. (Last run: {new Date(last_run).toLocaleTimeString()})</p>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '320px 1fr', gap: 'var(--sp-6)' }}>
        {/* District List */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-2)' }}>
          <SectionLabel icon="map-2" title="Monitored Districts" />
          {predictions.map((p: Prediction) => (
            <Card 
              key={p.district}
              hoverable
              onClick={() => setSelectedDistrict(p.district)}
              style={{
                cursor: 'pointer',
                border: activePred?.district === p.district ? '1px solid var(--primary)' : undefined,
                background: activePred?.district === p.district ? 'var(--primary-dim)' : undefined,
                padding: '12px 16px',
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                <span style={{ fontWeight: 600 }}>{p.district}</span>
                <Badge variant={p.risk_level.includes('Extreme') ? 'critical' : p.risk_level.includes('High') ? 'severe' : 'moderate'}>
                  {p.risk_level}
                </Badge>
              </div>
              <div style={{ fontSize: '11px', color: 'var(--text-dim)', display: 'flex', justifyContent: 'space-between' }}>
                <span>Severity: <strong style={{ color: 'var(--text)' }}>{p.severity_score}/100</strong></span>
                <span>Rain: {p.rainfall_mm_24h}mm</span>
              </div>
            </Card>
          ))}
        </div>

        {/* Detailed Analysis */}
        {activePred && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-4)' }}>
            <SectionLabel icon="brain" title="Inference Details" subtitle={`Analysis for ${activePred.district}`} />
            
            <Card>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 'var(--sp-4)', marginBottom: 'var(--sp-6)' }}>
                <div>
                  <div style={{ fontSize: '11px', color: 'var(--text-faint)', textTransform: 'uppercase' }}>Water Level</div>
                  <div style={{ fontSize: '24px', fontWeight: 600, fontFamily: 'var(--font-mono)' }}>{activePred.water_level_m}m</div>
                  <div style={{ fontSize: '11px', color: 'var(--alert)' }}>Danger: {activePred.danger_mark_m}m</div>
                </div>
                <div>
                  <div style={{ fontSize: '11px', color: 'var(--text-faint)', textTransform: 'uppercase' }}>24h Rainfall</div>
                  <div style={{ fontSize: '24px', fontWeight: 600, fontFamily: 'var(--font-mono)' }}>{activePred.rainfall_mm_24h}mm</div>
                </div>
                <div>
                  <div style={{ fontSize: '11px', color: 'var(--text-faint)', textTransform: 'uppercase' }}>Wind Speed</div>
                  <div style={{ fontSize: '24px', fontWeight: 600, fontFamily: 'var(--font-mono)' }}>{activePred.wind_speed_kmh}km/h</div>
                </div>
              </div>

              <div style={{ borderTop: '1px solid var(--border)', paddingTop: 'var(--sp-4)', marginBottom: 'var(--sp-4)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                  <span style={{ fontSize: '12px', fontWeight: 500 }}>Model Confidence</span>
                  <span style={{ fontSize: '12px', fontFamily: 'var(--font-mono)' }}>{Math.round(activePred.confidence * 100)}%</span>
                </div>
                <ConfidenceBar value={activePred.confidence * 100} />
              </div>

              <div>
                <h4 style={{ fontSize: '13px', marginBottom: '12px', color: 'var(--text-dim)' }}>AI Recommendations</h4>
                <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  {activePred.recommendations.map((rec: string, i: number) => (
                    <li key={i} style={{ display: 'flex', gap: '10px', fontSize: '13px', padding: '10px', background: 'var(--surface-hi)', borderRadius: 'var(--r-sm)' }}>
                      <i className="ti ti-check" style={{ color: 'var(--primary)', marginTop: '2px' }} />
                      <span>{rec}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </Card>
          </div>
        )}
      </div>
    </div>
  );
};
