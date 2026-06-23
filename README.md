# 🖱️ Motion-Based Mouse Mover

A modern **Motion-Based Mouse Mover** built with **Python**, **OpenCV**, **MediaPipe**, and **Flask** that enables users to control their computer's mouse cursor using **hand movements** captured through a webcam. The application uses real-time computer vision and AI-powered hand tracking to provide a touchless, intuitive, and interactive human-computer interaction experience.

> **Control your computer effortlessly with hand gestures—no physical mouse required.**

---

# ✨ Features

- 🖐️ Real-time hand tracking
- 🖱️ Motion-based mouse cursor control
- 🎥 Live webcam processing
- 🤖 AI-powered hand landmark detection
- ⚡ Smooth cursor movement
- 🌐 Flask-based web interface
- 📱 Responsive dashboard
- 🎯 High-precision gesture tracking
- 💻 Cross-platform compatibility
- 🚀 Lightweight and fast performance

---

# 🛠️ Tech Stack

## Backend

- Python 3.x
- Flask

## Computer Vision

- OpenCV
- MediaPipe Hands

## Automation

- PyAutoGUI

## Scientific Computing

- NumPy

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Jinja2 Templates

---

# 📚 Main Libraries Used

| Library | Purpose |
|----------|---------|
| **Flask** | Web framework |
| **OpenCV** | Webcam access and image processing |
| **MediaPipe** | Hand landmark detection and tracking |
| **PyAutoGUI** | Mouse cursor automation |
| **NumPy** | Numerical calculations and coordinate mapping |

---

# 📂 Project Structure

```text
Motion-Based-Mouse-Mover/
│
├── app.py
├── mouse_controller.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── assets/
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── base.html
│
├── utils/
│   ├── hand_tracker.py
│   ├── mouse_mapper.py
│   └── ...
│
└── ...
```

---

# 🚀 Features Overview

- 🖐️ Hand Detection
- 🖱️ Cursor Movement
- 🎥 Live Webcam Feed
- 🤖 AI Hand Tracking
- 🌐 Flask Web Interface
- ⚡ Real-Time Processing
- 📱 Responsive UI
- 💻 Cross-Platform Support
- 🎯 Accurate Motion Detection
- 🚀 Easy Deployment

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/subham-paul/Motion-Based-Mouse-Mover.git
```

```bash
cd Motion-Based-Mouse-Mover
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
python app.py
```

or

```bash
flask run
```

---

# 🌐 Open in Browser

```
http://127.0.0.1:5000
```

---

# ⚙️ How It Works

### Step 1 — Webcam Capture

The webcam continuously captures live video frames.

---

### Step 2 — Hand Detection

MediaPipe detects the user's hand and identifies **21 hand landmarks** in real time.

---

### Step 3 — Motion Tracking

The system tracks the position of the user's index finger and calculates its movement inside the camera frame.

---

### Step 4 — Coordinate Mapping

The detected hand coordinates are mapped to the monitor's screen resolution using NumPy calculations.

---

### Step 5 — Cursor Control

PyAutoGUI moves the mouse cursor according to the tracked hand motion, enabling touchless navigation.

---

### Step 6 — Real-Time Interaction

The cursor updates continuously, providing smooth and responsive control of the computer using natural hand movements.

---

# 🧠 System Workflow

```text
Webcam
    │
    ▼
OpenCV Video Capture
    │
    ▼
MediaPipe Hand Detection
    │
    ▼
Hand Landmark Tracking
    │
    ▼
Coordinate Mapping
    │
    ▼
PyAutoGUI Mouse Control
    │
    ▼
Cursor Movement
```

---

# ✋ Hand Gesture Interaction

| Hand Motion | Action |
|-------------|--------|
| ☝️ Move Index Finger | Move Mouse Cursor |
| ✋ Hand Detection | Enable Tracking |
| 🚫 No Hand Detected | Pause Cursor Movement |

> *Additional gestures such as click, drag, or scroll can be implemented in future versions.*

---

# 📊 Applications

- Touchless Computer Control
- Smart Classrooms
- Accessibility Solutions
- Human-Computer Interaction
- Interactive Presentations
- Smart Kiosks
- AI Demonstrations
- Computer Vision Projects
- Gesture-Based Interfaces
- Research & Education

---

# 🚀 Future Enhancements

- 👆 Left Click Gesture
- 👆 Right Click Gesture
- 🤏 Drag and Drop
- 🔄 Scroll Control
- ✌️ Multi-Hand Detection
- 🧠 Deep Learning Gesture Recognition
- 🗣️ Voice Command Integration
- 📱 Mobile Device Support
- ☁️ Cloud Analytics
- 🎮 Gesture-Based Gaming Controls

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.

2. Create a feature branch.

```bash
git checkout -b feature/NewFeature
```

3. Commit your changes.

```bash
git commit -m "Add New Feature"
```

4. Push your changes.

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request.

---

# 🐞 Reporting Issues

Found a bug or have a feature request?

Please create an issue with detailed information.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## **Subham Paul**

Passionate about **Artificial Intelligence, Computer Vision, Python, Flask, Automation, and Human-Computer Interaction.**

- **GitHub:** https://github.com/subham-paul
- **LinkedIn:** https://www.linkedin.com/in/subham-paul-india/

---

# ⭐ Show Your Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the project
- 🤝 Contribute
- 💬 Share your feedback


---

## 🙏 Acknowledgements

Special thanks to the open-source communities behind:

- Python
- Flask
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

for providing the technologies that made this project possible.

---

> **"Transforming hand movements into seamless computer interaction through the power of Computer Vision and Artificial Intelligence."** 🖱️🤖🖐️
