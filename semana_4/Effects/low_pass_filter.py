import cv2

def low_pass_filter(name):
    img = cv2.imread(name)
    img1 = cv2.bilateralFilter(img, 9, 75, 75)  # Bilateral LPF
    img2 = cv2.GaussianBlur(img1, (5, 5), 0)    # Gaussian LFP
    img3 = cv2.medianBlur(img2, 5)              # Median LFP

    img4 = cv2.resize(img3, (500, 300))         # New size
    img5 = cv2.resize(img4, (960, 777))         # Original size

    cv2.imshow('original', img)
    cv2.imshow('Low-Pass-Filtered & resized', img5)  # Multi filtered & resized image
    cv2.waitKey()