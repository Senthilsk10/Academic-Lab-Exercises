import cv2,math
import numpy as np
from matplotlib import pyplot as plt

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


def idealFilterLP(d0,imgshape):
    base = np.zeros(imgshape[:2])
    rows,cols = img.shape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((x,y),center)<d0:
                base[y,x] = 1
    return base

img = cv2.imread('images.png',0)
plt.imshow(img,cmap="gray")
plt.xticks([])
plt.yticks([])
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
im = ax.imshow(np.abs(idealFilterLP(50, img.shape)), cmap='gray')
ax.set_title('Ideal Low Pass Filter of Diameter 25 px')
ax.set_xticks([])
ax.set_yticks([])

fig, ax = plt.subplots()
im = ax.imshow(np.log(1+np.abs(fshift * idealFilterLP(50,img.shape))),cmap='gray')
ax.set_title('Filtered Image in Frequency Domain')
ax.set_xticks([])
ax.set_yticks([])

fig, ax = plt.subplots()
im = ax.imshow(np.log(1+np.abs(np.fft.ifftshift(fshift *idealFilterLP(50,img.shape)))), cmap='gray')
ax.set_title('Filtered Image inverse fft shifted')
ax.set_xticks([])
ax.set_yticks([])

fig, ax = plt.subplots()
im = ax.imshow(np.log(1+np.abs(np.fft.ifft2(np.fft.ifftshift(fshift *
idealFilterLP(50,img.shape))))), cmap='gray')
ax.set_title('Final Filtered Image In Spatial Domain')
ax.set_xticks([])
ax.set_yticks([])

cv2.waitKey(0)
cv2.destroyAllWindows()

