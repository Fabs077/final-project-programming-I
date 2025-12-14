# ============================================
# PARAMETROS DE CONFIGURACION
# Centro de Bienestar Emocional
# ============================================

# ============================================
# ANSIEDAD - Ejercicio de Respiracion
# ============================================
ANSIEDAD = {
    'inhale_time': 4,           # Segundos para inhalar
    'exhale_time': 4,           # Segundos para exhalar
    'pause_time': 0.5,          # Pausa entre inhalar y exhalar
    'cycles': 5,                # Cantidad de ciclos de respiracion
    'circle_size': 150,         # Tamano del circulo en px
    'circle_scale': 2.2,        # Escala maxima del circulo al expandirse
    'colors': {
        'primary': '#0ea5e9',   # Azul cielo
        'secondary': '#06b6d4', # Cyan
        'tertiary': '#14b8a6',  # Teal
        'quaternary': '#10b981' # Verde esmeralda
    },
    'messages': {
        'inhale': 'Inhala',
        'exhale': 'Exhala',
        'question': '¿Te sientes mucho mejor?',
        'success': 'Ahora estas en control.'
    }
}

# ============================================
# IRA - Ejercicio de Respiracion con Transicion de Colores
# ============================================
IRA = {
    'inhale_time': 4,           # Segundos para inhalar (circulo se agranda)
    'hold_time': 7,             # Segundos para mantener (circulo tiembla, cambia a amarillo)
    'exhale_time': 8,           # Segundos para exhalar (circulo se encoge, cambia a violeta/azul)
    'cycles': 1,                # Solo 1 ciclo de respiracion
    'circle_size': 150,         # Tamano del circulo en px
    'circle_scale_inhale': 2.2, # Escala al inhalar (crece como el de ansiedad)
    'circle_scale_exhale': 1,   # Escala al exhalar (vuelve al tamano original)
    'colors': {
        # ========== FASE 1: ROJO (Inhalar) ==========
        'red_1': '#7f1d1d',      # Rojo muy oscuro
        'red_2': '#991b1b',      # Rojo oscuro
        'red_3': '#b91c1c',      # Rojo intenso oscuro
        'red_4': '#dc2626',      # Rojo intenso
        'red_5': '#ef4444',      # Rojo
        'red_6': '#f87171',      # Rojo claro
        'red_7': '#fca5a5',      # Rojo muy claro
        
        # ========== TRANSICION ROJO -> AMARILLO ==========
        'red_orange_1': '#ea580c',   # Rojo-naranja
        'red_orange_2': '#f97316',   # Naranja
        'orange_1': '#fb923c',       # Naranja claro
        'orange_2': '#fdba74',       # Naranja muy claro
        'orange_yellow_1': '#fbbf24', # Naranja-amarillo
        'orange_yellow_2': '#fcd34d', # Amarillo-naranja
        
        # ========== FASE 2: AMARILLO (Mantener) ==========
        'yellow_1': '#ca8a04',   # Amarillo oscuro/dorado
        'yellow_2': '#eab308',   # Amarillo dorado
        'yellow_3': '#facc15',   # Amarillo
        'yellow_4': '#fde047',   # Amarillo claro
        'yellow_5': '#fef08a',   # Amarillo muy claro
        'yellow_6': '#fef9c3',   # Amarillo palido
        
        # ========== TRANSICION AMARILLO -> VIOLETA/AZUL ==========
        'yellow_green_1': '#a3e635',  # Amarillo-verde
        'green_1': '#4ade80',         # Verde claro
        'green_cyan_1': '#2dd4bf',    # Verde-cyan
        'cyan_1': '#22d3ee',          # Cyan
        'cyan_blue_1': '#38bdf8',     # Cyan-azul
        'blue_1': '#60a5fa',          # Azul claro
        
        # ========== FASE 3: VIOLETA/AZUL (Exhalar) ==========
        'blue_2': '#3b82f6',      # Azul
        'blue_3': '#2563eb',      # Azul intenso
        'indigo_1': '#6366f1',    # Indigo
        'indigo_2': '#4f46e5',    # Indigo intenso
        'violet_1': '#8b5cf6',    # Violeta
        'violet_2': '#a78bfa',    # Violeta claro
        'violet_3': '#c4b5fd',    # Violeta muy claro
        'purple_1': '#a855f7',    # Purpura
        'purple_2': '#c084fc',    # Purpura claro
    },
    'messages': {
        'inhale': 'Inhala',
        'hold': 'Manten',
        'exhale': 'Exhala',
        'question': '¿Te sientes mucho mejor?',
        'success': 'Ahora estas en control.'
    }
}

# ============================================
# ESTRES - Ondas de Sincronizacion Mental
# ============================================
ESTRES = {
    'duration': 30,             # Duracion total del ejercicio (segundos)
    'wave_count': 5,            # Numero de ondas superpuestas
    'initial_chaos': 1.0,       # Nivel de caos inicial (0-1)
    'final_chaos': 0.05,        # Nivel de caos final (casi cero)
    'initial_speed': 3.0,       # Velocidad inicial de las ondas
    'final_speed': 0.5,         # Velocidad final (lenta, relajante)
    'initial_amplitude': 80,    # Amplitud inicial (picos altos)
    'final_amplitude': 30,      # Amplitud final (suave)
    'colors': {
        # Fase Caotica (Naranja Oxido / Ruido Mental)
        'chaos_1': '#c2410c',   # Naranja oxido oscuro
        'chaos_2': '#ea580c',   # Naranja oxido
        'chaos_3': '#f97316',   # Naranja intenso
        'chaos_4': '#fb923c',   # Naranja claro
        
        # Transicion
        'trans_1': '#f59e0b',   # Ambar
        'trans_2': '#fbbf24',   # Amarillo dorado
        'trans_3': '#a3e635',   # Lima
        'trans_4': '#34d399',   # Esmeralda
        
        # Fase Calma (Lavanda / Turquesa)
        'calm_1': '#2dd4bf',    # Turquesa
        'calm_2': '#5eead4',    # Turquesa claro
        'calm_3': '#a78bfa',    # Lavanda
        'calm_4': '#c4b5fd',    # Lavanda claro
        'calm_5': '#e0e7ff',    # Indigo muy claro
    },
    'messages': {
        'start': 'Observa las ondas...',
        'middle': 'Siente como se calman...',
        'end': 'Claridad mental',
        'question': '¿Te sientes mucho mejor?',
        'success': 'Tu mente esta en calma.'
    }
}

# ============================================
# CONFIGURACION GENERAL
# ============================================
GENERAL = {
    'fade_duration': 1,         # Duracion de efectos de desvanecimiento (segundos)
    'message_display_time': 2,  # Tiempo que se muestra el mensaje de exito (segundos)
    'welcome_duration': 3       # Duracion de la pantalla de bienvenida (segundos)
}
