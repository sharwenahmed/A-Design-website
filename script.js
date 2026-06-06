const menuBtn = document.getElementById('menuBtn');
const navLinks = document.getElementById('navLinks');
const leadForm = document.getElementById('leadForm');
const formNote = document.getElementById('formNote');
const cursorGlow = document.getElementById('cursorGlow');

function closeMenu(){
  navLinks?.classList.remove('active');
  menuBtn?.classList.remove('active');
  menuBtn?.setAttribute('aria-expanded','false');
  document.body.classList.remove('menu-open');
}

menuBtn?.addEventListener('click', () => {
  const willOpen = !navLinks.classList.contains('active');
  navLinks.classList.toggle('active', willOpen);
  menuBtn.classList.toggle('active', willOpen);
  menuBtn.setAttribute('aria-expanded', String(willOpen));
  document.body.classList.toggle('menu-open', willOpen);
});

navLinks?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
window.addEventListener('keydown', event => { if(event.key === 'Escape') closeMenu(); });

window.addEventListener('mousemove', event => {
  if(cursorGlow){
    cursorGlow.style.left = `${event.clientX}px`;
    cursorGlow.style.top = `${event.clientY}px`;
  }
});

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

document.querySelectorAll('.tilt-card').forEach(card => {
  card.addEventListener('mousemove', event => {
    const rect = card.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    const rotateY = ((x / rect.width) - 0.5) * 10;
    const rotateX = ((0.5 - y / rect.height)) * 10;
    card.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = '';
  });
});

window.addEventListener('scroll', () => {
  const y = window.scrollY;
  document.querySelectorAll('[data-parallax]').forEach(el => {
    const speed = Number(el.dataset.parallax || 0.08);
    el.style.transform = `translateY(${y * speed}px)`;
  });
});

// Formspree lead form handler for GitHub Pages.
// Sends the form automatically without opening the customer's email app.
leadForm?.addEventListener('submit', async event => {
  event.preventDefault();

  const submitButton = leadForm.querySelector('button[type="submit"]');
  const originalButtonText = submitButton?.textContent || 'Submit';

  if (formNote) {
    formNote.textContent = 'Sending your request...';
    formNote.classList.remove('error', 'success');
  }

  if (submitButton) {
    submitButton.disabled = true;
    submitButton.textContent = 'Sending...';
  }

  try {
    const response = await fetch(leadForm.action, {
      method: 'POST',
      body: new FormData(leadForm),
      headers: { 'Accept': 'application/json' }
    });

    if (response.ok) {
      if (formNote) {
        formNote.textContent = 'Thank you! Your request has been sent. We’ll contact you soon.';
        formNote.classList.remove('error');
        formNote.classList.add('success');
      }
      leadForm.reset();
    } else {
      throw new Error('Formspree submission failed');
    }
  } catch (error) {
    if (formNote) {
      formNote.textContent = 'Something went wrong. Please try again or email us directly.';
      formNote.classList.remove('success');
      formNote.classList.add('error');
    }
  } finally {
    if (submitButton) {
      submitButton.disabled = false;
      submitButton.textContent = originalButtonText;
    }
  }
});
