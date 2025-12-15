/**
 * ================================================================================
 * utils.js - Utilidades Compartidas para Ejercicios de Respiración
 * ================================================================================
 * 
 * Descripción:
 *   Biblioteca de funciones JavaScript reutilizables que implementan la lógica
 *   común de animación para los tres ejercicios de respiración. Sigue el 
 *   principio DRY (Don't Repeat Yourself) centralizando código que de otra
 *   forma estaría duplicado en cada HTML.
 * 
 * Archivos que importan este módulo:
 *   - ansiedad.html (via <script src="/utils.js">)
 *   - ira.html
 *   - estres.html
 * 
 * Categorías de funciones:
 *   1. INTERPOLACIÓN - Transiciones suaves entre valores
 *   2. EASING - Curvas de aceleración para animaciones naturales
 *   3. CANVAS - Configuración y dibujo de fondos animados
 *   4. CIRCLE - Actualización visual del círculo de respiración
 * 
 * Conceptos matemáticos utilizados:
 *   - Linear Interpolation (LERP): Transición lineal entre dos valores
 *   - Cubic Easing: Curvas de aceleración/desaceleración
 *   - Radial Gradients: Degradados circulares para efectos de luz
 *   - Sinusoidal Movement: Movimiento orgánico usando sin/cos
 * 
 * ================================================================================
 */

// ========================================
// INTERPOLACIÓN Y EASING
// ========================================
// Funciones matemáticas para crear transiciones suaves
// entre valores. Fundamentales para animaciones fluidas.
// ========================================

/**
 * lerp - Linear Interpolation (Interpolación Lineal)
 * 
 * Calcula un valor intermedio entre dos puntos.
 * Es la base de todas las animaciones suaves.
 * 
 * Fórmula: resultado = a + (b - a) * t
 * 
 * @param {number} a - Valor inicial (cuando t = 0)
 * @param {number} b - Valor final (cuando t = 1)
 * @param {number} t - Progreso de la interpolación (0.0 a 1.0)
 * @returns {number} - Valor interpolado entre a y b
 * 
 * @example
 * lerp(0, 100, 0.5)  // → 50 (mitad del camino)
 * lerp(0, 100, 0.25) // → 25 (un cuarto del camino)
 * lerp(10, 20, 1)    // → 20 (valor final)
 */
function lerp(a, b, t) {
    return a + (b - a) * t;
}

/**
 * lerpColor - Interpolación de Colores RGB
 * 
 * Interpola suavemente entre dos colores.
 * Aplica lerp a cada canal (R, G, B) independientemente.
 * 
 * @param {Object} c1 - Color inicial {r, g, b}
 * @param {Object} c2 - Color final {r, g, b}
 * @param {number} t - Progreso (0.0 a 1.0)
 * @returns {Object} - Color interpolado {r, g, b}
 * 
 * @example
 * // Transición de rojo a azul al 50%
 * lerpColor({r: 255, g: 0, b: 0}, {r: 0, g: 0, b: 255}, 0.5)
 * // → {r: 128, g: 0, b: 128} (violeta)
 */
function lerpColor(c1, c2, t) {
    return {
        r: Math.round(lerp(c1.r, c2.r, t)),
        g: Math.round(lerp(c1.g, c2.g, t)),
        b: Math.round(lerp(c1.b, c2.b, t))
    };
}

/**
 * getColorFromArray - Obtener Color de un Array de Colores
 * 
 * Dado un array de colores y un progreso (0-1), calcula el color
 * exacto interpolando entre los colores adyacentes del array.
 * Permite crear gradientes complejos con múltiples paradas.
 * 
 * @param {Array<Object>} arr - Array de colores [{r, g, b}, ...]
 * @param {number} progress - Progreso en el array (0.0 a 1.0)
 * @returns {Object} - Color interpolado {r, g, b}
 * 
 * @example
 * const colors = [
 *   {r: 255, g: 0, b: 0},   // Rojo (0%)
 *   {r: 255, g: 255, b: 0}, // Amarillo (50%)
 *   {r: 0, g: 255, b: 0}    // Verde (100%)
 * ];
 * getColorFromArray(colors, 0.25) // → Naranja (entre rojo y amarillo)
 * getColorFromArray(colors, 0.75) // → Lima (entre amarillo y verde)
 */
function getColorFromArray(arr, progress) {
    // Calcular índice decimal en el array
    const idx = progress * (arr.length - 1);
    
    // Índices de los colores adyacentes
    const lo = Math.floor(idx);                    // Color anterior
    const hi = Math.min(lo + 1, arr.length - 1);   // Color siguiente
    
    // Interpolar entre los dos colores
    return lerpColor(arr[lo], arr[hi], idx - lo);
}

// ========================================
// EASING FUNCTIONS - Curvas de Animación
// ========================================
// Las funciones de easing modifican el progreso lineal (t)
// para crear movimientos más naturales y orgánicos.
// 
// Visualización de curvas: https://easings.net/
// ========================================

