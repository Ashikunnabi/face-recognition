import cv2
import numpy as np

capture = cv2.VideoCapture("a.mp4")

# Changing the resolutions
def make_1080p():
    capture.set(3, 1920)
    capture.set(4, 1080)

def make_720p():
    capture.set(3, 1280)
    capture.set(4, 720)

def make_480p():
    capture.set(3, 640)
    capture.set(4, 480)

def change_res(width, height):
    capture.set(3, width)
    capture.set(4, height)

def rescale_frame(frame, percent=75):
    scale_percent = percent
    width         = int(frame.shape[1] * scale_percent / 100)
    height        = int(frame.shape[0] * scale_percent / 100)
    dim           = (width, height)    
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    
while True:
    # Capturing frame by frame
    is_captureable, frame = capture.read()
    # Resizing capture video
    frame = rescale_frame(frame, percent=30)
    # Showing captured image as video
    cv2.imshow('Normal Video', frame)
    # Getting out from loop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
