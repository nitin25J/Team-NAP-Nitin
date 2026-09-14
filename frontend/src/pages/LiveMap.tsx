/**
 * Live Disaster Map — Leaflet integration with interactive layers.
 */
import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Circle, Marker, Tooltip, useMap } from 'react-leaflet';
import L from 'leaflet';
import { Card, SectionLabel } from '../components/ui';

// Fix for default Leaflet icons in React
delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
});

const GUWAHATI: [number, number] = [26.1445, 91.7362];

// Custom DivIcon creator for our status dots
const createCustomIcon = (color: string, iconClass: string) => {
  const html = `
    <div style="width:26px;height:26px;border-radius:50%;background:${color};display:flex;align-items:center;justify-content:center;border:2px solid #0E1B26;box-shadow:0 0 0 2px ${color}55;">
      <i class="ti ${iconClass}" style="font-size:13px;color:#04211f"></i>
    </div>
  `;
  return L.divIcon({ html, className: '', iconSize: [26, 26], iconAnchor: [13, 13] });
};

// Component to handle map resizing when sidebar toggles or tab switches
const MapResizer = () => {
  const map = useMap();
  useEffect(() => {
    const resizeObserver = new ResizeObserver(() => {
      map.invalidateSize();
    });
    const container = document.getElementById('map-container');
    if (container) resizeObserver.observe(container);
    return () => resizeObserver.disconnect();
  }, [map]);
  return null;
};

export const LiveMap: React.FC = () => {
  const [activeLayers, setActiveLayers] = useState<Record<string, boolean>>({
    flood: true,
    hospitals: true,
    units: true,
    sensors: true,
  });

  const toggleLayer = (layer: string) => {
    setActiveLayers((prev) => ({ ...prev, [layer]: !prev[layer] }));
  };

  const layers = [
    { id: 'flood', label: 'Flood Zones', color: 'var(--blue)' },
    { id: 'hospitals', label: 'Hospitals', color: 'var(--safe)' },
    { id: 'shelters', label: 'Relief Camps', color: 'var(--primary)' },
    { id: 'units', label: 'Rescue Units', color: 'var(--blue)' },
    { id: 'sensors', label: 'IoT Sensors', color: 'var(--safe)' },
    { id: 'radar', label: 'Weather Radar', color: 'var(--text-dim)' },
    { id: 'drones', label: 'Drone Feeds', color: 'var(--violet)' },
  ];

  return (
    <div className="animate-fade-up">
      <div className="view-head">
        <div>
          <h1>Live Disaster Map</h1>
          <p>Real-time telemetry, resource tracking, and geospatial risk overlays.</p>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 300px', gap: 'var(--sp-4)' }}>
        {/* Map Container */}
        <Card style={{ padding: 0, overflow: 'hidden' }}>
          <div id="map-container" style={{ height: '100%', width: '100%' }}>
          <MapContainer center={GUWAHATI} zoom={9} style={{ height: '600px', width: '100%' }}>
            <MapResizer />
            <TileLayer
              attribution='&copy; <a href="https://carto.com/">CARTO</a>'
              url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
              subdomains="abcd"
              maxZoom={19}
            />

            {/* Simulated Data Layers (will be replaced with real API data) */}
            {activeLayers.flood && (
              <Circle center={[26.10, 91.90]} radius={15000} pathOptions={{ color: '#5B9CFF', fillColor: '#5B9CFF', fillOpacity: 0.25, weight: 1 }} />
            )}
            
            {activeLayers.radar && (
              <Circle center={GUWAHATI} radius={40000} pathOptions={{ color: '#8CA3AE', fillColor: '#8CA3AE', fillOpacity: 0.06, weight: 1, dashArray: '4,6' }} />
            )}

            {activeLayers.hospitals && (
              <>
                <Marker position={[26.13, 91.80]} icon={createCustomIcon('#3ED598', 'ti-building-hospital')}>
                  <Tooltip direction="top" offset={[0, -10]}>Guwahati Medical College · 88% ICU</Tooltip>
                </Marker>
                <Marker position={[26.98, 94.64]} icon={createCustomIcon('#3ED598', 'ti-building-hospital')}>
                  <Tooltip direction="top" offset={[0, -10]}>Sivasagar Civil Hospital · 100% ICU</Tooltip>
                </Marker>
              </>
            )}

            {activeLayers.units && (
              <>
                <Marker position={[26.145, 91.83]} icon={createCustomIcon('#5B9CFF', 'ti-truck')}>
                  <Tooltip direction="top" offset={[0, -10]}>NDRF Team Alpha · en route</Tooltip>
                </Marker>
                <Marker position={[26.75, 94.20]} icon={createCustomIcon('#5B9CFF', 'ti-anchor')}>
                  <Tooltip direction="top" offset={[0, -10]}>SDRF Boat Unit · deployed</Tooltip>
                </Marker>
              </>
            )}

            {activeLayers.sensors && (
              <>
                <Marker position={[26.15, 91.95]} icon={createCustomIcon('#3ED598', 'ti-antenna')}>
                  <Tooltip direction="top" offset={[0, -10]}>River gauge · Brahmaputra</Tooltip>
                </Marker>
              </>
            )}
          </MapContainer>
          </div>
        </Card>

        {/* Controls Sidebar */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--sp-4)' }}>
          <Card>
            <SectionLabel icon="layers-intersect" title="Map Overlays" />
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', marginTop: '12px' }}>
              {layers.map((layer) => (
                <button
                  key={layer.id}
                  onClick={() => toggleLayer(layer.id)}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '7px',
                    padding: '7px 12px',
                    borderRadius: '20px',
                    border: `1px solid ${activeLayers[layer.id] ? layer.color : 'var(--border)'}`,
                    background: activeLayers[layer.id] ? 'var(--surface-hi)' : 'var(--surface)',
                    color: activeLayers[layer.id] ? 'var(--text)' : 'var(--text-dim)',
                    fontSize: '11.5px',
                    cursor: 'pointer',
                    transition: 'all 0.2s',
                  }}
                >
                  <span style={{ width: '8px', height: '8px', borderRadius: '50%', background: layer.color }} />
                  {layer.label}
                </button>
              ))}
            </div>
          </Card>

          <Card>
            <SectionLabel icon="activity" title="Live Telemetry" />
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', marginTop: '12px' }}>
              <div style={{ fontSize: '12px', color: 'var(--text-dim)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}>
                  <span>Brahmaputra Level</span>
                  <span className="font-mono text-alert">86.8m</span>
                </div>
                <div style={{ width: '100%', height: '4px', background: 'var(--surface-hi)', borderRadius: '2px' }}>
                  <div style={{ width: '90%', height: '100%', background: 'var(--alert)', borderRadius: '2px' }} />
                </div>
                <div style={{ fontSize: '10px', marginTop: '4px', textAlign: 'right' }}>Danger: 85.5m</div>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
};
