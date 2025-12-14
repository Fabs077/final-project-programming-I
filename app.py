from flask import Flask, render_template, request, send_from_directory
from parameters import ANSIEDAD, IRA, ESTRES, GENERAL

app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

@app.route('/')
def index():
    """Página principal"""
    show_param = request.args.get('show', 'welcome')
    show_welcome = show_param == 'welcome'
    return render_template('index.html', show_welcome=show_welcome)

@app.route('/select/ansiedad')
def select_ansiedad():
    """Ruta para Ansiedad - Ejercicio de respiración"""
    return render_template('ansiedad.html', config=ANSIEDAD, general=GENERAL)

@app.route('/select/ira')
def select_ira():
    """Ruta para Ira - Ejercicio de respiracion con transicion de colores"""
    return render_template('ira.html', config=IRA, general=GENERAL)

@app.route('/select/estres')
def select_estres():
    """Ruta para Estrés - Ondas de sincronizacion mental"""
    return render_template('estres.html', config=ESTRES, general=GENERAL)

@app.route('/styles.css')
def serve_styles():
    """Servir archivo CSS"""
    return send_from_directory('.', 'styles.css', mimetype='text/css')

if __name__ == '__main__':
    print("=" * 50)
    print("🌟 Centro de Bienestar Emocional")
    print("=" * 50)
    print("🚀 Servidor iniciando...")
    print("📡 Accede a: http://localhost:5000")
    print("💡 Para detener el servidor: Ctrl+C")
    print("=" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
