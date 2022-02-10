import cv2 as cv
import numpy as np
import matplotlib.pyplot  as plt

img = cv.imread("image/1.jpg")

half = cv.resize(img, (0,0), fx = 0.1, fy = 0.1)
small = cv.resize(img, (900, 600))
shrink = cv.resize(img, (600, 900), interpolation = cv.INTER_NEAREST)
# img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.uint8)

img_erosion = cv.erode(img, kernel, iterations=1)
img_dilation = cv.dilate(img, kernel, iterations=1)

Titles = ['Origin', 'Half', 'Small', 'Shrink']

images = [img, half, img_erosion, img_dilation]
# images = [img, half, small, shrink]

count = 4

for i in range(count):
  plt.subplot(2, 2, i+1)
  plt.title(Titles[i])
  plt.imshow(images[i])

plt.show()