/**
 * easeInOutCubic - Aceleración y Desaceleración Suave
 * 
 * Comienza lento, acelera en el medio, termina lento.
 * Ideal para: Transiciones de UI, movimientos naturales.
 * 
 * Curva: Cúbica (t³) en ambos extremos
 * 
 * @param {number} t - Progreso lineal (0.0 a 1.0)
 * @returns {number} - Progreso con easing aplicado
 * 
 * Comportamiento:
 *   t=0.0 → 0.0   (inicio lento)
 *   t=0.5 → 0.5   (velocidad máxima en el medio)
 *   t=1.0 → 1.0   (final lento)
 */
function easeInOutCubic(t) {
    return t < 0.5 
        ? 4 * t * t * t                        // Primera mitad: acelera
        : 1 - Math.pow(-2 * t + 2, 3) / 2;     // Segunda mitad: desacelera
}

/**
 * easeOutCubic - Solo Desaceleración
 * 
 * Comienza rápido, termina lento.
 * Ideal para: Elementos que "aterrizan" suavemente.
 * 
 * @param {number} t - Progreso lineal (0.0 a 1.0)
 * @returns {number} - Progreso con easing aplicado
 */
function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
}

/**
 * easeInCubic - Solo Aceleración
 * 
 * Comienza lento, termina rápido.
 * Ideal para: Elementos que "despegan".
 * 
 * @param {number} t - Progreso lineal (0.0 a 1.0)
 * @returns {number} - Progreso con easing aplicado
 */
function easeInCubic(t) {
    return t * t * t;
}

// ========================================
// CANVAS UTILITIES - Configuración del Canvas
// ========================================
// Funciones para manejar el elemento <canvas> HTML5
// que renderiza los fondos animados de los ejercicios.
// ========================================

/**
 * setupCanvas - Inicializar Canvas Responsive
 * 
 * Configura el canvas para que siempre ocupe toda la ventana
 * y se redimensione automáticamente cuando cambia el tamaño.
 * 
 * @param {HTMLCanvasElement} canvas - Elemento canvas a configurar
 * 
 * @example
 * const canvas = document.getElementById('bg-canvas');
 * setupCanvas(canvas);
 * // El canvas ahora es fullscreen y responsive
 */
function setupCanvas(canvas) {
    /**
     * resize - Ajusta el canvas al tamaño de la ventana
     * Se ejecuta al inicio y cada vez que cambia el tamaño
     */
    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    
    // Configuración inicial
    resize();
    
    // Listener para redimensionamiento
    window.addEventListener('resize', resize);
}

/**
 * drawRadialGradient - Dibujar Fondo con Gradientes Radiales Animados
 * 
 * Crea un fondo animado con múltiples "orbs" de luz que se mueven
 * suavemente usando funciones sinusoidales. Cada orb es un gradiente
 * radial que va de color sólido a transparente.
 * 
 * @param {CanvasRenderingContext2D} ctx - Contexto 2D del canvas
 * @param {HTMLCanvasElement} canvas - Elemento canvas
 * @param {Object} color - Color base {r, g, b}
 * @param {number} rMult - Multiplicador para el canal rojo del fondo (0-1)
 * @param {number} gMult - Multiplicador para el canal verde del fondo (0-1)
 * @param {number} bMult - Multiplicador para el canal azul del fondo (0-1)
 * @param {number} speed - Velocidad de animación (típicamente 0.0003-0.001)
 * 
 * Algoritmo:
 *   1. Dibuja fondo base oscuro (color * multiplicadores)
 *   2. Genera 5 puntos con posiciones sinusoidales
 *   3. Dibuja gradiente radial en cada punto
 *   4. Los gradientes se superponen creando efecto de mezcla
 * 
 * @example
 * // En el loop de animación:
 * function animate() {
 *   drawRadialGradient(ctx, canvas, currentColor, 0.1, 0.1, 0.15, 0.0005);
 *   requestAnimationFrame(animate);
 * }
 */
