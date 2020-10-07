import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def match(image1, image2, quantity):
    img1 = cv.imread(image1, cv.IMREAD_GRAYSCALE)          # queryImage
    img2 = cv.imread(image2, cv.IMREAD_GRAYSCALE) # trainImage
    # Initiate ORB detector
    orb = cv.ORB_create()
    # find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1,des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key = lambda x:x.distance)
    # Draw first quantity matches.
    img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:quantity],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imshow('IMG', img3)
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()


image1 = '../img2.jpg'
image2 = '../img3.jpg'
quantity = 30
match(image1,image2, quantity)