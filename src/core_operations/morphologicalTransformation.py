import cv2
import numpy as np
from ..utils.media import get_image_path

path = get_image_path('ronaldo.jpg')
img = cv2.imread(path, 0)
kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('crissy', img)
cv2.imshow('crissy1', erosion)
cv2.imshow('crissy2', dilation)
cv2.imshow('crissy3', opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
