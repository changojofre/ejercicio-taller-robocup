import cv2
import numpy as np

def intercambiar_superior(imgA, imgB):
    h, w, c = imgA.shape

    A = imgA.copy()
    B = imgB.copy()

    A[0:h//2] = imgB[0:h//2]
    B[0:h//2] = imgA[0:h//2]

    return A, B


imgA = cv2.imread("cataratas.jpg")
imgB = cv2.imread("lago_nahuel.jpg")
resA, resB = intercambiar_superior(imgA, imgB)


cv2.imshow("Original A", imgA)
cv2.imshow("Original B", imgB)
cv2.imshow("A", resA)
cv2.imshow("B", resB)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Martu: Bien!! Este sería ele ejercicio 5...