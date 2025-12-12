// Temporizador para el mensaje de bienvenida
setTimeout(() => {
    const welcomeScreen = document.getElementById('welcome-screen');
    const mainContent = document.getElementById('main-content');
    
    // Desvanecer el mensaje de bienvenida
    welcomeScreen.style.opacity = '0';
    
    setTimeout(() => {
        welcomeScreen.style.display = 'none';
        mainContent.classList.remove('hidden');
    }, 1000);
}, 3000);

// Función para seleccionar emoción (pendiente de implementación)
function selectEmotion(emotion) {
    console.log('Emoción seleccionada:', emotion);
    // Funcionalidad pendiente de definir
}

// Efectos de partículas en el fondo (opcional)
function createParticle() {
    const particle = document.createElement('div');
    particle.style.position = 'fixed';
    particle.style.width = '3px';
    particle.style.height = '3px';
    particle.style.borderRadius = '50%';
    particle.style.background = `rgba(167, 139, 250, ${Math.random() * 0.5})`;
    particle.style.left = Math.random() * 100 + '%';
    particle.style.top = Math.random() * 100 + '%';
    particle.style.pointerEvents = 'none';
    particle.style.animation = `pulse ${2 + Math.random() * 3}s ease-in-out infinite`;
    
    document.body.appendChild(particle);
    
    setTimeout(() => {
        particle.remove();
    }, 5000);
}

// Crear partículas periódicamente para un efecto ambiente
setInterval(createParticle, 2000);

// Animación suave de scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
