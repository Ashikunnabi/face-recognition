import cv2
import numpy as np

# Collecting Image
img = cv2.imread("a.png")
# Resizing Image
resized = cv2.resize(img, (int(img.shape[1]/2,int(img.shape[0]/2)))
# Calling the trained model
face_cascade = cv2.CascadeClassifier('E:\\Courses\\Programming Exercises\\Python\\Open CV\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
# Converting the image RGB to GRAY
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
# Detecting Face
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
# Marking face with ractangle
for (x,y,w,h) in faces:
    img = cv2.rectangle(resized, (x,y), (x+w, y+y), (0, 255, 0), 3)
# Showing Result
cv2.imshow('Capturing...', resized)
# Close all
cv2.waitKey(0)
cv2.destroyAllWindows()
