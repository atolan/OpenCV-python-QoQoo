import cv2 as cv
# import numpy as np

img1 = cv.imread("image/1.jpg", 1)
img2 = cv.imread("image/2.jpg", 1)

sub = cv.subtract(img1, img2)

cv.imshow("added Image", sub)

if cv.waitKey(0) & 0xff == 27:
  cv.destroyAllWindows

