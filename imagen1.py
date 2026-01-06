import cv2
import numpy as np

img = cv2.imread("potrero.jpg")
h, w, c = img.shape

img1 = img.copy()

img1[0:h//2, :, 0] = 0
img1[0:h//2, :, 1] = 0

img1[h//2:h, :, 0] = 0
img1[h//2:h, :, 2] = 0

cv2.imshow("original", img)
cv2.imshow("potrero en rojo y verde", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()