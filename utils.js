/**
 * utils.js - Utilidades compartidas para ejercicios de respiración
 * DRY: Funciones reutilizables en ansiedad, ira y estrés
 */

// ========================================
// INTERPOLACIÓN Y EASING
// ========================================

function lerp(a, b, t) {
    return a + (b - a) * t;
}

function lerpColor(c1, c2, t) {
    return {
        r: Math.round(lerp(c1.r, c2.r, t)),
        g: Math.round(lerp(c1.g, c2.g, t)),
        b: Math.round(lerp(c1.b, c2.b, t))
    };
}

function getColorFromArray(arr, progress) {
    const idx = progress * (arr.length - 1);
    const lo = Math.floor(idx);
    const hi = Math.min(lo + 1, arr.length - 1);
    return lerpColor(arr[lo], arr[hi], idx - lo);
}

// Easing functions
function easeInOutCubic(t) {
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
}

function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
}

function easeInCubic(t) {
    return t * t * t;
}

// ========================================
// CANVAS UTILITIES
// ========================================

function setupCanvas(canvas) {
    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resize();
    window.addEventListener('resize', resize);
}

// Fondo con gradientes radiales animados
function drawRadialGradient(ctx, canvas, color, rMult, gMult, bMult, speed) {
    const w = canvas.width;
    const h = canvas.height;
    
    // Fondo base oscuro
    ctx.fillStyle = `rgb(${Math.floor(color.r * rMult)}, ${Math.floor(color.g * gMult)}, ${Math.floor(color.b * bMult)})`;
    ctx.fillRect(0, 0, w, h);
    
    // Gradientes animados
    const time = Date.now() * speed;
    const points = [
        {x: 0.2 + Math.sin(time) * 0.08, y: 0.2 + Math.cos(time * 0.8) * 0.08},
        {x: 0.8 + Math.cos(time * 1.2) * 0.08, y: 0.3 + Math.sin(time) * 0.08},
        {x: 0.5 + Math.sin(time * 0.7) * 0.1, y: 0.5 + Math.cos(time * 1.1) * 0.1},
        {x: 0.7 + Math.cos(time * 0.9) * 0.08, y: 0.8 + Math.sin(time * 0.6) * 0.08},
        {x: 0.3 + Math.sin(time * 1.3) * 0.08, y: 0.7 + Math.cos(time * 0.5) * 0.08}
    ];
    
    points.forEach((p, i) => {
        const grad = ctx.createRadialGradient(p.x * w, p.y * h, 0, p.x * w, p.y * h, w * 0.5);
        const alpha = 0.35 + Math.sin(time + i) * 0.1;
        grad.addColorStop(0, `rgba(${color.r}, ${color.g}, ${color.b}, ${alpha})`);
        grad.addColorStop(0.4, `rgba(${color.r}, ${color.g}, ${color.b}, ${alpha * 0.4})`);
        grad.addColorStop(1, 'transparent');
        ctx.fillStyle = grad;
        ctx.fillRect(0, 0, w, h);
    });
}

// ========================================
// CIRCLE ANIMATION
// ========================================

function updateCircleStyle(circle, color, scale, maxScale) {
    circle.style.transform = `scale(${scale})`;
    
    const glow = scale / maxScale;
    const r = color.r, g = color.g, b = color.b;
    
    circle.style.background = `
        linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.1)) padding-box,
        linear-gradient(135deg, rgb(${r}, ${g}, ${b}), rgb(${Math.min(255, r + 40)}, ${Math.min(255, g + 40)}, ${Math.min(255, b + 40)})) border-box
    `;
    
    circle.style.boxShadow = `
        0 0 ${50 * glow}px rgba(${r}, ${g}, ${b}, 0.7),
        0 0 ${100 * glow}px rgba(${r}, ${g}, ${b}, 0.5),
        0 0 ${150 * glow}px rgba(${r}, ${g}, ${b}, 0.3),
        inset 0 0 ${50 * glow}px rgba(${r}, ${g}, ${b}, 0.3)
    `;
}