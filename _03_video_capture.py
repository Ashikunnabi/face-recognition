import cv2
import numpy as np

capture = cv2.VideoCapture("a.mp4")

while True:
    # Capturing frame by frame
    is_captureable, frame = capture.read()
    # Showing captured image as video
    cv2.imshow('Capturing...', frame)
    # Getting out from loop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
