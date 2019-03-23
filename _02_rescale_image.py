import cv2
import numpy as np


img = cv2.imread("a.png",1)
## Rescalling the image----- DO not follow as it is not maintaining pixal ratio
# resized = cv2.resize(img, (200,200))
## Recomanded to use
resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow('Color Image', resized)

# Press any key to close
cv2.waitKey(0)
# Close all window
cv2.destroyAllWindows()
