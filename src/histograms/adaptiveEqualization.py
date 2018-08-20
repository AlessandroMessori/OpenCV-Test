import cv2
from ..utils.media import get_image_path

path = get_image_path('ronaldo.jpg')
img = cv2.imread(path, 0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)

cv2.imshow('clahe_2', cl1)
cv2.waitKey(0)
cv2.destroyAllWindows()
