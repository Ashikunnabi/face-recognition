import cv2
import numpy as np


# Resize video
def rescale_frame(frame, percent=75):
    scale_percent = percent
    width         = int(frame.shape[1] * scale_percent / 100)
    height        = int(frame.shape[0] * scale_percent / 100)
    dim           = (width, height)    
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

# Capturing video
capture = cv2.VideoCapture("a.mp4")
# Calling the trained model
face = cv2.CascadeClassifier('E:\\Courses\\Programming Exercises\\Python\\Open CV\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
# Collecting fram by frame
while True:
    is_captureAble, frame = capture.read()
    # Resize function called
    frame = rescale_frame(frame, percent=50)
    # Converting the video RGB to GRAY
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detecting Face
    faces = face.detectMultiScale(gray, 1.5, 5)
    # Marking face with ractangle
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
    # Showing Result    
    cv2.imshow('Capturing...', frame)

    # Press q to stop process
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Close all
capture.release()
cv2.destroyAllWindows()
