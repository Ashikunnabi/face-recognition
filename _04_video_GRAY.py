import cv2
import numpy as np

capture = cv2.VideoCapture("a.mp4")

while True:
    # Capturing frame by frame
    is_captureable, frame = capture.read()
    # Converting video colot RGB to GRAY
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Showing captured image as video
    cv2.imshow('Normal Video', frame)
    cv2.imshow('Gray Video', gray)
    # Getting out from loop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
