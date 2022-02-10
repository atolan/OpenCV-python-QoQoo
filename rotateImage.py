import cv2 as cv
import numpy as np

M = np.float32([[1,0,300], [0,1,150]])

try:
  img = cv.imread("image/1.jpg", 1)
  (rows, cols) = img.shape[:2]

  ratio = 900 / cols
  dim = (900, int(rows*ratio))

  resize = cv.resize(img, dim)

  # M = cv.getRotationMatrix2D((450, int(rows*ratio) / 2), 45, 1)

  res = cv.warpAffine(resize, M, (900, int(rows*ratio)))

  cv.imshow("Rotated Image", res)
except IOError:
  print("Errors while reading images!!!")

cv.waitKey(0)