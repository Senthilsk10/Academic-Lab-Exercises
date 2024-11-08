import cv2
import numpy as np
image = cv2.imread('water_coins.jpg')
cv2.imshow('img',image)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,threshold = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernal = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(threshold,cv2.MORPH_OPEN,kernal,iterations = 2)

sure_bg = cv2.dilate(opening,kernal,iterations=3)

dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)

ret , sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
sure_fg= np.uint8(sure_fg)

unknown = cv2.subtract(sure_bg,sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)

markers += 1
markers[unknown == 255] = 0

cv2.watershed(image,markers)

colored_markers = np.zeros_like(image)
colored_markers[markers==-1] = [0,255,0]

segmented_image = cv2.addWeighted(image,0.7,colored_markers,0.7,0)

cv2.imshow("segmented image",segmented_image)
cv2.waitKey(0)

cv2.destroyAllWindows()