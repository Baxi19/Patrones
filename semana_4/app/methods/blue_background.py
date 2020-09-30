import cv2
import numpy as np

image = cv2.resize(cv2.imread('../static/images/im.jpg'), (200,200), interpolation=cv2.INTER_CUBIC)
im_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100,50,50])
upper_blue = np.array([130,255,255])

mask = cv2.inRange(im_hsv, lower_blue, upper_blue)
cv2.imshow("Imagen", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()