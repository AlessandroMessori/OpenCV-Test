import cv2
from ..utils.media import get_image_path

pathname = get_image_path('game.mp4')
cap = cv2.VideoCapture(pathname)  # take first frame of the video
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
