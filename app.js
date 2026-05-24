document.addEventListener('DOMContentLoaded', () => {
  initHeader();
  initThemeToggle();
  initMobileMenu();
  initStatsCounter();
  initFaqAccordion();
  initJobMatcher();
  initScrollReveal();
  initTestimonialCarousel();
});

/* --- HEADER EFFECS --- */
function initHeader() {
  const header = document.querySelector('.header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
}

/* --- TESTIMONIAL CAROUSEL --- */
function initTestimonialCarousel() {
  const track = document.getElementById('testimonial-track');
  const nextBtn = document.getElementById('carousel-next');
  const prevBtn = document.getElementById('carousel-prev');
  const dots = document.querySelectorAll('#carousel-dots .dot');

  if (track && nextBtn && prevBtn && dots.length > 0) {
    let currentIndex = 0;
    const slides = track.children;
    const totalSlides = slides.length;

    function updateCarousel() {
      track.style.transform = `translateX(-${currentIndex * 100}%)`;
      dots.forEach((dot, index) => {
        if (index === currentIndex) {
          dot.style.background = 'var(--color-accent)';
          dot.classList.add('active');
        } else {
          dot.style.background = 'rgba(212,175,55,0.3)';
          dot.classList.remove('active');
        }
      });
    }

    nextBtn.addEventListener('click', () => {
      currentIndex = (currentIndex + 1) % totalSlides;
      updateCarousel();
    });

    prevBtn.addEventListener('click', () => {
      currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
      updateCarousel();
    });

    dots.forEach((dot, index) => {
      dot.addEventListener('click', () => {
        currentIndex = index;
        updateCarousel();
      });
    });

    setInterval(() => {
      currentIndex = (currentIndex + 1) % totalSlides;
      updateCarousel();
    }, 6000);
  }
}

/* --- THEME TOGGLING --- */
function initThemeToggle() {
  const themeToggleBtn = document.getElementById('theme-toggle');
  
  // Check local storage or system preference
  const savedTheme = localStorage.getItem('theme') || 
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  themeToggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
  });
}

function updateThemeIcon(theme) {
  const iconPath = document.querySelector('#theme-toggle svg path');
  // Sun icon SVG path (for dark mode selection/sun appearance)
  const sunPath = "M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1zM5.99 4.58c-.39-.39-1.03-.39-1.41 0s-.39 1.03 0 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41L5.99 4.58zm12.37 12.37c-.39-.39-1.03-.39-1.41 0s-.39 1.03 0 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41l-1.06-1.06zm1.06-10.96c.39-.39.39-1.03 0-1.41s-1.03-.39-1.41 0l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06zM7.05 18.01c.39-.39.39-1.03 0-1.41s-1.03-.39-1.41 0l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06z";
  // Moon icon SVG path (for light mode selection/moon appearance)
  const moonPath = "M12.3 22h-.1c-5.5 0-10-4.5-10-10 0-4.8 3.5-8.9 8.2-9.8.6-.1 1.2.3 1.3.9.1.6-.3 1.2-.9 1.3-3.7.7-6.5 3.9-6.5 7.7 0 4.4 3.6 8 8 8 3.8 0 7-2.8 7.7-6.5.1-.6.7-1 1.3-.9.6.1 1 .7.9 1.3-.9 4.7-5 8.2-9.9 8.2z";
  
  if (theme === 'dark') {
    iconPath.setAttribute('d', sunPath);
  } else {
    iconPath.setAttribute('d', moonPath);
  }
}

/* --- MOBILE MENU --- */
function initMobileMenu() {
  const mobileToggle = document.getElementById('mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');

  mobileToggle.addEventListener('click', () => {
    mobileToggle.classList.toggle('active');
    navMenu.classList.toggle('active');
  });

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      mobileToggle.classList.remove('active');
      navMenu.classList.remove('active');
    });
  });
}

