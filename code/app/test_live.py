from pathlib import Path
import time

import cv2
import joblib
import numpy as np

from code.services.audio_manager import AudioManager
from code.services.language_map import LANGUAGE_MAP
from code.utils.hand_tracking import HandTracker
from code.utils.landmarks import normalize_landmarks_dual

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "models" / "sign_dual_model.pkl"
CONFIDENCE_THRESHOLD = 0.55
BUFFER_SIZE = 3
MATCH_COUNT = 2
FRAME_SKIP = 2
SIGN_HOLD_TIME = 0.6

LANG_KEYS = {
    ord("1"): ("en", "English"),
    ord("2"): ("hi", "Hindi"),
    ord("3"): ("te", "Telugu"),
    ord("4"): ("ta", "Tamil"),
}
current_lang, current_lang_name = "en", "English"

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Trained model not found: {MODEL_PATH}")

model, labels = joblib.load(MODEL_PATH)
tracker = HandTracker(maxHands=2)
audio = AudioManager(gap=1.2)
prediction_buffer = []
frame_count = 0
last_detected_sign = ""
display_text = ""
last_update_time = 0.0
last_pred_idx = None

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 15)
if not cap.isOpened():
    audio.cleanup()
    raise RuntimeError("Unable to open the default webcam (camera index 0).")

print("SIGN LANGUAGE RECOGNIZATION - LIVE TEST")
print("1-English | 2-Hindi | 3-Telugu | 4-Tamil | q-Quit")

try:
    while True:
        ret, img = cap.read()
        if not ret:
            print("Unable to read a frame from the webcam. Exiting.")
            break

        frame_count += 1
        detected_sign = ""
        tracker.findHands(img)

        if frame_count % FRAME_SKIP == 0:
            hands = tracker.getLandmarks()
            if not hands:
                prediction_buffer.clear()
                last_pred_idx = None
            else:
                features = normalize_landmarks_dual(
                    hands[0], hands[1] if len(hands) > 1 else None
                )
                if features is not None and features.shape == (126,):
                    probs = model.predict_proba([features])[0]
                    idx = int(np.argmax(probs))
                    if probs[idx] >= CONFIDENCE_THRESHOLD:
                        if last_pred_idx is not None and idx != last_pred_idx:
                            prediction_buffer.clear()
                        prediction_buffer.append(idx)
                        if len(prediction_buffer) > BUFFER_SIZE:
                            prediction_buffer.pop(0)
                        if prediction_buffer.count(idx) >= MATCH_COUNT:
                            detected_sign = labels[idx]
                        last_pred_idx = idx

        now = time.time()
        if detected_sign in LANGUAGE_MAP:
            if detected_sign != last_detected_sign or now - last_update_time > SIGN_HOLD_TIME:
                display_text = LANGUAGE_MAP[detected_sign][current_lang]
                audio.speak(display_text)
                last_detected_sign = detected_sign
                last_update_time = now

        cv2.putText(
            img,
            f"Language: {current_lang_name} | Press 1-4 to change",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
        )
        if display_text:
            cv2.putText(
                img,
                display_text,
                (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.6,
                (0, 255, 255),
                3,
            )

        cv2.imshow("SIGN LANGUAGE RECOGNIZATION - LIVE TEST", img)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

        if key in LANG_KEYS:
            current_lang, current_lang_name = LANG_KEYS[key]
            if last_detected_sign in LANGUAGE_MAP:
                display_text = LANGUAGE_MAP[last_detected_sign][current_lang]
                audio.speak(display_text)
            print(f"Switched to {current_lang_name}")
finally:
    cap.release()
    cv2.destroyAllWindows()
    audio.cleanup()
    print("Live test ended successfully")
