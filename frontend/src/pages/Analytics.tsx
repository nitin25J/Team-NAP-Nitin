/**
 * Analytics — Historical data and performance charts.
 */
import React from 'react';
import { Card, SectionLabel, EmptyState } from '../components/ui';

export const Analytics: React.FC = () => {
  return (
    <div className="animate-fade-up">
      <div className="view-head">
        <div>
          <h1>Analytics & Reporting</h1>
          <p>Historical trends, response times, and resource utilization analysis.</p>
        </div>
      </div>

      <SectionLabel icon="chart-bar" title="Performance Metrics" />
      <Card style={{ minHeight: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <EmptyState 
          icon="chart-histogram" 
          title="Analytics Module Inactive" 
          message="Chart.js integration is being finalized. Historical data views will be available in the next release." 
        />
      </Card>
    </div>
  );
};
