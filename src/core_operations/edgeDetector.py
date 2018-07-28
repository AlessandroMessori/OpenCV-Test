import cv2
from matplotlib import pyplot as plt
from ..utils.media import get_image_path

path = get_image_path('ronaldo.jpg')
img = cv2.imread(path, 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
