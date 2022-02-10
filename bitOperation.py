import cv2 as cv

img1 = cv.imread("image/bit01.png", 1)
img2 = cv.imread("image/bit02.png", 1)

# dest_and = cv.bitwise_and(img1, img2, mask = None)
dest_or = cv.bitwise_or(img1, img2, mask = None)
# dest_xor = cv.bitwise_xor(img1, img2, mask = None)


cv.imshow("Bit Operation", dest_or)

if cv.waitKey(0) & 0xff == 27:
  cv.destroyAllWindows