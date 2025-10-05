// Responsive JavaScript Example
window.addEventListener('DOMContentLoaded', (event) => {
    console.log('Page fully loaded and ready');

    // Example: Add a click event to a button (if any button exists)
    const button = document.querySelector('button');
    if (button) {
        button.addEventListener('click', () => {
            alert('Button clicked!');
        });
    }

// Navigation Menu Active State
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.main-nav a');
    navLinks.forEach(link => {
        if (window.location.pathname === link.getAttribute('href')) {
            link.classList.add('active');
        }
    });

    // Search Box Functionality
    const searchBox = document.querySelector('.search-box input');
    const searchButton = document.querySelector('.search-box button');
    
    searchButton.addEventListener('click', () => {
        if (searchBox.value.trim()) {
            // Implement search functionality
            console.log('Searching for:', searchBox.value);
        }
    });

    // Add smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});    // Add smooth scrolling to navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Add a back-to-top button
    const backToTopButton = document.createElement('button');
    backToTopButton.textContent = '↑';
    backToTopButton.style.position = 'fixed';
    backToTopButton.style.bottom = '20px';
    backToTopButton.style.right = '20px';
    backToTopButton.style.padding = '10px';
    backToTopButton.style.border = 'none';
    backToTopButton.style.borderRadius = '50%';
    backToTopButton.style.backgroundColor = '#004d99';
    backToTopButton.style.color = 'white';
    backToTopButton.style.cursor = 'pointer';
    backToTopButton.style.display = 'none';
    backToTopButton.style.zIndex = '1000';

    document.body.appendChild(backToTopButton);

    backToTopButton.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });
});
