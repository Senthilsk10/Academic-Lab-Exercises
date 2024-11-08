import numpy as np

import cv2

img = cv2.imread('download.jpeg',0)

#cv2.imshow("original",img)

f = np.fft.fft2(img)
fs = np.fft.fftshift(f)
hs = 15*np.log(1+np.abs(fs))# why 15, formula definition ?


cv2.imshow("transformed",np.uint8(hs))

#inversing

shifted_img = np.fft.ifftshift(fs)
inversed = np.fft.ifft2(shifted_img)
a_img = np.abs(inversed)

cv2.imshow("inversed",np.uint8(a_img))

cv2.waitKey(0)
cv2.destroyAllWindows()
