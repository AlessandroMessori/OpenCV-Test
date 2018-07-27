import cv2
import numpy as np
from matplotlib import pyplot as plt
from ..utils.media import get_image_path

path = get_image_path('ronaldo.jpg')
img = cv2.imread(path)

kernel = np.ones((5, 5), np.float32) / 25
averaging = cv2.filter2D(img, -1, kernel)
blur = cv2.GaussianBlur(img, (5, 5), 0)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(averaging), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.show()
