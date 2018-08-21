import cv2
from matplotlib import pyplot as plt
from ..utils.media import get_image_path

path = get_image_path('sunset.jpg')
img = cv2.imread(path)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

plt.imshow(hist, interpolation='nearest')
plt.show()
