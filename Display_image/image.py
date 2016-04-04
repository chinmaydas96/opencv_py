import cv2
image=cv2.imread('/home/user/image.jpg',cv2.IMREAD_COLOR)
cv2.imshow(' window ',image)
cv2.waitkey()
