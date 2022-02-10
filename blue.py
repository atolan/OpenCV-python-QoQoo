import cv2 as cv
import matplotlib.pyplot as mpl

try: 
  original = cv.imread("image/1.jpg", 1)
  gaussian = cv.GaussianBlur(original, (7,7), 0)
  median = cv.medianBlur(original, 5)
  bilateral = cv.bilateralFilter(original, 9, 75, 75)

  titles = ["Original", "Gaussian", "Median", "Bilateral"]
  imgs = [original, gaussian, median, bilateral]

  count = 4

  for i in range(count):
    mpl.subplot(2, 2, i+1 )
    mpl.title(titles[i])
    mpl.imshow(imgs[i])

  mpl.show()

except IOError:
  print("Image Read Error")

cv.waitKey(0)  