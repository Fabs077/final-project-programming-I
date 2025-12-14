# ============================================
# PARAMETROS DE CONFIGURACION
# Centro de Bienestar Emocional
# ============================================

# ============================================
# ANSIEDAD - Ejercicio de Respiracion 4-4
# Tecnica: Inhalar 4s, Exhalar 4s (5 ciclos)
# ============================================
ANSIEDAD = {
    'inhale_time': 4,
    'exhale_time': 4,
    'pause_time': 0.5,
    'cycles': 5,
    'colors': {
        # Inhalar - azules claros (calma)
        'inhale': [
            {'r': 14, 'g': 165, 'b': 233},    # sky-500
            {'r': 56, 'g': 189, 'b': 248},    # sky-400
            {'r': 125, 'g': 211, 'b': 252},   # sky-300
            {'r': 6, 'g': 182, 'b': 212},     # cyan-500
            {'r': 34, 'g': 211, 'b': 238},    # cyan-400
            {'r': 103, 'g': 232, 'b': 249}    # cyan-300
        ],
        # Exhalar - teals/verdes (tranquilidad)
        'exhale': [
            {'r': 103, 'g': 232, 'b': 249},   # cyan-300
            {'r': 45, 'g': 212, 'b': 191},    # teal-400
            {'r': 20, 'g': 184, 'b': 166},    # teal-500
            {'r': 13, 'g': 148, 'b': 136},    # teal-600
            {'r': 16, 'g': 185, 'b': 129},    # emerald-500
            {'r': 52, 'g': 211, 'b': 153}     # emerald-400
        ]
    },
    'messages': {
        'inhale': 'Inhala',
        'exhale': 'Exhala',
        'question': '¿Te sientes mucho mejor?',
        'success': 'Ahora estas en control.'
    }
}

# ============================================
# IRA - Ejercicio de Respiracion 4-7-8
# Tecnica: Inhalar 4s, Mantener 7s, Exhalar 8s
# ============================================
IRA = {
    'inhale_time': 4,
    'hold_time': 7,
    'exhale_time': 8,
    'cycles': 2,
    'colors': {
        # Rojo (Inhalar)
        'red': [
            {'r': 127, 'g': 29, 'b': 29},
            {'r': 153, 'g': 27, 'b': 27},
            {'r': 185, 'g': 28, 'b': 28},
            {'r': 220, 'g': 38, 'b': 38},
            {'r': 239, 'g': 68, 'b': 68},
            {'r': 248, 'g': 113, 'b': 113}
        ],
        # Rojo -> Amarillo (Mantener)
        'red_to_yellow': [
            {'r': 239, 'g': 68, 'b': 68},
            {'r': 234, 'g': 88, 'b': 12},
            {'r': 249, 'g': 115, 'b': 22},
            {'r': 251, 'g': 146, 'b': 60},
            {'r': 253, 'g': 186, 'b': 116},
            {'r': 251, 'g': 191, 'b': 36},
            {'r': 252, 'g': 211, 'b': 77},
            {'r': 250, 'g': 204, 'b': 21},
            {'r': 253, 'g': 224, 'b': 71}
        ],
        # Amarillo -> Violeta (Exhalar)
        'yellow_to_violet': [
            {'r': 253, 'g': 224, 'b': 71},
            {'r': 163, 'g': 230, 'b': 53},
            {'r': 74, 'g': 222, 'b': 128},
            {'r': 45, 'g': 212, 'b': 191},
            {'r': 34, 'g': 211, 'b': 238},
            {'r': 56, 'g': 189, 'b': 248},
            {'r': 96, 'g': 165, 'b': 250},
            {'r': 59, 'g': 130, 'b': 246},
            {'r': 99, 'g': 102, 'b': 241},
            {'r': 139, 'g': 92, 'b': 246},
            {'r': 167, 'g': 139, 'b': 250}
        ]
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
    'duration': 30,
    'wave_count': 5,
    'initial_chaos': 1.0,
    'final_chaos': 0.05,
    'initial_speed': 3.0,
    'final_speed': 0.5,
    'initial_amplitude': 80,
    'final_amplitude': 30,
    'colors': {
        # Fase Caotica (Naranja)
        'chaos': [
            {'r': 194, 'g': 65, 'b': 12},
            {'r': 234, 'g': 88, 'b': 12},
            {'r': 249, 'g': 115, 'b': 22},
            {'r': 251, 'g': 146, 'b': 60}
        ],
        # Fase Calma (Turquesa/Lavanda)
        'calm': [
            {'r': 45, 'g': 212, 'b': 191},
            {'r': 94, 'g': 234, 'b': 212},
            {'r': 167, 'g': 139, 'b': 250},
            {'r': 196, 'g': 181, 'b': 253}
        ]
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
    'fade_duration': 1,
    'message_display_time': 2,
    'welcome_duration': 3
}
