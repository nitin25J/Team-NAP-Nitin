/**
 * Settings — System configuration.
 */
import React from 'react';
import { Card, SectionLabel, Button } from '../components/ui';

export const Settings: React.FC = () => {
  return (
    <div className="animate-fade-up">
      <div className="view-head">
        <div>
          <h1>System Configuration</h1>
          <p>Varuna AI command center preferences.</p>
        </div>
      </div>

      <SectionLabel icon="settings" title="Application Settings" />
      <div style={{ maxWidth: '600px', display: 'flex', flexDirection: 'column', gap: 'var(--sp-4)' }}>
        <Card>
          <h3 style={{ fontSize: '15px', marginBottom: '16px' }}>Network Connection</h3>
          <div className="form-group">
            <label>API Endpoint Override</label>
            <input type="text" className="form-control" placeholder="Default: Auto-detected from environment" />
          </div>
          <Button variant="primary" style={{ marginTop: '8px' }}>Test Connection</Button>
        </Card>
        
        <Card>
          <h3 style={{ fontSize: '15px', marginBottom: '16px', color: 'var(--alert)' }}>Danger Zone</h3>
          <p style={{ fontSize: '13px', color: 'var(--text-dim)', marginBottom: '16px' }}>
            System reset actions require Director General authorization.
          </p>
          <Button variant="danger" icon="alert-triangle">Reset Database Cache</Button>
        </Card>
      </div>
    </div>
  );
};
