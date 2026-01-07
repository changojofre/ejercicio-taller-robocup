import cv2
import numpy as np

img = cv2.imread("potrero.jpg")
h, w, c = img.shape

img2 = img.copy()

mitad_izq = img[:, :w//2]
img2[:, w//2:] = cv2.flip(mitad_izq, 1)

cv2.imshow("original", img)
cv2.imshow("izq eb der", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Martu: Bien!!