function drawRadialGradient(ctx, canvas, color, rMult, gMult, bMult, speed) {
    const w = canvas.width;
    const h = canvas.height;
    
    // ========================================
    // PASO 1: Fondo base oscuro
    // ========================================
    // Usa el color actual multiplicado por factores bajos
    // para crear un fondo oscuro pero tintado
    ctx.fillStyle = `rgb(${Math.floor(color.r * rMult)}, ${Math.floor(color.g * gMult)}, ${Math.floor(color.b * bMult)})`;
    ctx.fillRect(0, 0, w, h);
    
    // ========================================
    // PASO 2: Calcular posiciones de los orbs
    // ========================================
    // Cada punto se mueve en patrón sinusoidal
    // Diferentes frecuencias crean movimiento orgánico
    const time = Date.now() * speed;
    
    const points = [
        // Punto 1: Arriba izquierda
        {
            x: 0.2 + Math.sin(time) * 0.08, 
            y: 0.2 + Math.cos(time * 0.8) * 0.08
        },
        // Punto 2: Arriba derecha
        {
            x: 0.8 + Math.cos(time * 1.2) * 0.08, 
            y: 0.3 + Math.sin(time) * 0.08
        },
        // Punto 3: Centro
        {
            x: 0.5 + Math.sin(time * 0.7) * 0.1, 
            y: 0.5 + Math.cos(time * 1.1) * 0.1
        },
        // Punto 4: Abajo derecha
        {
            x: 0.7 + Math.cos(time * 0.9) * 0.08, 
            y: 0.8 + Math.sin(time * 0.6) * 0.08
        },
        // Punto 5: Abajo izquierda
        {
            x: 0.3 + Math.sin(time * 1.3) * 0.08, 
            y: 0.7 + Math.cos(time * 0.5) * 0.08
        }
    ];
    
    // ========================================
    // PASO 3: Dibujar gradientes radiales
    // ========================================
    points.forEach((p, i) => {
        // Crear gradiente radial desde el centro del punto
        const grad = ctx.createRadialGradient(
            p.x * w, p.y * h, 0,           // Centro: sin radio
            p.x * w, p.y * h, w * 0.5      // Borde: 50% del ancho
        );
        
        // Alpha pulsante para efecto de respiración
        const alpha = 0.35 + Math.sin(time + i) * 0.1;
        
        // Definir paradas del gradiente
        grad.addColorStop(0, `rgba(${color.r}, ${color.g}, ${color.b}, ${alpha})`);           // Centro: color fuerte
        grad.addColorStop(0.4, `rgba(${color.r}, ${color.g}, ${color.b}, ${alpha * 0.4})`);   // Medio: más tenue
        grad.addColorStop(1, 'transparent');                                                   // Borde: invisible
        
        // Dibujar el gradiente
        ctx.fillStyle = grad;
        ctx.fillRect(0, 0, w, h);
    });
}

// ========================================
// CIRCLE ANIMATION - Animación del Círculo
// ========================================
// Funciones para animar el círculo de respiración
// que guía visualmente al usuario durante el ejercicio.
// ========================================

/**
 * updateCircleStyle - Actualizar Estilo Visual del Círculo
 * 
 * Aplica transformaciones CSS al círculo de respiración:
 * - Escala (tamaño)
 * - Color del borde con gradiente
 * - Efecto glow (resplandor) proporcional al tamaño
 * 
 * @param {HTMLElement} circle - Elemento DOM del círculo (.breathing-circle)
 * @param {Object} color - Color actual {r, g, b}
 * @param {number} scale - Escala actual (1 = tamaño base)
 * @param {number} maxScale - Escala máxima para calcular intensidad del glow
 * 
 * Efectos visuales aplicados:
 *   1. transform: scale() - Tamaño del círculo
 *   2. background: linear-gradient - Borde con degradado
 *   3. box-shadow: múltiples capas de glow
 * 
 * @example
 * // En el loop de animación:
 * const scale = lerp(1, 2, progress);  // Escala de 1x a 2x
 * const color = getColorFromArray(colors, progress);
 * updateCircleStyle(circle, color, scale, 2);
 */
function updateCircleStyle(circle, color, scale, maxScale) {
    // ========================================
    // Aplicar escala (tamaño)
    // ========================================
    circle.style.transform = `scale(${scale})`;
    
    // ========================================
    // Calcular intensidad del glow
    // ========================================
    // glow = 0 cuando scale = 0
    // glow = 1 cuando scale = maxScale
    const glow = scale / maxScale;
    
    // Extraer componentes RGB
    const r = color.r, g = color.g, b = color.b;
    
    // ========================================
    // Aplicar gradiente al borde
    // ========================================
    // Técnica: Doble gradiente con padding-box/border-box
    // - Primer gradiente: Fondo oscuro semi-transparente
    // - Segundo gradiente: Borde colorido con highlight
    circle.style.background = `
        linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.1)) padding-box,
        linear-gradient(135deg, 
            rgb(${r}, ${g}, ${b}), 
            rgb(${Math.min(255, r + 40)}, ${Math.min(255, g + 40)}, ${Math.min(255, b + 40)})
        ) border-box
    `;
    
    // ========================================
    // Aplicar efecto glow (múltiples sombras)
    // ========================================
    // 4 capas de sombra con diferentes tamaños y opacidades
    // + 1 sombra interior (inset) para profundidad
    circle.style.boxShadow = `
        0 0 ${50 * glow}px rgba(${r}, ${g}, ${b}, 0.7),
        0 0 ${100 * glow}px rgba(${r}, ${g}, ${b}, 0.5),
        0 0 ${150 * glow}px rgba(${r}, ${g}, ${b}, 0.3),
        inset 0 0 ${50 * glow}px rgba(${r}, ${g}, ${b}, 0.3)
    `;
}