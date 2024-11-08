import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('logo.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Input Image',img)
cv.imshow('Input Image flattened',img.flatten())

plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.show()
equ = cv.equalizeHist(img)
cv.imshow('Equalized',equ)
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()