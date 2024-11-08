import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

#ideal - > d(u,v) < d0 then base = 1
#blp -> 1/(1-(d(u,v)/d0)**2*n))
#glp,ghp -> 1 + e**((-d(u,v))**2/2*d0**2))
img = cv2.imread('..\download.jpeg',0)

def euclidean(point1,point2):
    return math.dist(point1,point2)
    
def butterworthlp(img,d0,n):
    row,col = img.shape[:2]
    center = (row/2,col/2)
    base = np.zeros_like(img,dtype=np.float32)
    for i in range(row):
        for j in range(col):
            base[i,j] = 1 / (1 + ((euclidean((i, j), center) / d0) ** (2 * n)))
    return base

fft = np.fft.fft2(img)
f_shift = np.fft.fftshift(fft)

filtered = f_shift * butterworthlp(img,30,2)
ishift = np.fft.ifftshift(filtered)
org = np.fft.ifft2(ishift)
cv2.imshow('orginal',np.uint8(np.abs(org)))
cv2.waitKey(0)
cv2.destroyAllWindows()