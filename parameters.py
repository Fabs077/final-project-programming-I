"""
parameters.py - Configuración Centralizada del Centro de Bienestar Emocional

Este módulo actúa como SINGLE SOURCE OF TRUTH (única fuente de verdad) para
toda la configuración de la aplicación. Centralizar los parámetros aquí permite:

    1. DRY (Don't Repeat Yourself): Cambiar un valor una vez afecta toda la app
    2. Mantenibilidad: Fácil de ajustar tiempos, colores y mensajes
    3. Separación de concerns: La lógica visual está separada de la configuración

Estructura de datos:
    - ANSIEDAD: Config del ejercicio de respiración 4-4
    - IRA: Config del ejercicio de respiración 4-7-8
    - ESTRES: Config de las ondas de sincronización mental
    - GENERAL: Parámetros compartidos (duraciones de fade, etc.)
    - UI_COLORS: Colores de la interfaz principal (index.html)

Formato de colores:
    - RGB dict {'r': int, 'g': int, 'b': int}: Para animaciones (interpolación)
    - HEX string '#RRGGBB': Para CSS estático

Uso:
    from parameters import ANSIEDAD, IRA, ESTRES, GENERAL, UI_COLORS
"""

# ============================================
# ANSIEDAD - Ejercicio de Respiración 4-4
# ============================================
# Técnica: Respiración cuadrada simplificada
# - Inhalar: 4 segundos (expansión del círculo)
# - Exhalar: 4 segundos (contracción del círculo)
# - Ciclos: 5 repeticiones (~45 segundos total)
#
# Beneficios: Activa el sistema nervioso parasimpático,
# reduciendo la respuesta de "lucha o huida"
# ============================================
ANSIEDAD = {
    # Tiempos en segundos
    'inhale_time': 4,       # Duración de inhalación
    'exhale_time': 4,       # Duración de exhalación
    'pause_time': 0.5,      # Pausa entre fases (transición suave)
    'cycles': 5,            # Número de repeticiones
    
    # Paletas de colores para animación del canvas
    # Formato RGB para interpolación suave frame a frame
    'colors': {
        # Inhalar - Azules claros (asociados con calma y cielo)
        # Progresión: sky-500 -> cyan-300 (más luminoso)
        'inhale': [
            {'r': 14, 'g': 165, 'b': 233},    # sky-500 (inicio)
            {'r': 56, 'g': 189, 'b': 248},    # sky-400
            {'r': 125, 'g': 211, 'b': 252},   # sky-300
            {'r': 6, 'g': 182, 'b': 212},     # cyan-500
            {'r': 34, 'g': 211, 'b': 238},    # cyan-400
            {'r': 103, 'g': 232, 'b': 249}    # cyan-300 (fin)
        ],
        # Exhalar - Teals/Verdes (asociados con naturaleza y tranquilidad)
        # Progresión: cyan-300 -> emerald-400 (más terroso)
        'exhale': [
            {'r': 103, 'g': 232, 'b': 249},   # cyan-300 (continúa desde inhale)
            {'r': 45, 'g': 212, 'b': 191},    # teal-400
            {'r': 20, 'g': 184, 'b': 166},    # teal-500
            {'r': 13, 'g': 148, 'b': 136},    # teal-600
            {'r': 16, 'g': 185, 'b': 129},    # emerald-500
            {'r': 52, 'g': 211, 'b': 153}     # emerald-400 (fin)
        ]
    },
    
    # Textos mostrados durante el ejercicio
    'messages': {
        'inhale': 'Inhala',                      # Durante inhalación
        'exhale': 'Exhala',                      # Durante exhalación
        'question': '¿Te sientes mucho mejor?',  # Pregunta final
        'success': 'Ahora estas en control.'     # Mensaje de éxito
    }
}

