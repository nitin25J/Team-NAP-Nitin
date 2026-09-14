/**
 * useTheme — Dark/light theme management hook.
 */
import { useState, useEffect, useCallback } from 'react';
import type { Theme } from '../types';

export function useTheme() {
  const [theme, setThemeState] = useState<Theme>(() => {
    const stored = localStorage.getItem('varuna-theme');
    return (stored === 'light' ? 'light' : 'dark') as Theme;
  });

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('varuna-theme', theme);
  }, [theme]);

  const setTheme = useCallback((t: Theme) => setThemeState(t), []);
  const toggle = useCallback(
    () => setThemeState((prev) => (prev === 'dark' ? 'light' : 'dark')),
    []
  );

  return { theme, setTheme, toggle };
}
