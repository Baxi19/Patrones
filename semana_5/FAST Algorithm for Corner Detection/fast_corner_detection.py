import cv2 as cv


# FAST Algorithm for Corner Detection
def fast_corner_detection(image_path):
    # Sencillo
    img = cv.imread(image_path, 0)
    fast = cv.FastFeatureDetector_create()
    kp = fast.detect(img, None)
    img2 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))
    cv.imshow('fast_true.png', img2)
    # Más sensible
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img,None)
    img3 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
    cv.imshow('fast_false.png', img3)
    cv.waitKey()


fast_corner_detection("../img.jpg")