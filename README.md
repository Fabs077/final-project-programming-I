# 🧘 Emotional Wellness Center

A guided breathing web application designed to help users manage intense emotions (anxiety, anger, stress) within 60-90 seconds.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **3 Personalized Exercises:**
  - 🌊 **Anxiety** - 4-4 breathing technique with calming blue/cyan gradients
  - 🔥 **Anger** - 4-7-8 breathing with color transition (red → yellow → violet)
  - ⚡ **Stress** - Visual wave synchronization from chaos to calm

- **Modern UI/UX:**
  - Canvas-based animations with 60fps smooth rendering
  - Glassmorphism design with animated gradients
  - Responsive layout for all devices
  - Quick access optimized (<3 seconds to start)

- **Visual Feedback:**
  - Breathing circle that expands/contracts
  - Dynamic color interpolation
  - Glow effects synchronized with breathing phases
  - Progress indicators

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/emotional-wellness-center.git
   cd emotional-wellness-center
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser:**
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
emotional-wellness-center/
├── app.py              # Flask application & routes
├── parameters.py       # Configuration for all exercises
├── index.html          # Main page with emotion selection
├── ansiedad.html       # Anxiety breathing exercise
├── ira.html            # Anger breathing exercise
├── estres.html         # Stress wave visualization
├── styles.css          # Global styles
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🎯 How It Works

### Anxiety Exercise (4-4 Technique)
- **Inhale:** 4 seconds (circle expands)
- **Exhale:** 4 seconds (circle contracts)
- **Cycles:** 5 repetitions (~45 seconds)
- **Colors:** Blue → Cyan → Teal gradient

### Anger Exercise (4-7-8 Technique)
- **Inhale:** 4 seconds (red tones)
- **Hold:** 7 seconds (transition to yellow + shake)
- **Exhale:** 8 seconds (transition to violet)
- **Cycles:** 2 repetitions (~38 seconds)

### Stress Exercise (Wave Visualization)
- **Duration:** 30 seconds
- **Visual:** 5 sinusoidal waves with Perlin noise
- **Transition:** Chaotic orange → Synchronized lavender/turquoise
- **Goal:** Sync breathing with wave movement

## ⚙️ Configuration

All exercise parameters can be customized in `parameters.py`:

```python
ANSIEDAD = {
    'inhale_time': 4,      # seconds
    'exhale_time': 4,      # seconds
    'cycles': 5,           # repetitions
    'circle_scale': 2.2,   # max expansion
    ...
}
```

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
- **Animations:** Canvas API with requestAnimationFrame
- **Templating:** Jinja2

## 🎨 Design Principles

1. **Immediate Access:** Users in emotional distress need quick solutions
2. **Visual Calm:** Dark backgrounds with soft, flowing gradients
3. **Clear Feedback:** Always know what phase you're in
4. **Minimal Interaction:** One click to start, focus on breathing

## 📱 Responsive Design

The app is fully responsive and works on:
- Desktop browsers
- Tablets
- Mobile phones

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Breathing techniques based on clinical research
- UI inspired by modern wellness applications
- Built with ❤️ for emotional wellbeing

---

**Remember:** This app is a tool to help manage emotions, not a replacement for professional mental health support. If you're struggling, please reach out to a mental health professional.
