const header = document.querySelector('[data-header]');
const menuButton = document.querySelector('[data-menu-button]');
const mobileMenu = document.querySelector('[data-mobile-menu]');
const themeToggle = document.querySelector('[data-theme-toggle]');
const themeStorageKey = 'pos-estudio-theme';
const colorSchemeQuery = window.matchMedia?.('(prefers-color-scheme: light)');

const readStoredTheme = () => {
  try {
    const value = window.localStorage.getItem(themeStorageKey);
    return value === 'light' || value === 'dark' ? value : null;
  } catch {
    return null;
  }
};

const applyTheme = (theme, { persist = false } = {}) => {
  const normalizedTheme = theme === 'light' ? 'light' : 'dark';
  document.documentElement.dataset.theme = normalizedTheme;
  const isLight = normalizedTheme === 'light';
  const nextLabel = isLight ? 'Cambiar a tema oscuro' : 'Cambiar a tema claro';

  themeToggle?.setAttribute('aria-pressed', String(isLight));
  themeToggle?.setAttribute('aria-label', nextLabel);
  themeToggle?.setAttribute('title', nextLabel);

  document.querySelector('meta[name="theme-color"]')?.setAttribute(
    'content',
    isLight ? '#f6f8fc' : '#0b1020',
  );

  if (persist) {
    try {
      window.localStorage.setItem(themeStorageKey, normalizedTheme);
    } catch {
      // Private browsing can deny storage; the theme still applies for this visit.
    }
  }
};

const storedTheme = readStoredTheme();
applyTheme(storedTheme ?? (colorSchemeQuery?.matches ? 'light' : 'dark'));

themeToggle?.addEventListener('click', () => {
  const nextTheme = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
  applyTheme(nextTheme, { persist: true });
});

const handleSystemThemeChange = (event) => {
  if (!readStoredTheme()) applyTheme(event.matches ? 'light' : 'dark');
};

if (colorSchemeQuery?.addEventListener) {
  colorSchemeQuery.addEventListener('change', handleSystemThemeChange);
} else {
  colorSchemeQuery?.addListener?.(handleSystemThemeChange);
}

const closeMenu = () => {
  mobileMenu?.classList.remove('open');
  menuButton?.setAttribute('aria-expanded', 'false');
  menuButton?.setAttribute('aria-label', 'Abrir menú de navegación');
};

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') closeMenu();
});

document.addEventListener('click', (event) => {
  if (!mobileMenu?.classList.contains('open')) return;
  if (event.target instanceof Node && !mobileMenu.contains(event.target) && !menuButton?.contains(event.target)) {
    closeMenu();
  }
});

menuButton?.addEventListener('click', () => {
  const open = !mobileMenu?.classList.contains('open');
  mobileMenu?.classList.toggle('open', open);
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Cerrar menú de navegación' : 'Abrir menú de navegación');
});

mobileMenu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));

window.addEventListener('scroll', () => header?.classList.toggle('scrolled', window.scrollY > 12), { passive: true });

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));
document.querySelectorAll('[data-year]').forEach((element) => { element.textContent = new Date().getFullYear(); });

document.querySelector('[data-waitlist]')?.addEventListener('submit', (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const message = form.querySelector('[data-form-message]');
  message.textContent = 'La lista de espera se habilitará próximamente.';
  message.style.color = '#ffad78';
  form.reset();
});

// Keep the default content visible if JavaScript is unavailable or interrupted.
document.documentElement.classList.add('js');
