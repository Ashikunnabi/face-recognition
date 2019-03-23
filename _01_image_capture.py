import cv2
import numpy as np

# Color Image
img1 = cv2.imread("a.png",1)

# Gray Image
img2 = cv2.imread("a.png",0)


cv2.imshow('Color Image', img1)
cv2.imshow('Gray Image', img2)

# Press any key to close
cv2.waitKey(0)         # cv.waitKey(2000) Wait 2 sec and auto close
# Close all window
cv2.destroyAllWindows()
