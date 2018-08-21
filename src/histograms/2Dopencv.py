import cv2
from ..utils.media import get_image_path

path = get_image_path('ronaldo.jpg')
img = cv2.imread(path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

#this method gives an histogram difficult to read
cv2.imshow('hist2D', hist)

cv2.waitKey(0)
cv2.destroyAllWindows()
