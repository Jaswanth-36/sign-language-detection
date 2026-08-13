import os

import cv2
import numpy as np

from utils.hand_tracking import HandTracker
from utils.landmarks import normalize_landmarks_dual

SIGN_NAME = "there"
SAMPLES = 80
SAVE_DIR = f"data/dataset/{SIGN_NAME}"
os.makedirs(SAVE_DIR, exist_ok=True)

cap = cv2.VideoCapture(0)
tracker = HandTracker(maxHands=2)
count = 0
skip = 0

while count < SAMPLES:
    ret, img = cap.read()
    if not ret:
        break

    img = tracker.findHands(img)
    hands = tracker.getLandmarks()

    if hands:
        features = normalize_landmarks_dual(
            hands[0], hands[1] if len(hands) > 1 else None
        )

        if features is not None and len(features) == 126:
            if skip >= 8:
                np.save(f"{SAVE_DIR}/{count}.npy", features)
                print(f"Saved {count + 1}/{SAMPLES}")
                count += 1
                skip = 0
            else:
                skip += 1

    cv2.putText(img, f"{SIGN_NAME}: {count}/{SAMPLES}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Collecting Sign Samples", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Dataset collection complete: {count} samples in {SAVE_DIR}")
