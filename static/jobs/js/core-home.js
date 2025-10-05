// Scroll animations
function observeElements() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1
    });
    
    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });
}

// Counter animation for stats
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    
    counters.forEach(counter => {
        const target = parseInt(counter.textContent.replace(/\D/g, ''));
        const increment = target / 50;
        let current = 0;
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                counter.textContent = target + '+';
                clearInterval(timer);
            } else {
                counter.textContent = Math.floor(current) + '+';
            }
        }, 50);
    });
}

// Parallax effect for hero section
function parallaxEffect() {
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const heroContent = document.querySelector('.hero-content');
        const floatingIcons = document.querySelectorAll('.floating-icon');
        
        if (heroContent) {
            heroContent.style.transform = `translateY(${scrolled * 0.3}px)`;
        }
        
        floatingIcons.forEach((icon, index) => {
            const speed = 0.1 + (index * 0.05);
            icon.style.transform = `translateY(${scrolled * speed}px) rotate(${scrolled * 0.1}deg)`;
        });
    });
}

// Enhanced card hover effects
function enhanceCardInteractions() {
    const cards = document.querySelectorAll('.modern-sidebar-card, .modern-job-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
            this.style.zIndex = '10';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.zIndex = '1';
        });
    });
}

// Smooth reveal animation for cards
function staggerCardAnimations() {
    const cards = document.querySelectorAll('.modern-sidebar-card');
    
    cards.forEach((card, index) => {
        card.classList.add('animate-on-scroll');
        card.style.animationDelay = `${index * 0.1}s`;
    });
}

// Initialize all effects
document.addEventListener('DOMContentLoaded', function() {
    observeElements();
    parallaxEffect();
    enhanceCardInteractions();
    staggerCardAnimations();
    
    // Animate counters when hero section is visible
    const heroObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
                heroObserver.unobserve(entry.target);
            }
        });
    });
    
    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) {
        heroObserver.observe(heroStats);
    }
    
    // Add loading animation to job cards
    const jobCards = document.querySelectorAll('.modern-job-card');
    jobCards.forEach((card, index) => {
        card.style.animationDelay = `${0.5 + (index * 0.1)}s`;
        card.classList.add('fade-in-up');
    });
});

// Page transition effects
window.addEventListener('beforeunload', function() {
    document.body.style.opacity = '0.8';
    document.body.style.transform = 'scale(0.98)';
});