# ============================================
# IRA - Ejercicio de Respiración 4-7-8
# ============================================
# Técnica: Respiración relajante del Dr. Andrew Weil
# - Inhalar: 4 segundos (color rojo - reconocer la ira)
# - Mantener: 7 segundos (rojo -> amarillo - procesar)
# - Exhalar: 8 segundos (amarillo -> violeta - liberar)
# - Ciclos: 2 repeticiones (~38 segundos total)
#
# Beneficios: La exhalación prolongada activa el nervio vago,
# induciendo un estado de calma profunda
# ============================================
IRA = {
    # Tiempos en segundos (proporción 4:7:8)
    'inhale_time': 4,       # Inhalación corta
    'hold_time': 7,         # Retención media
    'exhale_time': 8,       # Exhalación larga (clave del ejercicio)
    'cycles': 2,            # Pocos ciclos, alta intensidad
    
    # Paletas de colores - Transición emocional completa
    # Rojo (ira) -> Amarillo (procesamiento) -> Violeta (paz)
    'colors': {
        # Fase 1: Rojo (Inhalar) - Reconocer la emoción
        # Progresión: rojo oscuro -> rojo brillante
        'red': [
            {'r': 127, 'g': 29, 'b': 29},      # red-900 (inicio oscuro)
            {'r': 153, 'g': 27, 'b': 27},      # red-800
            {'r': 185, 'g': 28, 'b': 28},      # red-700
            {'r': 220, 'g': 38, 'b': 38},      # red-600
            {'r': 239, 'g': 68, 'b': 68},      # red-500
            {'r': 248, 'g': 113, 'b': 113}     # red-400 (fin brillante)
        ],
        # Fase 2: Rojo -> Amarillo (Mantener) - Transformar energía
        # Transición a través de naranjas
        'red_to_yellow': [
            {'r': 239, 'g': 68, 'b': 68},      # red-500 (continúa)
            {'r': 234, 'g': 88, 'b': 12},      # orange-600
            {'r': 249, 'g': 115, 'b': 22},     # orange-500
            {'r': 251, 'g': 146, 'b': 60},     # orange-400
            {'r': 253, 'g': 186, 'b': 116},    # orange-300
            {'r': 251, 'g': 191, 'b': 36},     # amber-400
            {'r': 252, 'g': 211, 'b': 77},     # amber-300
            {'r': 250, 'g': 204, 'b': 21},     # yellow-400
            {'r': 253, 'g': 224, 'b': 71}      # yellow-300 (fin)
        ],
        # Fase 3: Amarillo -> Violeta (Exhalar) - Liberar y calmar
        # Transición por todo el espectro hasta violeta
        'yellow_to_violet': [
            {'r': 253, 'g': 224, 'b': 71},     # yellow-300 (continúa)
            {'r': 163, 'g': 230, 'b': 53},     # lime-400
            {'r': 74, 'g': 222, 'b': 128},     # green-400
            {'r': 45, 'g': 212, 'b': 191},     # teal-400
            {'r': 34, 'g': 211, 'b': 238},     # cyan-400
            {'r': 56, 'g': 189, 'b': 248},     # sky-400
            {'r': 96, 'g': 165, 'b': 250},     # blue-400
            {'r': 59, 'g': 130, 'b': 246},     # blue-500
            {'r': 99, 'g': 102, 'b': 241},     # indigo-500
            {'r': 139, 'g': 92, 'b': 246},     # violet-500
            {'r': 167, 'g': 139, 'b': 250}     # violet-400 (fin - paz)
        ]
    },
    
    # Textos mostrados durante el ejercicio
    'messages': {
        'inhale': 'Inhala',                      # Fase de inhalación
        'hold': 'Manten',                        # Fase de retención
        'exhale': 'Exhala',                      # Fase de exhalación
        'question': '¿Te sientes mucho mejor?',  # Pregunta final
        'success': 'Ahora estas en control.'     # Mensaje de éxito
    }
}

# ============================================
# ESTRÉS - Ondas de Sincronización Mental
# ============================================
# Técnica: Visualización de ondas calmantes
# - No requiere control de respiración activo
# - Las ondas pasan de caóticas a serenas
# - El usuario sincroniza naturalmente su estado
# - Duración: 30 segundos
#
# Beneficios: Reduce la carga cognitiva al no requerir
# seguir instrucciones, ideal para estrés alto
# ============================================
ESTRES = {
    # Duración total del ejercicio
    'duration': 30,              # Segundos totales
    
    # Configuración de las ondas (Perlin Noise)
    'wave_count': 5,             # Número de ondas simultáneas
    
    # Transición de caos a calma (valores 0.0 - 1.0)
    'initial_chaos': 1.0,        # Inicio: máximo caos
    'final_chaos': 0.05,         # Final: casi sin caos
    
    # Velocidad de las ondas
    'initial_speed': 3.0,        # Inicio: movimiento rápido
    'final_speed': 0.5,          # Final: movimiento lento
    
    # Amplitud de las ondas (altura en píxeles)
    'initial_amplitude': 80,     # Inicio: ondas grandes
    'final_amplitude': 30,       # Final: ondas suaves
    
    # Paletas de colores para la transición visual
    'colors': {
        # Fase Caótica - Naranjas (asociados con energía/alerta)
        'chaos': [
            {'r': 194, 'g': 65, 'b': 12},      # orange-700
            {'r': 234, 'g': 88, 'b': 12},      # orange-600
            {'r': 249, 'g': 115, 'b': 22},     # orange-500
            {'r': 251, 'g': 146, 'b': 60}      # orange-400
        ],
        # Fase Calma - Turquesa/Lavanda (asociados con serenidad)
        'calm': [
            {'r': 45, 'g': 212, 'b': 191},     # teal-400
            {'r': 94, 'g': 234, 'b': 212},     # teal-300
            {'r': 167, 'g': 139, 'b': 250},    # violet-400
            {'r': 196, 'g': 181, 'b': 253}     # violet-300
        ]
    },
    
    # Textos mostrados durante el ejercicio
    'messages': {
        'start': 'Observa las ondas...',         # Mensaje inicial
        'middle': 'Siente como se calman...',    # Mensaje a mitad
        'end': 'Claridad mental',                # Mensaje al finalizar ondas
        'question': '¿Te sientes mucho mejor?',  # Pregunta final
        'success': 'Tu mente esta en calma.'     # Mensaje de éxito
    }
}

