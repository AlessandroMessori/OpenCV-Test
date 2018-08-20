import cv2
from matplotlib import pyplot as plt
from ..utils.media import get_image_path

path = get_image_path('ronaldo.jpg')
img = cv2.imread(path)

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()
