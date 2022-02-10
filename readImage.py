import cv2 as cv
import numpy as np

img1 = cv.imread("image/1.jpg", 1)
img2 = cv.imread("image/2.jpg", 1)

h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]

ratio1 = 800 / w1
ratio2 = 800 / w2

dim1 = (800, int(h1 * ratio1))
dim2 = (800, int(h2 * ratio2))

resize1 = cv.resize(img1, dim1)
resize2 = cv.resize(img2, dim2)

addedImage = cv.addWeighted(resize1, 0.5, resize2, 0.5, 0)

cv.imshow("Pretty Kitty", img_erosion)
# cv.imwrite("image/Pretty kitty.png", addedImage)

cv.waitKey(0)

cv.destroyAllWindows()
