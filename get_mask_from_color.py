import cv2
import numpy as np

img = cv2.imread("img.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
lower = np.array([22, 93, 0])
upper = np.array([45, 255, 255])
mask = cv2.inRange(img_hsv, lower, upper)

output_img = img.copy()
output_img[np.where(mask==0)] = 0
output_img = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)
output_img[np.where(output_img > 30)] = 255

cv2.imshow('Original', img)
cv2.imshow('Mask', output_img)

cv2.waitKey(0)