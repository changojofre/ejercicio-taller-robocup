import cv2
import numpy as np

img = cv2.imread("potrero.jpg")
h, w, c = img.shape
img5 = img.copy()

img4 = img.copy()

sup_izq = img[0:h//2, 0:w//2].copy()
sup_der = img[0:h//2, w//2:w].copy()
inf_izq = img[h//2:h, 0:w//2].copy()
inf_der = img[h//2:h, w//2:w].copy()

img4[0:h//2, 0:w//2] = inf_der
img4[0:h//2, w//2:w] = inf_izq
img4[h//2:h, 0:w//2] = sup_der
img4[h//2:h, w//2:w] = sup_izq

cv2.imshow("Original", img)
cv2.imshow("", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Martu: No comprendo bien a qué consigna corresponde el ejercicio...