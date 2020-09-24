import cv2

# Method to apply contrats to an image
def contrast_image(image_dir, contrast, brightness):
    image = cv2.imread(image_dir)
    alpha = contrast  #1.5  # Contrast control (1.0-3.0)
    beta = brightness #0  # Brightness control (0-100)
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    cv2.imshow('original', image)
    cv2.imshow('adjusted', adjusted)
    cv2.waitKey()