import cv2
import numpy as np

capture = cv2.VideoCapture("a.mp4")


def apply_invert(frame):
    return cv2.bitwise_not(frame)

while True:
    # Capturing frame by frame
    is_captureAble, frame = capture.read()
    invert = apply_invert(frame)
    
    cv2.imshow('Capturing...', invert)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
