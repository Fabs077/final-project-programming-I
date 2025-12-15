# 🧘 Centro de Bienestar Emocional

Aplicación web de respiración guiada diseñada para ayudar a los usuarios a gestionar emociones intensas (ansiedad, ira, estrés) en menos de 60 segundos.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Tailwind](https://img.shields.io/badge/Tailwind-CSS-38B2AC.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Características

### 🎯 3 Ejercicios Personalizados

| Ejercicio | Técnica | Duración | Descripción |
|-----------|---------|----------|-------------|
| 🌊 **Ansiedad** | 4-4 | ~45s | Respiración cuadrada con gradientes azul/cyan |
| 🔥 **Ira** | 4-7-8 | ~38s | Transición de colores (rojo → amarillo → violeta) |
| ⚡ **Estrés** | Ondas | ~30s | Visualización de ondas del caos a la calma |

### 🎨 UI/UX Moderno

- Animaciones Canvas a 60fps
- Diseño glassmorphism con gradientes animados
- Layout responsive para todos los dispositivos
- Acceso rápido optimizado (<3 segundos para empezar)
- Colores centralizados (Single Source of Truth)

### 📊 Feedback Visual

- Círculo de respiración que se expande/contrae
- Interpolación de colores dinámica
- Efectos glow sincronizados con las fases
- Indicadores de progreso

## 🚀 Inicio Rápido

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/centro-bienestar-emocional.git
   cd centro-bienestar-emocional
   ```

2. **Instalar dependencias:**
   ```bash
   pip install flask
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

4. **Abrir en el navegador:**
   ```
   http://localhost:5000
   ```

## 📁 Estructura del Proyecto

```
centro-bienestar-emocional/
├── app.py              # Servidor Flask y rutas
├── parameters.py       # Configuración centralizada (Single Source of Truth)
├── utils.js            # Funciones JS compartidas (DRY)
├── styles.css          # Estilos CSS compartidos (DRY)
├── index.html          # Página principal con selección de emociones
├── ansiedad.html       # Ejercicio de respiración para ansiedad
├── ira.html            # Ejercicio de respiración para ira
├── estres.html         # Visualización de ondas para estrés
└── README.md           # Este archivo
```

## 🏗️ Arquitectura

### Flujo de Datos

```
┌─────────────────┐     ┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  parameters.py  │ --> │   app.py    │ --> │   Jinja2     │ --> │  HTML final │
│  (configuración)│     │  (Flask)    │     │  (templates) │     │  (navegador)│
└─────────────────┘     └─────────────┘     └──────────────┘     └─────────────┘
```

### Principios de Diseño Aplicados

| Principio | Implementación |
|-----------|----------------|
| **DRY** | `utils.js` y `styles.css` compartidos entre ejercicios |
| **KISS** | Configuración simple en diccionarios Python |
| **YAGNI** | Solo funciones que realmente se usan |
| **Single Source of Truth** | Todos los colores en `parameters.py` |

## 🎯 Cómo Funciona

### Ejercicio de Ansiedad (Técnica 4-4)

```
Inhalar (4s) → Exhalar (4s) → Repetir x5
```

- **Beneficio:** Activa el sistema nervioso parasimpático
- **Colores:** Azul cielo → Cyan → Teal → Esmeralda
- **Visual:** Círculo que se expande al inhalar

### Ejercicio de Ira (Técnica 4-7-8)

```
Inhalar (4s) → Mantener (7s) → Exhalar (8s) → Repetir x2
```

- **Beneficio:** La exhalación prolongada activa el nervio vago
- **Colores:** Rojo (reconocer) → Amarillo (procesar) → Violeta (liberar)
- **Visual:** Círculo con efecto shake durante la retención

### Ejercicio de Estrés (Ondas de Sincronización)

```
30 segundos de visualización pasiva
```

- **Beneficio:** Reduce carga cognitiva, ideal para estrés alto
- **Colores:** Naranja caótico → Turquesa/Lavanda calmado
- **Visual:** 5 ondas con Perlin Noise que se sincronizan gradualmente

## ⚙️ Configuración

Todos los parámetros se configuran en `parameters.py`:

### Ejercicios de Respiración

```python
ANSIEDAD = {
    'inhale_time': 4,       # Duración de inhalación (segundos)
    'exhale_time': 4,       # Duración de exhalación (segundos)
    'cycles': 5,            # Número de repeticiones
    'colors': { ... }       # Paletas de colores RGB
}
```

### Colores de UI

```python
UI_COLORS = {
    'theme': {
        'bg_primary': '#0a0a0f',    # Fondo principal
        'accent': '#a78bfa'          # Color de acento
    },
    'ansiedad': {
        'primary': '#0ea5e9',        # Color principal
        'icon': '#22d3ee'            # Color del icono
    },
    # ... más emociones
}
```

## 🛠️ Stack Tecnológico

| Capa | Tecnología | Uso |
|------|------------|-----|
| **Backend** | Flask (Python) | Servidor web y rutas |
| **Templating** | Jinja2 | Variables dinámicas en HTML |
| **Frontend** | HTML5 + Tailwind CSS | Estructura y estilos |
| **Animaciones** | Canvas API | Fondos y círculo de respiración |
| **Matemáticas** | Interpolación lineal + Easing | Transiciones suaves |

## 📱 Responsive Design

La app está optimizada para:

- 🖥️ Desktop (grid de 3 columnas)
- 📱 Tablet (grid adaptativo)
- 📱 Mobile (stack vertical)

## 🔧 Funciones Principales (utils.js)

| Función | Descripción |
|---------|-------------|
| `lerp(a, b, t)` | Interpolación lineal entre dos valores |
| `lerpColor(c1, c2, t)` | Interpolación de colores RGB |
| `getColorFromArray(arr, progress)` | Color desde array con progreso |
| `easeInOutCubic(t)` | Curva de aceleración suave |
| `setupCanvas(canvas)` | Configura canvas responsive |
| `drawRadialGradient(...)` | Dibuja fondo con orbs animados |
| `updateCircleStyle(...)` | Actualiza estilo del círculo |

## 📝 Documentación del Código

Todos los archivos están completamente documentados:

- **Python:** Docstrings PEP 257 con descripción, parámetros y returns
- **JavaScript:** JSDoc con @param, @returns y @example
- **CSS:** Comentarios por sección explicando cada bloque
- **HTML:** Comentarios estructurados por componente

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Reconocimientos

- Técnicas de respiración basadas en investigación clínica
- UI inspirada en aplicaciones modernas de bienestar
- Construido con ❤️ para el bienestar emocional

---

> **Nota:** Esta aplicación es una herramienta para ayudar a gestionar emociones, no un reemplazo del apoyo profesional de salud mental. Si estás pasando por dificultades, por favor busca ayuda profesional.
