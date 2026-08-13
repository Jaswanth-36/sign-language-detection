import cv2
import mediapipe as mp


class HandTracker:
    def __init__(self, maxHands=2, detectionCon=0.6, trackCon=0.6):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=maxHands,
            min_detection_confidence=detectionCon,
            min_tracking_confidence=trackCon,
        )
        self.results = None

    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        return img

    def getLandmarks(self):
        hands = []
        if self.results and self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                hands.append([[lm.x, lm.y, lm.z] for lm in handLms.landmark])
            hands.sort(key=lambda h: h[0][0])
        return hands
