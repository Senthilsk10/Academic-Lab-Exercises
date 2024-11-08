import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('..\download.jpeg',0)
# hist = cv.calcHist([img],[0],None,[256],[0,256])
# plt.plot(hist,color='red')
# plt.show()
# norm = cv.normalize(hist,hist,0,1,cv.NORM_MINMAX)
# plt.plot(norm)
# plt.show()
equ = cv.equalizeHist(img)
plt.hist(equ.flatten(),256,[0,256],color='red')
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()