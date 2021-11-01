import cv2
import numpy as np

image = cv2.imread('Mask6.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
total = 0

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    mask = np.zeros(image.shape, dtype=np.uint8)
    cv2.fillPoly(mask, [c], [255,255,255])
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    pixels = cv2.countNonZero(mask)
    total += pixels
    cv2.putText(image, '{}'.format(pixels), (x,y - 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    print(pixels)

# print(c)


print(total)
# cv2.imshow('thresh', thresh)
cv2.imshow('img2.png', image)
cv2.waitKey(0)