import numpy as np
import cv2
import argparse

cap = cv2.VideoCapture(0)
ap = argparse.ArgumentParser()


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('web', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
