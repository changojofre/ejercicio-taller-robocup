import cv2
import numpy as np

img = cv2.imread("potrero.jpg")
img3 = img.copy()
h, w, c = img.shape

sup_izq = img[0:h//2, 0:w//2]
sup_der = img[0:h//2, w//2:w]

img3[h//2:h, w//2:w] = sup_izq
img3[h//2:h, 0:w//2] = sup_der

cv2.imshow("original", img)
cv2.imshow("cuadros cruzados", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
