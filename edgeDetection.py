import cv2 as cv
import numpy as np
  
try:
    # Read image from disk.
    img = cv.imread("image/Pretty.png", 0)
  
    # Canny edge detection.
    edges = cv.Canny(img, 100, 200)
  
    # Write image back to disk.
    cv.imshow('Edge Detection', edges)
except IOError:
    print ('Error while reading files !!!')

cv.waitKey(0)