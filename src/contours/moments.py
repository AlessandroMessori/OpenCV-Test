import cv2
from ..utils.media import get_image_path

path = get_image_path('juventus.jpeg')
img = cv2.imread(path, 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, _, _ = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)

img = cv2.drawContours(img, contours, 0, (0, 255, 0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
