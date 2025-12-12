from flask import Flask, render_template, request, jsonify, send_from_directory
import json
from datetime import datetime
import os

app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

# Base de datos en memoria para almacenar las selecciones
emotion_log = []

# Mensajes personalizados para cada emoción
EMOTION_RESPONSES = {
    'ansiedad': {
        'title': 'Trabajando en tu Ansiedad',
        'message': 'Respira profundo. La ansiedad es temporal y puedes superarla. Te recomendamos: técnicas de respiración profunda, meditación guiada y ejercicios de grounding para reconectar con el presente.',
        'recommendations': [
            'Practica la respiración 4-7-8',
            'Realiza 10 minutos de meditación',
            'Sal a caminar al aire libre',
            'Escribe tus pensamientos en un diario'
        ],
        'color': 'cyan'
    },
    'ira': {
        'title': 'Gestionando tu Ira',
        'message': 'Es completamente normal sentir ira. Lo importante es canalizar esa energía de forma positiva. Vamos a trabajar juntos en técnicas efectivas para gestionar estas emociones intensas.',
        'recommendations': [
            'Cuenta hasta 10 antes de reaccionar',
            'Realiza actividad física intensa',
            'Practica comunicación asertiva',
            'Identifica los desencadenantes'
        ],
        'color': 'red'
    },
    'estres': {
        'title': 'Reduciendo tu Estrés',
        'message': 'El estrés es parte de la vida moderna, pero no debe controlarte. Vamos a encontrar formas efectivas de recuperar tu balance, bienestar y paz interior.',
        'recommendations': [
            'Establece prioridades claras',
            'Toma descansos regulares',
            'Practica yoga o estiramientos',
            'Organiza tu espacio de trabajo'
        ],
        'color': 'orange'
    }
}

@app.route('/')
def index():
    """Página principal"""
    # Verificar si se debe mostrar la pantalla principal o la de bienvenida
    show_param = request.args.get('show', 'welcome')
    show_welcome = show_param == 'welcome'
    return render_template('index.html', show_welcome=show_welcome)

@app.route('/select/<emotion>')
def select_emotion_page(emotion):
    """Página de selección de emoción"""
    emotion = emotion.lower()
    
    # Validar que la emoción es válida
    if emotion not in EMOTION_RESPONSES:
        return render_template('index.html', 
                             show_welcome=False, 
                             error="Emoción no válida")
    
    # Registrar la selección
    log_entry = {
        'emotion': emotion,
        'timestamp': datetime.now().isoformat(),
        'ip': request.remote_addr
    }
    emotion_log.append(log_entry)
    
    # Obtener respuesta personalizada
    response_data = EMOTION_RESPONSES[emotion]
    
    return render_template('result.html', 
                         emotion=emotion,
                         title=response_data['title'],
                         message=response_data['message'],
                         recommendations=response_data['recommendations'],
                         color=response_data['color'])

@app.route('/styles.css')
def serve_styles():
    """Servir archivo CSS"""
    return send_from_directory('.', 'styles.css', mimetype='text/css')

@app.route('/script.js')
def serve_script():
    """Servir archivo JavaScript"""
    return send_from_directory('.', 'script.js', mimetype='application/javascript')

@app.route('/select_emotion', methods=['POST'])
def select_emotion():
    """Endpoint para procesar la selección de emoción"""
    try:
        data = request.get_json()
        emotion = data.get('emotion', '').lower()
        
        # Validar que la emoción es válida
        if emotion not in EMOTION_RESPONSES:
            return jsonify({
                'error': 'Emoción no válida',
                'message': 'Por favor selecciona una opción válida'
            }), 400
        
        # Registrar la selección
        log_entry = {
            'emotion': emotion,
            'timestamp': datetime.now().isoformat(),
            'ip': request.remote_addr
        }
        emotion_log.append(log_entry)
        
        # Obtener respuesta personalizada
        response_data = EMOTION_RESPONSES[emotion]
        
        # Construir respuesta completa
        response = {
            'success': True,
            'title': response_data['title'],
            'message': response_data['message'],
            'recommendations': response_data['recommendations'],
            'color': response_data['color'],
            'timestamp': log_entry['timestamp']
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error del servidor',
            'message': str(e)
        }), 500

@app.route('/stats')
def get_stats():
    """Endpoint para obtener estadísticas de uso"""
    try:
        # Contar emociones
        emotion_counts = {
            'ansiedad': 0,
            'ira': 0,
            'estres': 0
        }
        
        for entry in emotion_log:
            emotion = entry.get('emotion')
            if emotion in emotion_counts:
                emotion_counts[emotion] += 1
        
        stats = {
            'total_selections': len(emotion_log),
            'emotion_counts': emotion_counts,
            'most_common': max(emotion_counts, key=emotion_counts.get) if emotion_log else None,
            'recent_entries': emotion_log[-10:] if emotion_log else []
        }
        
        return jsonify(stats), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error al obtener estadísticas',
            'message': str(e)
        }), 500

@app.route('/health')
def health_check():
    """Endpoint de salud del servidor"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    }), 200

# Manejador de errores 404
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'error': 'Recurso no encontrado',
        'message': 'La ruta solicitada no existe'
    }), 404

# Manejador de errores 500
@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        'error': 'Error interno del servidor',
        'message': 'Ha ocurrido un error inesperado'
    }), 500

if __name__ == '__main__':
    print("=" * 50)
    print("🌟 Centro de Bienestar Emocional")
    print("=" * 50)
    print("🚀 Servidor iniciando...")
    print("📡 Accede a: http://localhost:5000")
    print("💡 Para detener el servidor: Ctrl+C")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
