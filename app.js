/* ==========================================================================
   IRIS SOFT - Interactive Client-Side Engine
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMobileMenu();
  initScrollReveal();
  initCarousel();
  initFormValidation();
});

/* ==========================================================================
   Light / Dark Mode Engine
   ========================================================================== */
function initTheme() {
  const themeToggle = document.getElementById('theme-toggle');
  const sunIcon = themeToggle.querySelector('.sun-icon');
  const moonIcon = themeToggle.querySelector('.moon-icon');
  
  // Read theme from localStorage or default to system dark preference
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
  
  if (savedTheme === 'light' || (!savedTheme && systemPrefersLight)) {
    enableLightMode();
  } else {
    enableDarkMode();
  }

  themeToggle.addEventListener('click', () => {
    const isLightMode = document.documentElement.classList.contains('light-mode');
    if (isLightMode) {
      enableDarkMode();
    } else {
      enableLightMode();
    }
  });

  function enableLightMode() {
    document.documentElement.classList.add('light-mode');
    localStorage.setItem('theme', 'light');
    sunIcon.style.display = 'block';
    moonIcon.style.display = 'none';
  }

  function enableDarkMode() {
    document.documentElement.classList.remove('light-mode');
    localStorage.setItem('theme', 'dark');
    sunIcon.style.display = 'none';
    moonIcon.style.display = 'block';
  }
}

/* ==========================================================================
   Mobile Navigation Menu Toggle
   ========================================================================== */
function initMobileMenu() {
  const menuToggle = document.getElementById('menu-toggle');
  const navMenu = document.getElementById('nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  menuToggle.addEventListener('click', () => {
    const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
    menuToggle.setAttribute('aria-expanded', !isExpanded);
    navMenu.classList.toggle('active');
  });

  // Close mobile menu on clicking any navigation anchor
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      menuToggle.setAttribute('aria-expanded', 'false');
      navMenu.classList.remove('active');
    });
  });

  // Close menu on clicking outside
  document.addEventListener('click', (e) => {
    if (!menuToggle.contains(e.target) && !navMenu.contains(e.target)) {
      menuToggle.setAttribute('aria-expanded', 'false');
      navMenu.classList.remove('remove');
      navMenu.classList.remove('active');
    }
  });
}

/* ==========================================================================
   IntersectionObserver for Elegant Scroll Reveals
   ========================================================================== */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal-on-scroll');
  
  const revealCallback = (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal-active');
        // Unobserve after revealing to prevent repeated trigger on scrolling
        observer.unobserve(entry.target);
      }
    });
  };

  const revealObserver = new IntersectionObserver(revealCallback, {
    root: null, // Viewport
    threshold: 0.15, // Trigger when 15% visible
    rootMargin: '0px 0px -50px 0px' // Slightly offset triggers for natural flow
  });

  revealElements.forEach(element => {
    revealObserver.observe(element);
  });
}

/* ==========================================================================
   Easy POS LAN Product Carousel Engine
   ========================================================================== */
function initCarousel() {
  const track = document.getElementById('carousel-track');
  const nextBtn = document.getElementById('carousel-next');
  const prevBtn = document.getElementById('carousel-prev');
  const slides = Array.from(track.children);
  
  if (slides.length <= 1) return;

  let currentIdx = 0;

  function updateCarousel() {
    const slideWidth = slides[0].getBoundingClientRect().width;
    track.scrollTo({
      left: currentIdx * (slideWidth + 32), // Add gap size
      behavior: 'smooth'
    });
  }

  nextBtn.addEventListener('click', () => {
    if (currentIdx < slides.length - 1) {
      currentIdx++;
    } else {
      currentIdx = 0; // Wrap around
    }
    updateCarousel();
  });

  prevBtn.addEventListener('click', () => {
    if (currentIdx > 0) {
      currentIdx--;
    } else {
      currentIdx = slides.length - 1; // Wrap around
    }
    updateCarousel();
  });

  // Listen to manual scrolling to update current index
  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      updateCarousel();
    }, 150);
  });
}

/* ==========================================================================
   Premium Interactive Contact Form Validation
   ========================================================================== */
function initFormValidation() {
  const form = document.getElementById('project-form');
  if (!form) return;

  const inputs = form.querySelectorAll('.form-input');

  // Input events to toggle custom states
  inputs.forEach(input => {
    input.addEventListener('blur', () => {
      // Standardize input state check
      input.checkValidity();
    });

    input.addEventListener('input', () => {
      // Remove visual error once typing resumes
      if (input.validity.valid) {
        input.style.borderColor = '';
      }
    });
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    let isFormValid = true;
    inputs.forEach(input => {
      if (!input.checkValidity()) {
        isFormValid = false;
      }
    });

    if (isFormValid) {
      // Gorgeous dynamic feedback popover instead of standard alerts
      showSuccessModal();
      form.reset();
    } else {
      // Scroll to first invalid field
      const firstInvalid = form.querySelector('.form-input:invalid');
      if (firstInvalid) {
        firstInvalid.focus();
      }
    }
  });

  function showSuccessModal() {
    const modal = document.createElement('div');
    modal.style.position = 'fixed';
    modal.style.inset = '0';
    modal.style.background = 'rgba(13, 17, 28, 0.85)';
    modal.style.backdropFilter = 'blur(16px)';
    modal.style.display = 'flex';
    modal.style.alignItems = 'center';
    modal.style.justifyContent = 'center';
    modal.style.zIndex = '2000';
    modal.style.opacity = '0';
    modal.style.transition = 'opacity 0.4s ease';

    const card = document.createElement('div');
    card.className = 'glass-card';
    card.style.padding = '3.5rem';
    card.style.maxWidth = '500px';
    card.style.width = '90%';
    card.style.textAlign = 'center';
    card.style.transform = 'translateY(30px)';
    card.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
    card.style.display = 'flex';
    card.style.flexDirection = 'column';
    card.style.alignItems = 'center';

    card.innerHTML = `
      <div style="width: 64px; height: 64px; border-radius: 50%; background: hsla(186, 100%, 46%, 0.15); border: 1px solid var(--accent-cyan); display: flex; align-items: center; justify-content: center; margin-bottom: 2rem; color: var(--accent-cyan);">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
      </div>
      <h3 style="font-size: 1.8rem; margin-bottom: 1rem; font-family: var(--font-heading);">¡Mensaje Recibido!</h3>
      <p style="color: var(--text-secondary); margin-bottom: 2.5rem; font-size: 0.95rem;">Gracias por ponerte en contacto con IRIsoft. Analizaremos tu idea y nos comunicaremos contigo de inmediato para agendar una llamada.</p>
      <button class="btn btn-primary" style="width: 100%;">Entendido</button>
    `;

    modal.appendChild(card);
    document.body.appendChild(modal);

    // Fade in
    setTimeout(() => {
      modal.style.opacity = '1';
      card.style.transform = 'translateY(0)';
    }, 50);

    const closeBtn = card.querySelector('button');
    closeBtn.addEventListener('click', () => {
      modal.style.opacity = '0';
      card.style.transform = 'translateY(30px)';
      setTimeout(() => {
        modal.remove();
      }, 400);
    });
  }
}
