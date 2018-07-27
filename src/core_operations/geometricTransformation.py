import cv2
import numpy as np
from ..utils.media import get_image_path


def transform(rws, cls, tr):
    if tr == 'r':
        return cv2.getRotationMatrix2D((cls / 2, rws / 2), 90, 1)
    elif tr == 't':
        return np.float32([[1, 0, 100], [0, 1, 50]])
    else:
        raise ValueError("invalid input")


path = get_image_path('ronaldo.jpg')
img = cv2.imread(path)
rows, cols = img.shape[:2]

translation = ""
print("what do you want to do to the image?\n")

while translation == "":

    translation = str(raw_input("Press r to Rotate,t to Translate: "))
    if translation != "r" and translation != "t":
        print("wrong input,type again")
        translation = ""

    M = transform(rows, cols, translation)
    dst = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow('img', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
