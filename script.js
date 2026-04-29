// Mobile menu toggle
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('active');
  mobileMenu.classList.toggle('active');
});

// Close mobile menu on link click
mobileMenu.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('active');
    mobileMenu.classList.remove('active');
  });
});

// Navbar scroll effect
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 20) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// Fade-in animation on scroll
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.fade-in').forEach(el => {
  observer.observe(el);
});

// Form submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(contactForm);
    const data = Object.fromEntries(formData);
    console.log('Form submitted:', data);
    alert('Thank you for your inquiry. We will contact you shortly.');
    contactForm.reset();
  });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      const offset = 72;
      const position = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({
        top: position,
        behavior: 'smooth'
      });
    }
  });
});

// FAQ Accordion
const faqItems = document.querySelectorAll('.faq-item');
faqItems.forEach(item => {
  const question = item.querySelector('.faq-question');
  question.addEventListener('click', () => {
    // Close other open items
    faqItems.forEach(otherItem => {
      if (otherItem !== item && otherItem.classList.contains('active')) {
        otherItem.classList.remove('active');
      }
    });
    // Toggle current item
    item.classList.toggle('active');
  });
});

// Video slider navigation (optional enhancement)
const videoSlider = document.querySelector('.videos-slider');
if (videoSlider) {
  // Add scroll indicators or auto-scroll if needed
  let isDown = false;
  let startX;
  let scrollLeft;

  videoSlider.addEventListener('mousedown', (e) => {
    isDown = true;
    videoSlider.style.cursor = 'grabbing';
    startX = e.pageX - videoSlider.offsetLeft;
    scrollLeft = videoSlider.scrollLeft;
  });

  videoSlider.addEventListener('mouseleave', () => {
    isDown = false;
    videoSlider.style.cursor = 'grab';
  });

  videoSlider.addEventListener('mouseup', () => {
    isDown = false;
    videoSlider.style.cursor = 'grab';
  });

  videoSlider.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - videoSlider.offsetLeft;
    const walk = (x - startX) * 2;
    videoSlider.scrollLeft = scrollLeft - walk;
  });

  videoSlider.style.cursor = 'grab';
}