import cv2
import numpy as np
from PIL import Image

class MineFace:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def pixelate_face(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            small = cv2.resize(face, (16, 16), interpolation=cv2.INTER_NEAREST)
            pixelated = cv2.resize(small, (w, h), interpolation=cv2.NEAREST)
            frame[y:y+h, x:x+w] = pixelated

        return frame
