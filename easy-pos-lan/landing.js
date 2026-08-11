(function () {
  const root = document.documentElement;
  const toggle = document.getElementById('theme-toggle');
  if (!toggle) {
    return;
  }
  const storage = (() => {
    try {
      return window.localStorage;
    } catch (_) {
      return null;
    }
  })();
  let savedTheme = null;
  if (storage) {
    try {
      savedTheme = storage.getItem('easy-pos-theme');
    } catch (_) {
      savedTheme = null;
    }
  }
  const initialTheme = savedTheme === 'light' ? 'light' : 'dark';

  function applyTheme(theme) {
    const isLight = theme === 'light';
    root.dataset.theme = theme;
    toggle.setAttribute('aria-pressed', String(isLight));
    toggle.setAttribute('aria-label', isLight ? 'Cambiar a modo oscuro' : 'Cambiar a modo claro');
    toggle.querySelector('.theme-icon').textContent = isLight ? '◐' : '☼';
    toggle.querySelector('.theme-label').textContent = isLight ? 'Modo oscuro' : 'Modo claro';
    if (storage) {
      try {
        storage.setItem('easy-pos-theme', theme);
      } catch (_) {
        // Private/file origins can deny persistence; the current session still works.
      }
    }
  }

  applyTheme(initialTheme);
  toggle.addEventListener('click', function () {
    applyTheme(root.dataset.theme === 'dark' ? 'light' : 'dark');
  });
}());
