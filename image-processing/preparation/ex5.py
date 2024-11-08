import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pywt

img = cv.imread('..\download.jpeg',0)
#fourier
# fft = np.fft.fft2(img)
# f_shift = np.fft.fftshift(fft)
# cv.imshow('freq',np.uint8(np.abs(1+f_shift)))
# ishift = np.fft.ifftshift(f_shift)
# org = np.fft.ifft2(ishift)
# cv.imshow('orginal',np.uint8(np.abs(org)))

#dct
# img_f = np.float32(img)
# dct = cv.dct(img_f,cv.DCT_INVERSE)

# cv.imshow('frequency',dct)
# org = cv.idct(dct)
# cv.imshow('original',np.uint8(org))

#pywt

coeffs = pywt.dwt2(img,'bior1.3')
ca,(ch,cV,cd) = coeffs

cv.imshow('freq',np.uint8(ca))

org = pywt.idwt2(coeffs,'bior1.3')
cv.imshow('orginal',np.uint8(org))


cv.waitKey(0)
cv.destroyAllWindows()