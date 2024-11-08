import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('..\ex-10\water_coins.jpg')
pix_val = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,threshold = cv.threshold(pix_val,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
opening = cv.morphologyEx(pix_val,cv.MORPH_OPEN,(3,3),iterations=2)
sure_bg = cv.morphologyEx(opening,cv.MORPH_DILATE,(3,3),iterations=2)

dist = cv.distanceTransform(opening,cv.DIST_L2,5)
_,sure_fg = cv.threshold(dist,0.7*np.max(dist),255,0)
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_fg)
_,markers = cv.connectedComponents(sure_fg)
markers += 1
markers[unknown ==1] = 255
cv.watershed(img,markers)

colored = np.zeros_like(img)
colored[markers == -1] = [0,255,0]  

segmented = cv.addWeighted(img,0.7,colored,0.7,0)
cv.imshow('segmented',segmented)

cv.waitKey(0)
cv.destroyAllWindows()