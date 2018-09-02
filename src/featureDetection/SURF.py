import cv2
from ..utils.media import get_image_path

pathname = get_image_path('match.jpeg')
img = cv2.imread(pathname)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
surf = cv2.xfeatures2d.SURF_create(50)
kp, des = surf.detectAndCompute(img, None)
img = cv2.drawKeypoints(gray, kp, img)

cv2.imshow('SURF', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
