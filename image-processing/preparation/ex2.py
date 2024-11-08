import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('..\download.jpeg',0)
#negative
neg = 255 - img
#log - c*log(1+r),c - 255/log(1+np.max(r))
img_f = np.float32(img)
c = 255/np.log(1+np.max(img_f))
log = c*np.log(1+img_f)
# gamma - c*r**g
gamma = 255*(img/255)**1.4
#contrast - ((r-r.min)/r.max-r.min)*255
# cont = np.zeros_like(img)
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         cont[i][j] = (img[i][j] - np.min(img))/(np.max(img)-np.min(img))*255
#intensity - make low and high and assign
cont = np.zeros_like(img)
low = 140
high = 180
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if low < img[i,j] and img[i,j] < high:
            cont[i,j] = 150
        else:
            cont[i,j] = 120
# cv.imshow('neg',neg)
# plt.imshow(log,cmap='gray')
# plt.show()
# plt.imshow(gamma,cmap='gray')
# plt.show()
plt.imshow(cont,cmap='gray')
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()