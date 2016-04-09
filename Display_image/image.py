# importing all the required library
import cv2
import numpy as np

# load an color image in grayscale whose value is 0,for color it's 1.
# load the image and show it. 

image=cv2.imread('/home/bat/messi5.jpg',0)
cv2.imshow(' window ',image)
r = 100.0 / image.shape[1]
dim = (100, int(image.shape[0] * r))
 
# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)
cv2.destroyWindow()
