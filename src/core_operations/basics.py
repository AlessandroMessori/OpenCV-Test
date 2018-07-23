import cv2
import os
import numpy as np

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "../images/ronaldo.jpg"
abs_file_path = os.path.join(script_dir, rel_path)

img = cv2.imread(abs_file_path)
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
cv2.imshow('crissy', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
