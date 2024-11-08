import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

def distance(point1,point2):
 return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def gaussianHP(D0,imgShape):
 base = np.zeros(imgShape[:2])
 rows, cols = imgShape[:2]
 center = (rows/2,cols/2)
 for x in range(cols):
    for y in range(rows):
        base[y,x] = 1 - math.exp(((-distance((y,x),center)**2)/(2*(D0**2))))
 return base


img = cv2.imread('images.png',0)
plt.imshow(img, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()

f = np.fft.fft2(img)
mag = 20*np.log(np.abs(f))
plt.imshow(mag, cmap = 'gray')
plt.title('Magnitude Spectrum')
plt.xticks([]), plt.yticks([])
plt.show()

fshift = np.fft.fftshift(f)
mag = 20*np.log(np.abs(fshift))
plt.imshow(mag, cmap = 'gray')
plt.title('Centered Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

fig, ax = plt.subplots()

im = ax.imshow(np.abs(gaussianHP(50,img.shape)), cmap='gray')
ax.set_title('guassian high Pass Filter of Diameter 30 px')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

fig, ax = plt.subplots()
im = ax.imshow(np.log(1+np.abs(fshift * gaussianHP(50,img.shape))), cmap='gray')
ax.set_title('Filtered Image in Frequency Domain')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

fig, ax = plt.subplots()
im = ax.imshow(np.log(1+np.abs(np.fft.ifftshift(fshift * gaussianHP(50,img.shape)))), cmap='gray')
ax.set_title('Filtered Image inverse fft shifted')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

fig, ax = plt.subplots()
im = ax.imshow(np.log(1+np.abs(np.fft.ifft2(np.fft.ifftshift(fshift *gaussianHP(50,img.shape))))), cmap='gray')
ax.set_title('Final Filtered Image In Spatial Domain')
ax.set_xticks([])
ax.set_yticks([])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()