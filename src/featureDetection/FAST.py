import cv2
from ..utils.media import get_image_path

pathname = get_image_path('match.jpeg')
img = cv2.imread(pathname)

fast = cv2.FastFeatureDetector_create()
# find and draw the keypoints
kp = fast.detect(img, None)
img = cv2.drawKeypoints(img, kp, img)

cv2.imshow('FAST', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
