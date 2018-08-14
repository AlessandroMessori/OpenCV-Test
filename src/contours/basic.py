import cv2
from ..utils.media import get_image_path

path = get_image_path('ronaldo.jpg')
img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[4]
imag = cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)

cv2.imshow('img', img)
cv2.imshow('img2', image)
cv2.imshow('img3', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
