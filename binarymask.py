import cv2
import numpy as np

img = cv2.imread("d.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
lower = np.array([22, 52, 72])
upper = np.array([102, 255, 255])
mask = cv2.inRange(img_hsv, lower, upper)

output_img = img.copy()
output_img[np.where(mask==0)] = 0
output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)
output_img[np.where(output_img > 30)] = 255

cv2.imshow('Original', img)
cv2.imwrite('Mask6.png', output_img)

cv2.waitKey(0)