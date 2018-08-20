import cv2
import numpy as np
from ..utils.media import get_image_path

path = get_image_path('ronaldo.jpg')
img = cv2.imread(path, 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))  # stacking images side-by-side
cv2.imshow('res.png', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
