import cv2
import numpy as np
from matplotlib import pyplot as plt
from ..utils.media import get_image_path

path = get_image_path('ronaldo.jpg')
img = cv2.imread(path, 0)

plt.hist(img.ravel(), 256, [0, 256])
plt.show()
