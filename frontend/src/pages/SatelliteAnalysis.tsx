/**
 * Satellite Analysis — Placeholder for GIS data.
 */
import React from 'react';
import { Card, SectionLabel, EmptyState } from '../components/ui';

export const SatelliteAnalysis: React.FC = () => {
  return (
    <div className="animate-fade-up">
      <div className="view-head">
        <div>
          <h1>Satellite Intelligence</h1>
          <p>Optical and SAR (Synthetic Aperture Radar) analysis.</p>
        </div>
      </div>

      <SectionLabel icon="satellite" title="ISRO/ESA Feed Integration" />
      <Card style={{ minHeight: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <EmptyState 
          icon="satellite" 
          title="Satellite Feeds Unavailable" 
          message="Direct connection to ISRO Bhuvan portal is required for live imagery. Waiting for authorization credentials." 
        />
      </Card>
    </div>
  );
};
