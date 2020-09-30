import cv2
import matplotlib.pyplot as plt

# reading the image
image = cv2.imread('../static/images/fd.jpeg')

im_res = cv2.resize(image, (200,200), interpolation=cv2.INTER_CUBIC)

color = ('b','g','r')

for i, col in enumerate(color):
    histr = cv2.calcHist([im_res], [i], None, [256], [0,256])
    plt.plot(histr, color=col)
    plt.xlim([0,256])

plt.show()