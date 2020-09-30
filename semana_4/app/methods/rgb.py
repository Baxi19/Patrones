import cv2 as cv
import numpy as np

img = cv.imread('image1.jpg')
z = np.zeros(img.shape[:2], 'uint8')

b, g, r = cv.split(img)
blue = cv.merge([b, z, z])
green = cv.merge([z, g, z])
red = cv.merge([z, z, r])

img2 = np.hstack([blue, green, red])

cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()