"""
app.py - Servidor Principal del Centro de Bienestar Emocional

Este módulo configura y ejecuta el servidor Flask que sirve la aplicación web.
Actúa como controlador principal, conectando las rutas URL con los templates HTML
y pasando los parámetros de configuración desde parameters.py.

Arquitectura:
    - Flask maneja las peticiones HTTP
    - Jinja2 (integrado en Flask) renderiza los templates
    - parameters.py contiene toda la configuración centralizada

Rutas disponibles:
    /                   -> Página principal con selección de emociones
    /select/ansiedad    -> Ejercicio de respiración 4-4
    /select/ira         -> Ejercicio de respiración 4-7-8
    /select/estres      -> Visualización de ondas calmantes
"""

from flask import Flask, render_template, request, send_from_directory
from parameters import ANSIEDAD, IRA, ESTRES, GENERAL, UI_COLORS

# Inicialización de Flask
# - template_folder='.' -> Busca templates en el directorio actual
# - static_folder='.'   -> Sirve archivos estáticos desde el directorio actual
# - static_url_path=''  -> URLs de archivos estáticos sin prefijo (ej: /styles.css)
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')


# ============================================
# RUTAS DE LA APLICACIÓN
# ============================================

@app.route('/')
def index():
    """
    Página principal - Pantalla de bienvenida y selección de emociones.
    
    Flujo:
        1. Primera visita: muestra pantalla de bienvenida (3 segundos)
        2. Redirección automática: muestra las 3 tarjetas de emociones
    
    Query Parameters:
        show (str): 'welcome' para bienvenida, 'main' para contenido principal
    
    Variables pasadas al template:
        show_welcome (bool): Controla qué pantalla mostrar
        ui (dict): Colores de UI desde parameters.py para estilos dinámicos
    
    Returns:
        str: HTML renderizado de index.html
    """
    show_param = request.args.get('show', 'welcome')
    show_welcome = show_param == 'welcome'
    return render_template('index.html', show_welcome=show_welcome, ui=UI_COLORS)


@app.route('/select/ansiedad')
def select_ansiedad():
    """
    Ejercicio de respiración para Ansiedad - Técnica 4-4.
    
    Técnica:
        - Inhalar: 4 segundos
        - Exhalar: 4 segundos
        - Repetir: 5 ciclos (~45 segundos total)
    
    Variables pasadas al template:
        config (dict): Tiempos, colores y mensajes específicos de ansiedad
        general (dict): Configuración general (duraciones de fade, etc.)
    
    Returns:
        str: HTML renderizado de ansiedad.html
    """
    return render_template('ansiedad.html', config=ANSIEDAD, general=GENERAL)


@app.route('/select/ira')
def select_ira():
    """
    Ejercicio de respiración para Ira - Técnica 4-7-8.
    
    Técnica:
        - Inhalar: 4 segundos (color rojo)
        - Mantener: 7 segundos (transición rojo -> amarillo)
        - Exhalar: 8 segundos (transición amarillo -> violeta)
        - Repetir: 2 ciclos (~38 segundos total)
    
    Variables pasadas al template:
        config (dict): Tiempos, colores y mensajes específicos de ira
        general (dict): Configuración general (duraciones de fade, etc.)
    
    Returns:
        str: HTML renderizado de ira.html
    """
    return render_template('ira.html', config=IRA, general=GENERAL)


@app.route('/select/estres')
def select_estres():
    """
    Visualización de ondas para Estrés - Sincronización mental.
    
    Técnica:
        - Duración: 30 segundos
        - Ondas visuales que transicionan de caóticas a calmadas
        - Usa Perlin Noise para movimiento orgánico
        - Colores: naranja (caos) -> turquesa/lavanda (calma)
    
    Variables pasadas al template:
        config (dict): Parámetros de ondas, colores y mensajes de estrés
        general (dict): Configuración general (duraciones de fade, etc.)
    
    Returns:
        str: HTML renderizado de estres.html
    """
    return render_template('estres.html', config=ESTRES, general=GENERAL)


@app.route('/styles.css')
def serve_styles():
    """
    Sirve el archivo CSS compartido.
    
    Nota:
        Flask normalmente sirve archivos estáticos automáticamente,
        pero esta ruta explícita asegura el MIME type correcto
        y evita problemas de caché en desarrollo.
    
    Returns:
        Response: Archivo styles.css con Content-Type: text/css
    """
    return send_from_directory('.', 'styles.css', mimetype='text/css')


# ============================================
# PUNTO DE ENTRADA
# ============================================

if __name__ == '__main__':
    # Mensaje de bienvenida en consola
    print("=" * 50)
    print("🌟 Centro de Bienestar Emocional")
    print("=" * 50)
    print("🚀 Servidor iniciando...")
    print("📡 Accede a: http://localhost:5000")
    print("💡 Para detener el servidor: Ctrl+C")
    print("=" * 50)
    
    # Iniciar servidor Flask
    # - debug=True: Recarga automática al guardar cambios
    # - host='0.0.0.0': Accesible desde cualquier IP (útil para testing en red local)
    # - port=5000: Puerto estándar de Flask
    app.run(debug=True, host='0.0.0.0', port=5000)
