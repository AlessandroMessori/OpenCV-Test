import cv2
from ..utils.media import get_image_path

path = get_image_path('juventus.jpeg')
img = cv2.imread(path, 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
image, contours, _ = cv2.findContours(thresh, 1, 2)


def printContourData(cnt):
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    epsilon = 0.1 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    k = cv2.isContourConvex(cnt)
    boundingRect = cv2.boundingRect(cnt)
    enclosingCircle = cv2.minEnclosingCircle(cnt)
    fitEllipse = cv2.fitEllipse(cnt)

    print("centroid coordinates:")
    print("x:" + str(cx) + ",y:" + str(cy))
    print("area:")
    print(str(area))
    print("perimeter:")
    print(str(perimeter))
    print("approximated polygon:")
    print(approx)
    print("is convex:")
    print(str(k))
    print("bounding rectangle:")
    print(str(boundingRect))
    print("enclosing circle:")
    print(str(enclosingCircle))
    print("bounding ellipse:")
    print(str(fitEllipse))


for (index, cnt) in enumerate(contours[:10]):
    print("countour number " + str(index) + ":")
    printContourData(cnt)
    print("--------------")
