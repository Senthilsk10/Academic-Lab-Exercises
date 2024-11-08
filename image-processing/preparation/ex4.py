import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('..\s&p.jpeg')
#smoothin using linear

blurred = cv.blur(img,(5,5))
cv.imshow('blurred',blurred)
#smoothin using non linear
cv.imshow('median blur',cv.medianBlur(img,5))

#sharpening using laplacian operator
kernal = np.array([
    [-1,-1,-1],
    [-1,9,-1],
    [-1,-1,-1]
])
sharp = cv.filter2D(img,cv.CV_8U,kernal)
cv.imshow('sharpened',sharp)
cv.waitKey(0)
cv.destroyAllWindows()