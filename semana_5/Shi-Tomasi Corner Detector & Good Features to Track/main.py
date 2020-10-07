import numpy as np
import cv2
from matplotlib import pyplot as plt
def corners(image, quantity):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray,quantity,0.01,10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),3,255,-1)

    cv2.imshow('IMG',img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

image = '../img2.jpg'
quantity = 250
corners(image, quantity)