/* --- STATS COUNTER ANIMATION --- */
function initStatsCounter() {
  const stats = document.querySelectorAll('.stat-number');
  if (stats.length > 0) {
    const animateStats = () => {
      stats.forEach(stat => {
        const target = +stat.getAttribute('data-target');
        const suffix = stat.getAttribute('data-suffix') || '';
        
        const updateCount = () => {
          const current = +stat.innerText.replace(/[^0-9]/g, '');
          const increment = target / 50; 

          if (current < target) {
            stat.innerText = Math.ceil(current + increment) + suffix;
            setTimeout(updateCount, 40);
          } else {
            stat.innerText = target + suffix;
          }
        };
        
        updateCount();
      });
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateStats();
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    stats.forEach(stat => {
      observer.observe(stat);
    });
  }
}

/* --- FAQ ACCORDION --- */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');
  
  faqItems.forEach(item => {
    const header = item.querySelector('.faq-header');
    const body = item.querySelector('.faq-body');
    if (!header || !body) return;

    header.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      
      // Close all open items
      faqItems.forEach(otherItem => {
        otherItem.classList.remove('active');
        otherItem.querySelector('.faq-body').style.maxHeight = null;
      });

      if (!isActive) {
        item.classList.add('active');
        // Set dynamic scroll height
        body.style.maxHeight = body.scrollHeight + 'px';
      }
    });
  });
}

/* --- INTERACTIVE JOB MATCHER WIDGET --- */
function initJobMatcher() {
  const matcher = document.getElementById('job-matcher-widget');
  if (!matcher) return;

  const steps = matcher.querySelectorAll('.matcher-step');
  const progressBar = matcher.querySelector('.matcher-progress');
  const btnPrev = document.getElementById('matcher-prev');
  const btnNext = document.getElementById('matcher-next');
  
  let currentStepIndex = 0;
  
  // Selection States
  let selectedCategory = '';
  let selectedSkills = [];
  let selectedTimezone = '';

  // Options Handlers
  const categoryOptions = matcher.querySelectorAll('.category-option');
  categoryOptions.forEach(opt => {
    opt.addEventListener('click', () => {
      categoryOptions.forEach(o => o.classList.remove('selected'));
      opt.classList.add('selected');
      selectedCategory = opt.getAttribute('data-value');
      validateCurrentStep();
    });
  });

  const skillOptions = matcher.querySelectorAll('.skill-checkbox');
  skillOptions.forEach(opt => {
    opt.addEventListener('click', () => {
      opt.classList.toggle('selected');
      const val = opt.getAttribute('data-value');
      if (opt.classList.contains('selected')) {
        selectedSkills.push(val);
      } else {
        selectedSkills = selectedSkills.filter(s => s !== val);
      }
      validateCurrentStep();
    });
  });

  const timezoneOptions = matcher.querySelectorAll('.timezone-option');
  timezoneOptions.forEach(opt => {
    opt.addEventListener('click', () => {
      timezoneOptions.forEach(o => o.classList.remove('selected'));
      opt.classList.add('selected');
      selectedTimezone = opt.getAttribute('data-value');
      validateCurrentStep();
    });
  });

  // Validation
  function validateCurrentStep() {
    let isValid = false;
    if (currentStepIndex === 0 && selectedCategory) isValid = true;
    else if (currentStepIndex === 1 && selectedSkills.length > 0) isValid = true;
    else if (currentStepIndex === 2 && selectedTimezone) isValid = true;

    if(btnNext) btnNext.disabled = !isValid;
  }

  // Navigation Logic
  function goToStep(index) {
    steps[currentStepIndex].classList.remove('active');
    currentStepIndex = index;
    steps[currentStepIndex].classList.add('active');

    // Update Progress
    if(progressBar) {
      const progressPercent = ((currentStepIndex + 1) / steps.length) * 100;
      progressBar.style.width = `${progressPercent}%`;
    }

    // Navigation buttons toggle
    if(btnPrev) btnPrev.style.display = currentStepIndex === 0 || currentStepIndex === steps.length - 1 ? 'none' : 'flex';
    
    if (currentStepIndex === steps.length - 1) {
      // Calculate and display matching result
      displayResult();
    } else {
      if(btnNext) {
        btnNext.textContent = currentStepIndex === steps.length - 2 ? 'Evaluate Case' : 'Next Step';
        btnNext.style.display = 'flex';
      }
      validateCurrentStep();
    }
  }

  if(btnNext) {
    btnNext.addEventListener('click', () => {
      if (currentStepIndex < steps.length - 1) {
        goToStep(currentStepIndex + 1);
      }
    });
  }

  if(btnPrev) {
    btnPrev.addEventListener('click', () => {
      if (currentStepIndex > 0) {
        goToStep(currentStepIndex - 1);
      }
    });
  }

  // Calculate matching result
  function displayResult() {
    if(btnNext) btnNext.style.display = 'none';
    if(btnPrev) btnPrev.style.display = 'none';
    if(progressBar) progressBar.style.width = '100%';

    const resultRole = document.getElementById('matched-role');
    const resultDesc = document.getElementById('matched-desc');

    if(!resultRole || !resultDesc) return;

    let matchedRole = '';
    let matchedDesc = '';

    if (selectedCategory === 'corporate') {
      matchedRole = 'Corporate Litigation Match';
      matchedDesc = 'Based on your inputs, your matter aligns with our core corporate capabilities. Alexander Pierce can personally review your file regarding contracts, mergers, or partnership disputes.';
    } else if (selectedCategory === 'ip') {
      matchedRole = 'Intellectual Property Review';
      matchedDesc = 'Your IP matter requires aggressive defense. We have successfully defended patents, trademarks, and trade secrets in federal court. Pierce Law is ready to review your case.';
    } else {
      matchedRole = 'Case Review Requested';
      matchedDesc = 'Your legal matter has been preliminarily evaluated. Please schedule a consultation so we can dive into the specifics of your situation.';
    }

    resultRole.textContent = matchedRole;
    resultDesc.textContent = matchedDesc;
  }

  // Reset Matcher
  const resetBtn = document.getElementById('matcher-reset');
  if(resetBtn) {
    resetBtn.addEventListener('click', (e) => {
      e.preventDefault();
      selectedCategory = '';
      selectedSkills = [];
      selectedTimezone = '';
      
      // Clear styles
      categoryOptions.forEach(o => o.classList.remove('selected'));
      skillOptions.forEach(o => o.classList.remove('selected'));
      timezoneOptions.forEach(o => o.classList.remove('selected'));

      goToStep(0);
    });
  }

  // Initial validation
  validateCurrentStep();
}

