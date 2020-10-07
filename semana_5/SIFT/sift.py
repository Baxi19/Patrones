import cv2 as cv


# Scale-Invariant Feature Transform
def sift(image_name):
    img = cv.imread(image_name)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    sift_ = cv.SIFT_create()
    kp = sift_.detect(gray, None)
    img = cv.drawKeypoints(gray, kp, img)
    cv.imshow(image_name + '.jpg' + ' - SIFT', img)
    cv.waitKey()

sift("../img.jpg")