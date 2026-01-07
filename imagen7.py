import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, c = frame.shape
    mitad_izq = frame[:, :w//2]
    frame[:, w//2:] = cv2.flip(mitad_izq, 1)

    cv2.imshow("video", frame)

    if cv2.waitKey(1) & 0xFF == 27: #esto lo busque, y es el esc
        break

cap.release()
cv2.destroyAllWindows()

# Martu: Bien!
