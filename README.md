# Centro de Bienestar Emocional 🌟

Una aplicación web interactiva diseñada para ayudar a gestionar emociones como ansiedad, ira y estrés, con una interfaz suave y relajante.

## 🎨 Características

- **Interfaz UI/UX moderna** con efectos blur y transiciones suaves
- **Diseño responsivo** usando Tailwind CSS
- **Backend en Python** con Flask
- **Efectos visuales relajantes** con gradientes animados
- **Mensajes personalizados** para cada emoción
- **Recomendaciones específicas** basadas en la selección

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. **Instala las dependencias de Python:**
   ```powershell
   pip install -r requirements.txt
   ```

## 💻 Uso

1. **Inicia el servidor Flask:**
   ```powershell
   python app.py
   ```

2. **Abre tu navegador y visita:**
   ```
   http://localhost:5000
   ```

3. **Experimenta la aplicación:**
   - Verás un mensaje de bienvenida que se desvanece
   - Selecciona una de las tres opciones (Ansiedad, Ira, Estrés)
   - Recibe recomendaciones personalizadas

## 📁 Estructura del Proyecto

```
final_project_programming_I/
│
├── app.py              # Backend Flask (lógica del servidor)
├── index.html          # Estructura HTML principal
├── styles.css          # Estilos personalizados y efectos blur
├── script.js           # Interactividad del frontend
├── requirements.txt    # Dependencias de Python
└── README.md          # Este archivo
```

## 🎨 Paleta de Colores

### Ansiedad (Azul y Verde)
- Azul cielo: `#0ea5e9`
- Cyan: `#06b6d4`
- Teal: `#14b8a6`
- Verde esmeralda: `#10b981`

### Ira (Rojo a Violeta)
- Rojo: `#ef4444`
- Naranja: `#f97316`
- Rosa: `#ec4899`
- Púrpura: `#a855f7`
- Violeta: `#8b5cf6`

### Estrés (Naranja óxido a Lavanda)
- Naranja: `#f97316`
- Naranja claro: `#fb923c`
- Amarillo: `#fbbf24`
- Púrpura claro: `#c084fc`
- Lavanda: `#a78bfa`

## 🛠️ Tecnologías Utilizadas

- **Frontend:**
  - HTML5
  - CSS3 (con efectos blur y animaciones)
  - Tailwind CSS (framework CSS)
  - JavaScript vanilla

- **Backend:**
  - Python 3
  - Flask (framework web)

## 📊 Endpoints de la API

- `GET /` - Página principal
- `POST /select_emotion` - Procesar selección de emoción
- `GET /stats` - Obtener estadísticas de uso
- `GET /health` - Verificar estado del servidor

## ✨ Características Técnicas

### Efectos Visuales
- Transiciones suaves con `cubic-bezier`
- Efectos blur animados en los botones
- Gradientes que cambian dinámicamente
- Animaciones de fade-in progresivas
- Partículas flotantes en el fondo

### Principios UI/UX Aplicados
- **Claridad:** Mensajes directos y fáciles de entender
- **Feedback visual:** Animaciones al interactuar
- **Accesibilidad:** Diseño responsivo para todos los dispositivos
- **Estética relajante:** Colores y efectos que transmiten calma
- **Jerarquía visual:** Elementos organizados por importancia

## 🔧 Personalización

Puedes personalizar la aplicación modificando:

- **Colores:** Edita las clases en `styles.css`
- **Mensajes:** Modifica el diccionario `EMOTION_RESPONSES` en `app.py`
- **Animaciones:** Ajusta los keyframes en `styles.css`
- **Tiempo de bienvenida:** Cambia el setTimeout en `script.js`

## 🐛 Solución de Problemas

### El servidor no inicia
```powershell
# Verifica que Flask esté instalado
pip list | Select-String flask

# Reinstala las dependencias
pip install -r requirements.txt
```

### Los estilos no se aplican
- Asegúrate de que `styles.css` esté en el mismo directorio que `index.html`
- Verifica tu conexión a internet (para Tailwind CDN)

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 👤 Autor

Creado con ❤️ para el proyecto final de Programación I

## 🙏 Agradecimientos

- Tailwind CSS por el framework
- Flask por el framework web
- La comunidad de desarrollo web por la inspiración

---

**¡Disfruta de tu viaje hacia el bienestar emocional! 🌈**
