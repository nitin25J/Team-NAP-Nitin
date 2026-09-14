/**
 * Varuna AI — Reusable UI Components
 * Buttons, Cards, Badges, Bars, and atomic UI pieces.
 */
import React from 'react';
import './ui.css';

// ---- Button ----
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'default' | 'primary' | 'danger' | 'ghost';
  icon?: string;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'default',
  icon,
  children,
  className = '',
  ...props
}) => (
  <button className={`btn btn--${variant} ${className}`} {...props}>
    {icon && <i className={`ti ti-${icon}`} />}
    {children}
  </button>
);

// ---- Card ----
interface CardProps {
  children: React.ReactNode;
  hoverable?: boolean;
  className?: string;
  style?: React.CSSProperties;
  onClick?: () => void;
}

export const Card: React.FC<CardProps> = ({
  children,
  hoverable,
  className = '',
  style,
  onClick,
}) => (
  <div
    className={`card ${hoverable ? 'card--hoverable' : ''} ${className}`}
    style={style}
    onClick={onClick}
    role={onClick ? 'button' : undefined}
    tabIndex={onClick ? 0 : undefined}
  >
    {children}
  </div>
);

// ---- Badge / Tag ----
interface BadgeProps {
  variant: 'critical' | 'severe' | 'moderate' | 'ok' | 'info';
  children: React.ReactNode;
}

export const Badge: React.FC<BadgeProps> = ({ variant, children }) => (
  <span className={`badge badge--${variant}`}>{children}</span>
);

// ---- Confidence Bar ----
interface ConfidenceBarProps {
  value: number; // 0-100
  gradient?: string;
}

export const ConfidenceBar: React.FC<ConfidenceBarProps> = ({ value, gradient }) => (
  <div className="confidence-bar">
    <div
      className="confidence-bar__fill"
      style={{
        width: `${Math.min(100, Math.max(0, value))}%`,
        ...(gradient ? { background: gradient } : {}),
      }}
    />
  </div>
);

// ---- Progress Bar ----
interface ProgressBarProps {
  have: number;
  total: number;
  color?: string;
}

export const ProgressBar: React.FC<ProgressBarProps> = ({ have, total, color }) => {
  const pct = total > 0 ? (have / total) * 100 : 0;
  return (
    <div className="progress">
      <div
        className="progress__fill"
        style={{ width: `${pct}%`, background: color || 'var(--primary)' }}
      />
    </div>
  );
};

// ---- Status Dot ----
interface StatusDotProps {
  color: string;
  label?: string;
}

export const StatusDot: React.FC<StatusDotProps> = ({ color, label }) => (
  <span className="status-indicator">
    <span className="status-dot" style={{ background: color }} />
    {label && <span>{label}</span>}
  </span>
);

// ---- KPI Card ----
interface KPICardProps {
  label: string;
  value: string | number;
  suffix?: string;
  icon: string;
  iconBg: string;
  iconColor: string;
  delta?: string;
  deltaType?: 'up' | 'down';
}

export const KPICard: React.FC<KPICardProps> = ({
  label,
  value,
  suffix = '',
  icon,
  iconBg,
  iconColor,
  delta,
  deltaType = 'up',
}) => (
  <Card hoverable className="kpi-card">
    <div className="kpi-card__top">
      <div className="kpi-card__icon" style={{ background: iconBg, color: iconColor }}>
        <i className={`ti ti-${icon}`} />
      </div>
      {delta && (
        <span className={`kpi-card__delta kpi-card__delta--${deltaType}`}>
          {delta}
        </span>
      )}
    </div>
    <div className="kpi-card__value font-display">
      {value}
      {suffix}
    </div>
    <div className="kpi-card__label">{label}</div>
  </Card>
);

// ---- Section Label ----
interface SectionLabelProps {
  icon: string;
  title: string;
  subtitle?: string;
}

export const SectionLabel: React.FC<SectionLabelProps> = ({ icon, title, subtitle }) => (
  <div className="section-label">
    <div className="section-label__icon">
      <i className={`ti ti-${icon}`} />
    </div>
    <div>
      <h3 className="section-label__title">{title}</h3>
      {subtitle && <p className="section-label__subtitle">{subtitle}</p>}
    </div>
  </div>
);

// ---- Empty State ----
interface EmptyStateProps {
  icon: string;
  title: string;
  message?: string;
}

export const EmptyState: React.FC<EmptyStateProps> = ({ icon, title, message }) => (
  <div className="empty-state">
    <i className={`ti ti-${icon}`} />
    <h3>{title}</h3>
    {message && <p>{message}</p>}
  </div>
);

// ---- Loading State ----
export const LoadingState: React.FC<{ count?: number }> = ({ count = 3 }) => (
  <div className="loading-state">
    {Array.from({ length: count }).map((_, i) => (
      <div key={i} className="skeleton skeleton--card" />
    ))}
  </div>
);

// ---- Error State ----
interface ErrorStateProps {
  message: string;
  onRetry?: () => void;
}

export const ErrorState: React.FC<ErrorStateProps> = ({ message, onRetry }) => (
  <div className="error-state">
    <i className="ti ti-alert-triangle" />
    <h3>Something went wrong</h3>
    <p>{message}</p>
    {onRetry && (
      <Button variant="ghost" icon="refresh" onClick={onRetry}>
        Retry
      </Button>
    )}
  </div>
);

// ---- Severity Ring (Dashboard center widget) ----
interface SeverityRingProps {
  score: number;
  label: string;
  subtitle: string;
}

export const SeverityRing: React.FC<SeverityRingProps> = ({ score, label, subtitle }) => {
  const circumference = 2 * Math.PI * 70;
  const offset = circumference - (score / 100) * circumference;

  return (
    <Card className="ring-card">
      <div className="ring-card__glow" />
      <div className="ring-wrap">
        <svg viewBox="0 0 160 160">
          <defs>
            <linearGradient id="ringGrad" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stopColor="#FF6A4D" />
              <stop offset="100%" stopColor="#F5B94D" />
            </linearGradient>
          </defs>
          <circle className="ring-track" cx="80" cy="80" r="70" />
          <circle
            className="ring-fill"
            cx="80"
            cy="80"
            r="70"
            style={{
              strokeDasharray: circumference,
              strokeDashoffset: offset,
            }}
          />
        </svg>
        <div className="ring-center">
          <div className="ring-center__num font-display">{score}</div>
          <div className="ring-center__label">Severity /100</div>
        </div>
      </div>
      <div className="ring-foot">
        <div className="ring-foot__title">{label}</div>
        <div className="ring-foot__sub">{subtitle}</div>
      </div>
    </Card>
  );
};
