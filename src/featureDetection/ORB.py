import numpy as np
import cv2
from matplotlib import pyplot as plt
from ..utils.media import get_image_path

pathname = get_image_path('match.jpeg')
img = cv2.imread(pathname)

orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img, None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, img)
plt.imshow(img2), plt.show()
