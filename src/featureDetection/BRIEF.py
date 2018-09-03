import cv2
from ..utils.media import get_image_path

pathname = get_image_path('match.jpeg')
img = cv2.imread(pathname)

# Initiate STAR detector
star = cv2.xfeatures2d.StarDetector_create()
# Initiate BRIEF extractor
brief = cv2.xfeatures2d_BriefDescriptorExtractor.create()
# find the keypoints with STAR
kp = star.detect(img, None)
# compute the descriptors with BRIEF
kp, des = brief.compute(img, kp, img)
img = cv2.drawKeypoints(img, kp, img)

cv2.imshow('BRIEF', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
