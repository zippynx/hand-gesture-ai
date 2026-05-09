# 🤖 Gesture Control AI

A futuristic AI-powered desktop controller that allows you to manage system volume, screen brightness, and act as a virtual mouse using real-time hand gestures. Built with Python, OpenCV, and MediaPipe.

## ✨ Features

* **Multi-Mode System:** Seamlessly switch between different control modes using keyboard triggers.
* **🔊 Volume Control (Mode `V`):** Adjust system volume by pinching your thumb and index finger.
* **☀️ Brightness Control (Mode `B`):** Control screen brightness with the same intuitive pinch gesture.
* **🖱️ Virtual Mouse (Mode `M`):** Move your cursor using your index finger and click by pinching.
* **📸 Quick Screenshot:** Press `S` to take an instant screen capture of your workspace.
* **Interactive UI:** Real-time visual feedback, FPS counter, and mode indicators drawn directly on the webcam feed.

## 🛠️ Tech Stack

* **Python 3.x**
* **OpenCV (`cv2`)** - Computer vision and webcam frame processing
* **MediaPipe** - Real-time advanced hand tracking and landmark detection
* **Pycaw & Comtypes** - Windows system audio manipulation
* **Screen-Brightness-Control** - Multi-monitor brightness adjustment
* **PyAutoGUI** - Virtual mouse movement and automated clicks
* **NumPy & Math** - Coordinate interpolation and distance calculation

## 📁 Project Structure

```text
gesture-control-ai/
│
├── main.py                 # Main application loop and mode logic
├── hand_tracker.py         # MediaPipe hand tracking module
├── volume_controller.py    # Pycaw volume integration
├── brightness_control.py   # System brightness integration
├── virtual_mouse.py        # PyAutoGUI mouse mapping
├── gesture_actions.py      # Quick actions (screenshots, etc.)
├── requirements.txt        # Dependencies
└── README.md
```

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/gesture-control-ai.git
   cd gesture-control-ai
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 How to Use

1. Run the main script:
   ```bash
   python main.py
   ```

2. Make sure your hand is visible to the webcam.
3. Press the following keys to change modes:
   * `V` - Switch to Volume Mode
   * `B` - Switch to Brightness Mode
   * `M` - Switch to Virtual Mouse Mode
   * `S` - Take a Screenshot
   * `Q` - Quit the application
   