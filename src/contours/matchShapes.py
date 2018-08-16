import cv2
from ..utils.media import get_image_path

squarePath = get_image_path('square.png')
rectanglePath = get_image_path('rectangle.png')
circlePath = get_image_path('circle.png')

square = cv2.imread(squarePath, 0)
rectangle = cv2.imread(rectanglePath, 0)
circle = cv2.imread(circlePath, 0)

ret, thresh = cv2.threshold(square, 127, 255, 0)
ret, thresh2 = cv2.threshold(rectangle, 127, 255, 0)
ret, thresh3 = cv2.threshold(circle, 127, 255, 0)

_, contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt1 = contours[0]
_, contours, hierarchy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]
_, contours, hierarchy = cv2.findContours(thresh3, 2, 1)
cnt3 = contours[0]

ret = cv2.matchShapes(cnt1, cnt2, 1, 0)
print("comparing square and rectangle...")
print(ret)

ret = cv2.matchShapes(cnt1, cnt3, 1, 0)
print("comparing square and circle...")
print(ret)
