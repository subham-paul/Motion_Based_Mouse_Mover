# =====================================================
# Motion-Based Mouse Mover — FIXED GESTURE SYSTEM
# =====================================================

import cv2
import time
import threading
import pyautogui
import mediapipe as mp
import numpy as np
import os
from flask import Flask, render_template, jsonify, request

# ------------------ APP ------------------
app = Flask(__name__)
pyautogui.FAILSAFE = False

# ------------------ GLOBAL STATE ------------------
thread = None
stop_event = threading.Event()
is_running = False

SCREEN_W, SCREEN_H = pyautogui.size()

last_action_time = 0
ACTION_DELAY = 1.2   # cooldown between actions

cursor_speed = 0.05
pinch_threshold = 35

os.makedirs("screenshots", exist_ok=True)

# ------------------ MEDIAPIPE ------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75
)
draw = mp.solutions.drawing_utils

# ------------------ UTIL FUNCTIONS ------------------
def distance(p1, p2):
    return np.linalg.norm(
        np.array([p1.x * SCREEN_W, p1.y * SCREEN_H]) -
        np.array([p2.x * SCREEN_W, p2.y * SCREEN_H])
    )

def count_fingers(lm):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    fingers.append(lm.landmark[4].x < lm.landmark[3].x)

    # Other fingers
    for i in range(1, 5):
        fingers.append(lm.landmark[tips[i]].y < lm.landmark[tips[i] - 2].y)

    return fingers.count(True)

# ------------------ MAIN CONTROLLER ------------------
def gesture_controller():
    global last_action_time

    cam = cv2.VideoCapture(0)

    while not stop_event.is_set():
        ret, frame = cam.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = hands.process(rgb)

        gesture_text = "No Hand"

        if res.multi_hand_landmarks:
            lm = res.multi_hand_landmarks[0]
            draw.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)

            fingers = count_fingers(lm)
            now = time.time()

            index_tip = lm.landmark[8]
            thumb_tip = lm.landmark[4]

            mx, my = int(index_tip.x * SCREEN_W), int(index_tip.y * SCREEN_H)
            pinch_dist = distance(index_tip, thumb_tip)
            is_pinch = pinch_dist < pinch_threshold

            # ================= PRIORITY LOGIC =================

            # 🤏 PINCH → LEFT CLICK
            if is_pinch and fingers <= 2 and now - last_action_time > ACTION_DELAY:
                pyautogui.click()
                last_action_time = now
                gesture_text = "Left Click (Pinch)"

            # ☝️ MOVE CURSOR
            elif fingers == 1 and not is_pinch:
                pyautogui.moveTo(mx, my, duration=cursor_speed)
                gesture_text = "Move Cursor"

            # ✌️ RIGHT CLICK
            elif fingers == 2 and now - last_action_time > ACTION_DELAY:
                pyautogui.rightClick()
                last_action_time = now
                gesture_text = "Right Click"

            # 🤟 SCREENSHOT
            elif fingers == 3 and now - last_action_time > ACTION_DELAY:
                pyautogui.screenshot(f"screenshots/screen_{int(time.time())}.png")
                last_action_time = now
                gesture_text = "Screenshot"

            # ✋ UNDO
            elif fingers == 5 and now - last_action_time > ACTION_DELAY:
                pyautogui.hotkey("ctrl", "z")
                last_action_time = now
                gesture_text = "Undo"

            # ✊ REDO
            elif fingers == 0 and now - last_action_time > ACTION_DELAY:
                pyautogui.hotkey("ctrl", "y")
                last_action_time = now
                gesture_text = "Redo"

            # Overlay
            cv2.putText(frame, gesture_text, (20, 45),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)

        cv2.imshow("Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

# ------------------ ROUTES ------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/start", methods=["POST"])
def start():
    global thread, is_running
    if not is_running:
        stop_event.clear()
        thread = threading.Thread(target=gesture_controller, daemon=True)
        thread.start()
        is_running = True
    return jsonify({"status": "started"})

@app.route("/stop", methods=["POST"])
def stop():
    global is_running
    stop_event.set()
    is_running = False
    return jsonify({"status": "stopped"})

@app.route("/calibrate", methods=["POST"])
def calibrate():
    global cursor_speed, pinch_threshold
    data = request.json
    cursor_speed = float(data["speed"])
    pinch_threshold = int(data["pinch"])
    return jsonify({"ok": True})

# ------------------ MAIN ------------------
if __name__ == "__main__":
    app.run(debug=True)