# ============================================
# CONFIGURACIÓN GENERAL
# ============================================
# Parámetros compartidos por todos los ejercicios
# Controlan transiciones y tiempos de UI
# ============================================
GENERAL = {
    'fade_duration': 1,          # Duración de transiciones fade (segundos)
    'message_display_time': 2,   # Tiempo que se muestran mensajes (segundos)
    'welcome_duration': 3        # Duración pantalla de bienvenida (segundos)
}

# ============================================
# COLORES DE UI - Página Principal (index.html)
# ============================================
# Single Source of Truth para la interfaz visual
# Formato HEX para uso directo en CSS/Jinja2
#
# Estructura:
#   - theme: Colores base del diseño
#   - ansiedad/ira/estres: Colores específicos por emoción
#   - orbs: Configuración de los orbs animados del fondo
# ============================================
UI_COLORS = {
    # ========================================
    # Colores base del tema oscuro
    # ========================================
    'theme': {
        'bg_primary': '#0a0a0f',     # Fondo principal (casi negro)
        'bg_secondary': '#12121a',   # Fondo secundario (gris muy oscuro)
        'accent': '#a78bfa'          # Color de acento (violeta)
    },
    
    # ========================================
    # Colores por emoción (tarjetas en index.html)
    # Cada emoción tiene su paleta consistente
    # ========================================
    
    # Ansiedad - Paleta fría (azul/turquesa)
    'ansiedad': {
        'primary': '#0ea5e9',        # sky-500 - Color principal del glow
        'secondary': '#14b8a6',      # teal-500 - Color secundario del glow
        'icon': '#22d3ee',           # cyan-400 - Color del icono SVG
        'label': '#22d3ee'           # cyan-400 - Color de la etiqueta
    },
    
    # Ira - Paleta cálida (rojo/rosa)
    'ira': {
        'primary': '#ef4444',        # red-500 - Color principal del glow
        'secondary': '#ec4899',      # pink-500 - Color secundario del glow
        'icon': '#f87171',           # red-400 - Color del icono SVG
        'label': '#f87171'           # red-400 - Color de la etiqueta
    },
    
    # Estrés - Paleta energética (naranja/violeta)
    'estres': {
        'primary': '#f97316',        # orange-500 - Color principal del glow
        'secondary': '#a78bfa',      # violet-400 - Color secundario del glow
        'icon': '#fb923c',           # orange-400 - Color del icono SVG
        'label': '#fb923c'           # orange-400 - Color de la etiqueta
    },
    
    # ========================================
    # Orbs del fondo animado (Canvas)
    # ========================================
    # Cada orb tiene:
    #   - x, y: Posición inicial (0.0 - 1.0, relativo al canvas)
    #   - r: Radio (0.0 - 1.0, relativo al tamaño mínimo del canvas)
    #   - color: [R, G, B] para gradientes radiales
    #   - speed: Velocidad de movimiento sinusoidal
    # ========================================
    'orbs': [
        {
            'x': 0.2, 'y': 0.3, 'r': 0.4,
            'color': [167, 139, 250],    # violet-400
            'speed': 0.0003
        },
        {
            'x': 0.8, 'y': 0.2, 'r': 0.35,
            'color': [236, 72, 153],     # pink-500
            'speed': 0.0004
        },
        {
            'x': 0.5, 'y': 0.7, 'r': 0.45,
            'color': [14, 165, 233],     # sky-500
            'speed': 0.00035
        },
        {
            'x': 0.7, 'y': 0.8, 'r': 0.3,
            'color': [249, 115, 34],     # orange-500
            'speed': 0.00045
        }
    ]
}