/* --- SCROLL REVEAL (INTERSECTION OBSERVER) --- */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // Unobserve once animated
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -50px 0px' // animate slightly before element enters viewport
  });

  revealElements.forEach(el => observer.observe(el));
}

/* --- CONTACT FORM ANIMATION & SUBMISSION --- */
function initContactForm() {
  const form = document.getElementById('callback-form');
  const successMessage = document.getElementById('callback-success');
  const formTitle = document.getElementById('form-title');
  const formDesc = document.getElementById('form-desc');
  const submitBtn = document.getElementById('submit-btn');
  const btnText = document.getElementById('btn-text');
  const btnSpinner = document.getElementById('btn-spinner');
  const animatedCheck = document.getElementById('animated-check');
  
  if (form && successMessage && submitBtn) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const name = document.getElementById('contact-name')?.value;
      const email = document.getElementById('contact-email')?.value;
      const phone = document.getElementById('contact-phone')?.value;
      const message = document.getElementById('contact-message')?.value;
      
      // Loading State
      submitBtn.disabled = true;
      btnText.style.opacity = '0';
      btnSpinner.style.display = 'block';
      submitBtn.style.transform = 'scale(0.98)';
      submitBtn.style.cursor = 'wait';
      
      try {
        const response = await fetch('http://localhost:3001/api/contact', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name, email, phone, message })
        });
        
        const data = await response.json();
        
        if (data.success) {
          // Fade out form and headers, but KEEP layout space
          form.style.opacity = '0';
          form.style.visibility = 'hidden';
          if (formTitle) { formTitle.style.opacity = '0'; formTitle.style.visibility = 'hidden'; }
          if (formDesc) { formDesc.style.opacity = '0'; formDesc.style.visibility = 'hidden'; }
          
          // Show success message and trigger SVG animation
          setTimeout(() => {
            successMessage.style.pointerEvents = 'auto';
            successMessage.style.opacity = '1';
            successMessage.style.transform = 'translateY(0)';
            
            if (animatedCheck) {
              animatedCheck.classList.add('draw-check');
            }
          }, 100);
        } else {
          alert('Error: ' + data.error);
          resetFormState();
        }
      } catch (err) {
        console.error('Submission error:', err);
        alert('Failed to connect to the server. Please try again.');
        resetFormState();
      }
    });

    function resetFormState() {
      submitBtn.disabled = false;
      btnText.style.opacity = '1';
      btnSpinner.style.display = 'none';
      submitBtn.style.transform = 'scale(1)';
      submitBtn.style.cursor = 'pointer';
    }
  }
}

// Ensure the function is called on DOM load
document.addEventListener('DOMContentLoaded', () => {
  initContactForm();
});
