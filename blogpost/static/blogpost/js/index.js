const navSlide = () => {
    const navBars = document.querySelector('.logo span');
    const navLinks = document.querySelector('nav ul');     
        navBars.addEventListener('click', () => {
            navLinks.classList.toggle('nav-active');
        });    
}

navSlide();